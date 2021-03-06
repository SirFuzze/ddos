#!/usr/bin/env python3

#MIT License
#
#Copyright (c) 2021 Sloobot
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import json
import random

mails = (
    "mail.ru",
    "inbox.ru",
    "list.ru",
    "bk.ru",
    "ya.ru",
    "yandex.com",
    "yandex.ua",
    "yandex.ru",
    "gmail.com"
)


# Get random service
def random_service(list):
    return random.choice(list)

# Create random name
def random_name():
    with open("tools/SMS/names.json", 'r') as names:
        names = json.load(names)["names"]
    return random.choice(names)

# Create random suffix for email
# %random_name%SUFFIX@%random_email%
def random_suffix(int_range = 4):
    numbers = []
    for _ in range(int_range):
        numbers.append(str(random.randint(1, 9)))
    return "".join(numbers)


# Create random email by name, suffix, mail
# Example: Jefferson3715@gmail.com
def random_email():
    return random_name() + random_suffix() + "@" + random.choice(mails)

# Create random password
# %random_name%%random_suffix%
def random_password():
    return random_name() + random_suffix(int_range = 10)

# Get random user agent
def random_useragent():
    with open("tools/SMS/user_agents.json", 'r') as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)
