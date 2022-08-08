import base64
import hashlib
import os
import re
import json
import requests
import tweepy
import redis
from requests.auth import AuthBase, HTTPBasicAuth
from requests_oauthlib import OAuth2Session, TokenUpdated
from flask import Flask, request, redirect, session, url_for, render_template


r = redis.from_url(os.environ["REDIS_URL_DOGS"])

app = Flask(__name__)
app.secret_key = os.urandom(50)


client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
auth_url = "https://twitter.com/i/oauth2/authorize"
token_url = "https://api.twitter.com/2/oauth2/token"
redirect_uri = os.environ.get("REDIRECT_URI")

# Set the scopes
scopes = ["tweet.read", "users.read", "tweet.write", "offline.access"]

# Create a code verifier
code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

# Create a code challenge
code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
code_challenge = code_challenge.replace("=", "")



def make_token():
    return OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)


def parse_dog_fact():
    url = "http://dog-api.kinduff.com/api/facts"
    dog_fact = requests.request("GET", url).json()
    return dog_fact["facts"][0]



def post_tweet(payload, token):
    print("Tweeting!")
    return requests.request(
        "POST",
        "https://api.twitter.com/2/tweets",
        json=payload,
        headers={
            "Authorization": "Bearer {}".format(token["access_token"]),
            "Content-Type": "application/json",
        },
    )


@app.route("/")
def demo():
    global twitter
    twitter = make_token()
    authorization_url, state = twitter.authorization_url(
        auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )
    session["oauth_state"] = state
    return redirect(authorization_url)


@app.route("/oauth/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    token = twitter.fetch_token(
        token_url=token_url,
        client_secret=client_secret,
        code_verifier=code_verifier,
        code=code,
    )
    st_token = '"{}"'.format(token)
    j_token = json.loads(st_token)
    r.set("token", j_token)
    doggie_fact = parse_dog_fact()
    payload = {"text": "{}".format(doggie_fact)}
    response = post_tweet(payload, token).json()
    return response


if __name__ == "__main__":
    app.run()
