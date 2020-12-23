# Blog_Project
##### ver2.0
 Add about menu, snow effect


### 기술 스택
#### §Server-side
   ##### python3
   ##### MongoDB
   ##### jinja2
   ##### AWS
   ##### EC2 t2 micro
   
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
