# instagram-direct-spam-bot
This bot send a message to a list of users with Instagram direct


# How to use

## Installation and config
- Install:
  - [Firefox browser](https://www.mozilla.org/it/firefox/new/)
  - [Geckodriver](https://github.com/mozilla/geckodriver/releases)
  - [Python3](https://www.python.org/downloads/release/python-385/)
  - [Node.js](https://nodejs.org/)

- Install modules:

  ```
  pip3 install selenium
  npm install instatouch -g
  ```
- Config gen_raw_user.js variables:
  - [sessionid](https://drive.google.com/file/d/1ECEDySAY9RLUBGRlQnBvU-gP6vft-MWt/view?usp=sharing)
- Config main.py variables
## Start bot
- Run ```py parse_user_json.py``` to generate users json list
- Run ```py main.py``` to start bot, after login Firefox will ask you to activate notifications, click yes