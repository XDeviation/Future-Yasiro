set -ex
wget https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-rc3/go-cqhttp_linux_amd64.tar.gz -O bin/go-cqhttp.tar.gz
mkdir ./bin/go-cqhttp/
tar -xzvf ./bin/go-cqhttp.tar.gz -C ./bin/go-cqhttp/
rm ./bin/go-cqhttp.tar.gz
