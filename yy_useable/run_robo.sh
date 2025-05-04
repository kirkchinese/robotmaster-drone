rm log/* -rf
xhost +local:docker
docker run -it --net host  -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /home/c/yy/log:/yy/log -e DISPLAY=$DISPLAY --name robo3 --rm  robo3
