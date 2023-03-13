set -ex

# install go-cqhttp
inctallGoCqhttp() {
    mkdir bin
    wget https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-rc4/go-cqhttp_linux_amd64.tar.gz -O bin/go-cqhttp.tar.gz
    mkdir ./bin/go-cqhttp/
    tar -xzvf ./bin/go-cqhttp.tar.gz -C ./bin/go-cqhttp/
    rm ./bin/go-cqhttp.tar.gz
}

# install docker (for rabbit mq)
installDocker() {
    sudo apt install docker docker.io
}

# install postgresql
installPostgresql() {
    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo apt-get update
    sudo apt-get -y install postgresql postgresql-client
}

# init python env
installPoetry() {
    sudo apt install -y python3-pip
    curl -sSL https://install.python-poetry.org | python3 -
    echo "export PATH=\$PATH:\$HOME/.local/bin" >>$HOME/.bashrc
    echo "export PATH=\$PATH:\$HOME/.local/bin" >>$HOME/.zshrc
}

echo "---------- install go-cqhttp ----------"
inctallGoCqhttp
echo "---------- install docker ----------"
installDocker
echo "---------- install postgresql ----------"
installPostgresql
