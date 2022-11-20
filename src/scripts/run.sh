set -ex
sudo service postgresql start
sudo service rabbitmq-server start
cd bin/go-cqhttp
nohup ./go-cqhttp >/dev/null 2>&1 &
