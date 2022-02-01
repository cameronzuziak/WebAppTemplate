# WebAppTemplate

Author: Cameron Zuziak </br>
Date: 1/31/2022

<h5>Description:</h5>
Dockerized flask app served by gunicorn and nginx, for Ubuntu 20.04
This repo has 2 docker containers, one is a flask app served with gunicorn, 
the other is an nginx container that serves as a proxy. 
The flask will also install mysqlclient. 
If you do not wish to use MySQL, you can edit the flaskapp/Dockerfile to suit your needs.


<h5>Prereqs: </h5>
Instructions below assume you have set up an Ubuntu 20.04 server</br>
1. Update your instance: </br>
    > sudo apt-get update

2. Install docker compose:</br>
    > sudo apt-get install docker-compose

3. Clone this repopsitory:</br>
    >git clone https://github.com/cameronzuziak/WebAppTemplate.git

4. CD into the cloned directory and open the docker-compose.yml file in either vim or nano: </br>
    >cd WebAppTemplate/
    >nano docker-compose.yml

5. Change the enviroment variable SERVER_NAME from 0.0.0.0 to the public IPv4 of your instance. then save and exit.

6. Change back to the projects main directory:</br>
    >cd ../

7. Build your containers and run them, a few ways to do this.
    >sudo docker-compose build</br>
    >sudo docker-compose up</br>

  or combine the 2 commands with the build arg: </br>
    >sudo docker-compose up --build

  or if you want to build and run in the background:</br>
    >sudo docker-compose up --build -d
    
