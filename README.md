# Web Page Update Checker

This Python script allows you to monitor a web page for updates and receive notifications on Telegram when changes are detected.


## Introduction

The Web Page Update Checker is a Python script that allows you to automate the process of monitoring a web page for updates. Instead of checking for updates manually, this script uses hashing to compare the current version of a web page with its previous version. If changes are detected, the script sends notifications to your Telegram account, making it easier to stay up-to-date with changes to the web page.

## Problem
I created this script to address a specific need I had: to monitor a school website where I wanted my son to attend. In order to be considered for admission, we needed to add his name to the waiting list on the website. However, there was no clear indication of when this list would become available.

With this script, I was able to automate the process of checking the website for updates and receive notifications when the waiting list became available.


## Requirements

To run this script, you need to have Python 3 installed on your system. You also need the following Python libraries:

- requests
- hashlib

You can install these libraries using pip:

```
pip install requests
pip install hashlib
```

## Libraries used

This script uses the following libraries:

- [requests](https://pypi.org/project/requests/): A library for making HTTP requests in Python.
- [hashlib](https://docs.python.org/3/library/hashlib.html): A library for computing hash digests of data in Python.

## Usage

1. Clone or download this repository to your local machine.
2. Create the file `credentials.json` with the following parameters:
    ```
    {
        "url_to_check": "https://yourwebsite.com",
        "token": "your_telegram_token",
        "chat_id": "you_telegram_chat_id"
    }
    ```
    
    See [this article](https://medium.com/codex/using-python-to-send-telegram-messages-in-3-simple-steps-419a8b5e5e2) for more information
3. Open a terminal or command prompt and navigate to the directory containing the `web_page_update_checker.py` file.
4. Run the script by entering the following command:

```
python web_page_update_checker.py
```

The script will start monitoring the web page for updates and will send notifications to your Telegram account when changes are detected.
