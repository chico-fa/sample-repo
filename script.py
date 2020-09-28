import sys

import requests

print(sys.version)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://cnn.com")
print(r.status_code)

name = input("Your name? ")
print("Hello,", name)


# print(greet('World'))
# print(greet('Carlo'))
# print(sys.executable)