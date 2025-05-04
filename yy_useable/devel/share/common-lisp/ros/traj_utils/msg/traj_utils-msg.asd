
(cl:in-package :asdf)

(defsystem "traj_utils-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Bspline" :depends-on ("_package_Bspline"))
    (:file "_package_Bspline" :depends-on ("_package"))
    (:file "Circle" :depends-on ("_package_Circle"))
    (:file "_package_Circle" :depends-on ("_package"))
    (:file "CirclePoses" :depends-on ("_package_CirclePoses"))
    (:file "_package_CirclePoses" :depends-on ("_package"))
    (:file "DataDisp" :depends-on ("_package_DataDisp"))
    (:file "_package_DataDisp" :depends-on ("_package"))
    (:file "EgoInfo" :depends-on ("_package_EgoInfo"))
    (:file "_package_EgoInfo" :depends-on ("_package"))
    (:file "MultiBsplines" :depends-on ("_package_MultiBsplines"))
    (:file "_package_MultiBsplines" :depends-on ("_package"))
    (:file "TreePoses" :depends-on ("_package_TreePoses"))
    (:file "_package_TreePoses" :depends-on ("_package"))
    (:file "VelCmd" :depends-on ("_package_VelCmd"))
    (:file "_package_VelCmd" :depends-on ("_package"))
  ))