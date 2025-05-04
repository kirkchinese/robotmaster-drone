for pid in `(ps -elf | grep RMUA | awk '{print $4}')` ; do echo $pid; kill -9 $pid ; done
for pid in `(ps -elf | grep roslaunch | awk '{print $4}')` ; do echo $pid; kill -9 $pid ; done
for pid in `(ps -elf | grep "devel/lib" | awk '{print $4}')` ; do echo $pid; kill -9 $pid ; done
for pid in `(ps -elf | grep "python run" | awk '{print $4}')` ; do echo $pid; kill -9 $pid ; done


sleep 0.5
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
