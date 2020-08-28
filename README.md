# service-migration
How to install go newest version in Ubuntu 18.04 
1. Firstly, need to download go version to your local host
 $ curl -O https://storage.googleapis.com/golang/go1.15.linux-amd64.tar.gz
2. Tar file and move go file to /usr/local
 $ tar -xvf go1.15.linux-amd64.tar.gz
 $ sudo mv go /usr/local
 $ rm go1.15.linux-amd64.tar.gz
3. Because in Ubuntu18.04, there is already older go version so to install new version you need to unlink older version or remove it first
 - Find when running the go command which file is called
 $ whereis go
 go: /usr/bin/go /usr/lib/go /usr/local/go /usr/share/go /usr/share/man/man1/go.1.gz
 - we can observe that /usr/bin/go is called when type command go. We should cd to this folder
 $ cd usr/bin
 - check which folder is link to go comand
 $ ls -la go
 $ sudo ln -s /usr/local/go/bin/go /usr/bin/go 
 $ vi .bashrc
