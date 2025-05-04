#!/bin/bash
cd /yy
source devel/setup.bash

sleep 2.0

echo "run vins"
roslaunch vins fast_drone_250.launch > /yy/log/out_vins.log 2> /yy/log/err_vins.log & 
echo "-----------------------"
sleep 3.0

echo "run ctrl"
roslaunch airsim_ros controller.launch > /yy/log/out_ctrl.log 2> /yy/log/err_ctrl.log &
echo "----------------------"
sleep 5.0


#cd /home/sim/robo/src/myEnv
#source venv/bin/activate
#cd /usr/test/

echo "run run.py"
cd path_test
source ../devel/setup.bash
python3 run.py > /yy/log/run.log &
#tail -f /yy/log/run.log
echo "---------------------"

while true :
do 
    sleep 1
done
#source vins.sh

