#!/usr/bin/env python3

""" Check for new tweets and post them to Slack """

import os
import time
import subprocess
import requests


BASE_URL = "https://hooks.slack.com/services/"
HOOK_IDS = []


def get_fortune():
    """ Run UNIX fortune and grab the output - get a long fortune """
    out = subprocess.check_output(['/usr/games/fortune', '-l'])
    return out.decode('ascii')


def send_alert(text):
    """ Send a Message to Slack """
    payload = {'username': "Fortune of the Day",
               "text": "```%s```" % (text),
               "icon_emoji": ":fortune_cookie:",
               "link_names": 1}
    for hook in HOOK_IDS:
        response = requests.post(BASE_URL + hook, json=payload)
        print(response.text)

    # Rate limit in case of script failure
    time.sleep(1)


def get_hooks():
    """ Get a list of hook ids from the environment """
    hooks = []
    for key in os.environ.keys():
        if key.startswith('HOOK_ID_'):
            hooks.append(os.environ[key])
    return hooks


def main():
    """ Main Method """
    HOOK_IDS.extend(get_hooks())
    fortune = get_fortune()
    send_alert(fortune)


if __name__ == "__main__":
    main()
