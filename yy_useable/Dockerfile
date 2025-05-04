FROM osrf/ros:noetic-desktop-full-focal

ADD 3rd /3rd
ADD ros.key /yy/ros.key

USER root

RUN apt-key add /yy/ros.key && apt update && apt install python3-catkin-tools -y && apt install ros-noetic-geographic-msgs ros-noetic-tf2-sensor-msgs ros-noetic-tf2-geometry-msgs ros-noetic-image-transport ros-noetic-mavros ros-noetic-ddynamic-reconfigure -y
RUN apt-get install liblapack-dev libsuitesparse-dev libcxsparse3 libgflags-dev libgoogle-glog-dev libgtest-dev libtool -y
#RUN cd /opt/ros/noetic/lib/mavros 
#RUN ./install_geographiclib_datasets.sh

RUN cd /3rd/glog && sh ./autogen.sh && sh ./configure && make && make install
RUN cd /3rd/ceres-solver-2.0.0rc1 && mkdir build && cd build && cmake ../ && make -j4 && make install

#RUN apt-get install -y python3-pip
#RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  jupyter

RUN apt-get install python3.7 -y #&& python3.8 -m pip3 install opencv-python rospy rospkg -i  https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install -y python3-pip

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

RUN pip3 install torch==1.13.0+cpu torchvision==0.14.0+cpu torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cpu -i https://pypi.tuna.tsinghua.edu.cn/simple


ADD src /yy/src/
WORKDIR /yy/
RUN . /opt/ros/noetic/setup.sh && catkin_make

RUN mkdir /yy/log
ADD path_test /yy/path_test


ADD setup.bash /yy
RUN chmod u+x /yy/setup.bash
#ADD sh /sh
#RUN chmod +x /sh/*.sh

ENTRYPOINT [ "/yy/setup.bash" ]
#ENTRYPOINT [ "/sh/vins.sh & /sh/planner.sh & /sh/path_vel.sh" ]
#ENTRYPOINT [ "/sh/planner.sh" ]
#ENTRYPOINT [ "/sh/path_vel.sh" ]
#AND [ "/sh/planner.sh" ]

