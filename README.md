# Api Yamdb extended version
![workflow badge for yamdb project](https://github.com/SemenovaLiza/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.7-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-3.2.16-green?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.12.4-red?logo=django&logoColor=white)
![SimpleJWT](https://img.shields.io/badge/SimpleJWT-4.7.2-orange?logo=jsonwebtokens&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-20.10.23-blue?logo=docker&logoColor=white)
![Pytest](https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square&logo=pytest)![License](https://img.shields.io/badge/license-MIT-purple.svg?style=flat-square) ![Status](https://img.shields.io/badge/status-finished-green?style=flat-square)
### *Description*
This project is an extended version of the [Api Yamdb](https://github.com/SemenovaLiza/api_yamdb) project, which allows you to manage the project on a remote server.
### *Technologies*
- Python 3.7
- Django 3.2.16
- django rest framework 3.12.4
- django rest framework-simplejwt 4.7.2
- PostgreSQL
- Docker 20.10.23
###### *The rest of the technologies can be found in the requirements.txt file*
### You will need to create these secret variables in GitHub to work with this project:

- secrets.DOCKER_USERNAME - *Docker Hub login*
- secrets.DOCKER_PASSWORD - *Docker Hub password*
- secrets.HOST - *Remote server public IP*
- secrets.USER - *Remote server login*
- secrets.SSH_KEY - *Private key from the local machine*
- secrets.PASSPHRASE - *The passphrase used when creating the ssh key*
### Secrets variables for remote server:
- secrets.DB_ENGINE - *The database using in project*
- secrets.DB_NAME - *The database's name*
- secrets.POSTGRES_USER - *The username of database user*
- secrets.POSTGRES_PASSWORD - *The password for the user*
- secrets.DB_HOST - *Remote server public IP*
- secrets.DB_PORT - *The port for connecting to the database*
### Telegram variables:
- secrets.TELEGRAM_TO - *Telegram accont id*
- secrets.TELEGRAM_TOKEN - *Telegram bot token*
### *How to launch a project*
Using terminal change the current working directory to the location where you want the cloned directory.

Clone the repository to your local machine:
```
git@github.com:SemenovaLiza/yamdb_final.git
```
Go to the remote server and install docker:
```
ssh login@remote.server.pub.ip
sudo apt install docker.io
```
Install Docker Desktop and run it, install the compose plugin on your remote server:
```
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
```
Apply executable permissions to the binary:
```
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
```
or, if you chose to install compose for all users:
```
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```
Verify that docker-compose was installed correctly:
```
docker compose version
```
Copy *docker-compose.yaml* and *nginx/nginx.conf* from the *infra* directory to the remote server:
```
scp docker-compose.yml <login>@<host>:/home/<login>/docker-compose.yml
scp nginx.conf <login>@<host>:/home/login>/nginx.conf
```
After executing these commands, make a git push and perform migrations on the remote server and collect static:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
```
This project is available at:
http://lizasprojects.ddns.net/api/v1/titles/

### *Author*
Semenova Elizaveta
