from main import create_app
from main import mongo

import os
import  json
import requests
from oauthlib.oauth2 import WebApplicationClient
from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

app = create_app()
app.app_context().push()

if __name__ == '__main__':
    app.run(debug = True, port = os.getenv('PORT'))