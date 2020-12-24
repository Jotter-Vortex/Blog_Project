# [Blog_Project](http://changjin.me/)
## 눌러보세요

##### ver2.0 : Add about menu, snow effect
##### ver2.1 : upper menu fixed




###### * 기술 스택
    −  Server-side
    −  1. python3
    −  2. MongoDB
    -  3. Jinja2
    -  4. AWS
    -  5. EC2 t2 micro
   
###### * for server
    −  ssh -i key ubuntu@IPNUM
    −  ps -ef | grep app.py
    −  kill -9
    -  sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000
    -  pip install requests beautifulsoup4 pymongo
    -  5. EC2 t2 micro   
###### * for MongoDB
    −   wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
    -   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
    -   sudo apt-get update
    -   sudo apt-get install -y mongodb-org
    -   sudo service mongod start
    -   >mongo
    -   use admin;
    -   db.createUser({user: "test", pwd: "test", roles:["root"]});
    -   sudo service mongod restart
    -   sudo vi /etc/mongod.conf
    -   * bindIp : 0.0.0.0
    -   * security : authorization: enabled #주석제거
    
###### * for pip
    −  sudo apt-get update
    −  sudo apt-get install -y python3-pip
    −  pip3 --version
    -  sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
    -  >pip install flask
   


### 문서화
  EC2 환경(env) 설정이 필요 (vi ~/.profile)
  
## for server
  need ssh -i key ubuntu@IPNUM

## Envirionment DB
export DB_URL={RDS URL}
export DB_NAME={DB username}
export DB_PASSWORD={DB password}

## Environment OAuth
export OAUTH_CLIENTID={OAuth2 client}
export OAUTH_SECRET={OAuth2 secret}

## Environment OpenAPI
export INTERPARK_KEY={Interpark OpenAPI Key}
저장한 뒤 source .profile 입력
