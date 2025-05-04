import numpy as np
import cv2  
import time

class Stitcher:
    def __init__(self):
        self.matcher = cv2.DescriptorMatcher_create("BruteForce")
        self.descriptor = cv2.SIFT_create()
        pass

    def stitch(self, images, ratio=0.75, reprojThresh=4.0, showMatches=False):
        start = time.time()
        (imageB, imageA) = images
        
        (kpsA, featuresA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB) = self.detectAndDescribe(imageB)
        print('%.5f s' %(time.time()-start))

        # match features between the two images
        M = self.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh)
        print('%.5f s' %(time.time()-start))

        if M is None:
            return None, None

        # otherwise, apply a perspective warp to stitch the images together
        self.M = M
        (matches, H, status) = M
        result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
        print('%.5f s' %(time.time()-start))

        # check to see if the keypoint matches should be visualized
        if showMatches:
            vis = self.drawMatches(imageA, imageB, kpsA, kpsB, matches, status)
            print('%.5f s' %(time.time() - start))
            return (result, vis)

        return result, None
    
    def detectAndDescribe(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (kps, features) = self.descriptor.detectAndCompute(image, None)
        kps = np.float32([kp.pt for kp in kps])
    
        return (kps, features)

    #matchKeypoints方法需要四个参数,第一张图片的关键点和特征向量,第二张图片的关键点特征向量。
    #David Lowe’s ratio测试变量和RANSAC重投影门限也应该被提供。
    def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh):
        rawMatches = self.matcher.knnMatch(featuresA, featuresB, 2)
        
        matches = []
        for m in rawMatches:
            # ensure the distance is within a certain ratio of each
            # other (i.e. Lowe's ratio test)
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))

        # computing a homography requires at least 4 matches
        if len(matches) > 4:
            # construct the two sets of points
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])
            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)

            return (matches, H, status)
        return None

    #连线画出两幅图的匹配
    def drawMatches(self, imageA, imageB, kpsA, kpsB, matches, status, text = False):
        # initialize the output visualization image
        (hA, wA) = imageA.shape[:2]
        (hB, wB) = imageB.shape[:2]
        vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
        vis[0:hA, 0:wA] = imageA
        vis[0:hB, wA:] = imageB

        # loop over the matches
        for ((trainIdx, queryIdx), s) in zip(matches, status):
            # only process the match if the keypoint was successfully
            # matched
            if s == 1:
                # draw the match
                ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
                ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
                if text:
                    cv2.putText(vis,str(queryIdx), ptA, cv2.FONT_HERSHEY_COMPLEX, 3, (100,255,0), 1, cv2.LINE_AA)
                    cv2.putText(vis,str(trainIdx), ptB, cv2.FONT_HERSHEY_COMPLEX, 3, (100,255,0), 1, cv2.LINE_AA)
                cv2.line(vis, ptA, ptB, (0, 255, 0), 2)

        return vis