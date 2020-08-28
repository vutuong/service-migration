# service-migration
### How to install go newest version in Ubuntu 18.04 
1. Firstly, need to download go version to your local host
 ```
 $ curl -O https://storage.googleapis.com/golang/go1.15.linux-amd64.tar.gz
 ```
2. Tar file and move go file to /usr/local
 ```
 $ tar -xvf go1.15.linux-amd64.tar.gz
 ```
 ```
 $ sudo mv go /usr/local
 ```
 ```
 $ rm go1.15.linux-amd64.tar.gz
 ```
3. Because in Ubuntu18.04, there is already older go version so to install new version you need to unlink older version or remove it first
 - Find when running the go command which file is called
 ```
 $ whereis go
 ```
 ```
 go: /usr/bin/go /usr/lib/go /usr/local/go /usr/share/go /usr/share/man/man1/go.1.gz
 ```
 - we can observe that /usr/bin/go is called when type command go. We should cd to this folder
 ```
 $ cd usr/bin
 ```
 - check which folder is link to go comand
 ```
 $ ls -la go
 ```
 - If go version is old one, which mean that the go command is link to old version (bin go), we need to remove the symlink
 ```
 sudo unlink go
 ```
 - After unlink go, we can't run go command (e.g ```$ go version```), we need to link go to the new version
 - The go folder that we tar from downloaded file is moved to ```/usr/local/go``` at Step 2
 - We link this folder to usr/bin/go
 ```
 $ sudo ln -s /usr/local/go/bin/go /usr/bin/go
 ```
 - save and reload sources
 ```
 $ vi .bashrc
 ```
 - Addd this line to the end of file 
 ```export GOPATH=$HOME/go```
 - Apply the change by running the following command:
 ```
 $. .bashrc
 ```
 - Check go version
 ```
 $ go version
```
