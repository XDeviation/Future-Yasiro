#!/bin/bash
wget -P ./bin/go-cqhttp.tar.gz https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-rc3/go-cqhttp_darwin_amd64.tar.gz
tar -xzvf ./bin/go-cqhttp.tar.gz -C ./bin/go-cqhttp/
rm ./bin/go-cqhttp.tar.gz

