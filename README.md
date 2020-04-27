# IU Software Project (Spring semester 2020)
Staff-assessment service for Innopolis University students  
Technologies used:  
* **Backend**: Django REST
* **Frontend**: Vue.js & Vuetify
* **Databse**: MongoDB
* **Server**: nginx

## How to Launch
### Development version
    $ sudo docker-compose -f docker-compose.dev.yaml up -d --build
### Production version
    $ sudo docker-compose -f docker-compose.prod.yaml up -d --build 

## How to use
After launch just go to **http://127.0.0.1:8001/** for dev version
or to **http://127.0.0.1:8080/** for prod version.  
