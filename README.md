# Warpin Test Chat APP


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Warpin Test Chat App is a simple real time  chat app.
Powered by:
- python3
- Flask 1.1.1
- Flask-SocketIo 4.2.1
- SQLite
- Flask-SQLAlchemy 2.1


# Get The Source Codes
```
$ git clone <>
```

# How to run locally with docker
### Install Docker
for docker installation please refer to this link: https://docs.docker.com/install/
after docker successfully installed. run comman below
  ```sh
  $ cd warpin-chat
  $ docker-compose up --build
```
-------------------
# Run locally without docker
### Install Virtualenv
virtualenv: https://virtualenv.pypa.io/en/latest/installation/
virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/install.html
after virtualenv successfully install, then you need to create virtualenv python3 and activate the virtualenv.
### Runserver
```sh
$ (<venv>) cd warpin-chat 
$ (<venv>) pip install -r requirements.txt
$ (<venv>) python manage.py createdb
$ (<venv>) python manage.py runserver
```
--------------------
# Run unit test
```sh
$ (<venv>) python manage.py test
```
-------------------------------------
# TEST THE API
#### API REST FOR SENDING MESSAGE
```
 - URL: http://127.0.0.1:5000/messages
 - METHOD: Post
 - REQUEST-BODY: {"message": "message content"}
 ```

#### REST API TO RETRIEVE ALL MESSAGES HISTORY
```
 - URL: http://127.0.0.1:5000/messages
 - METHOD: Get
 - RESPONSE EXAMPLE: 
    {
        "messages":
            [
                {
                    "created_at": <timestamp message is sent/created>,
                    "message": <message_content>
                },
            ]
    }
```
#### API FOR SUBSCRIBE TO REAL TIME MESSAGE EVENT (SOcketIO Connection)
```
- URL: http://127.0.0.1:5000<port>/messages
- PATH: /socket.io
- TRANSPORT: polling
- LISTENER EVENT: subscribe
```

