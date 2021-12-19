import json
import datetime
import requests
import hashlib
import os

import urllib.parse

ROOT_URL = "http://192.168.0.13:8000"

DRIVER_URL = urllib.parse.urljoin(ROOT_URL, "drivers")
DRIVER_LOGIN_URL = DRIVER_URL + "/login/"
SETTINGS_PATH = os.path.join(os.getcwd(), "settings.json")

DEFAULT_SETTINGS = {
    "token": "0"
}

def load_settings() -> dict:
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, "r") as fp:
            return json.loads(fp.read())
    return DEFAULT_SETTINGS

def save_settings(settings: dict) -> bool:
    with open(SETTINGS_PATH, "w") as fp:
        fp.write(json.dumps(settings))

def generate_hash(data: dict, token: str, imei: str) -> str:
    """generate unique hash from request parameters, token auth and imei number

    Args:
        data (dict): request parameters
        token (str): unique token id stored in settings.json when logged in
        imei (str): unique mobile equipment identity from driver phone

    Returns:
        str: salted sha-1 hash used to authenticate
    """
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    salt = hashlib.sha1()
    salt.update(encoded_data)
    salt.update(token.encode("utf-8"))
    salt.update(imei.encode("utf-8"))
    return salt.hexdigest()

def driver_request(url: str, data: dict, token: str, imei: str, headers: dict, method: str) -> dict:
    """sends a request from server and returns a json object

    Args:
        url (str): [description]
        data (dict): [description]
        token (str): [description]
        imei: (str): [description]
        headers (dict): [description]
        method (str): [description]
    """
    # get imei number
    salted_hash = generate_hash(
        data, token, imei
    )
    data["h"] = salted_hash
    headers["Authorization"] = token
    if method == "POST":
        requests.post(url, data)
    else:
        pass
    

def save_settings(settings: dict):
    with open("settings.json", "w") as fp:
        fp.write(json.dumps(settings))