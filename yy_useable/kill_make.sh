for pid in `(ps -elf | grep RMUA | awk '{print $4}')` ; do echo $pid; kill -9 $pid ; done
for pid in `(docker ps | awk '{print $1}')` ; do echo $pid ; docker kill $pid ; done
sleep 0.5
