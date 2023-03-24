#!/usr/bin/zsh
set -e

echo "----------Start Rabbitmq server----------"
sudo service rabbitmq-server start
# If use docker run this
# docker run -it -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

echo "----------Start go-cqhttp----------"
cd bin/go-cqhttp
nohup ./go-cqhttp >/dev/null 2>&1 &

cd ../..

echo "----------Init python env----------"

cd src
export PYTHONPATH=$PWD/src:$PYTHONPATH

echo "----------Start Rec module----------"
nohup python3 rec_module >/dev/null 2>&1 &

echo "----------Start Send module----------"
nohup python3 send_module >/dev/null 2>&1 &

for package in $PWD/plugins/*; do
    echo "----------Running $package----------"
    nohup python $package >/dev/null 2>&1 &
done
