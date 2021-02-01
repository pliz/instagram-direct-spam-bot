# instagram-direct-spam-bot
This bot send a message to a list of users with Instagram direct


# How to use

## Installation and config
- Install:
  - [Git](https://git-scm.com/)
  - [Firefox browser](https://www.mozilla.org/it/firefox/new/)
  - [Geckodriver](https://github.com/mozilla/geckodriver/releases)
  - [Python3](https://www.python.org/downloads/release/python-385/)
  - [Node.js](https://nodejs.org/)

- Install modules:

  ```
  python3 -m pip install selenium
  npm install instatouch -g
  ```
- Clone repository:

  ```git clone https://github.com/valenzanico/instagram-direct-spam-bot```
- Create a config.json file

  example:
  ```
  [
    {
        "name": "config 1",
        "username": "username",
        "password": "password",
        "count": 10,
        "start_from":1,
        "users_page" : "page from which you want to get followers",
        "message": "message you want to send"
    },
    {
        "name": "config 2",
        "username": "username",
        "password": "password",
        "count": 20,
        "start_from":11,
        "users_page" : "page from which you want to get followers",
        "message": "message you want to send"
    }
  ]
  ```
## Start bot
- Run ```python3 main.py```