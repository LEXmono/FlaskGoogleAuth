from flask import Flask, redirect, url_for, session, jsonify, current_app, render_template
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import logout_user
from flask_google_auth import app
from flask_google_auth.config import config


blueprint = make_google_blueprint(
    client_id=config.GOOGLE_CLIENT_ID,
    client_secret=config.GOOGLE_CLIENT_SECRET,
    scope=['https://www.googleapis.com/auth/userinfo.email', 'openid'],
    offline=True
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route('/')
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get(config.google_userinfo_url)
    if not resp.ok:
        print('ERROR: ' + resp.text)
    return jsonify(resp.json())


@app.route('/login')
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    token = current_app.blueprints["google"].token["access_token"]
    resp = google.post(
        "https://oauth2.googleapis.com/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    if not resp.ok:
        print(resp.text)
    del blueprint.token  # Delete OAuth token
    return "<h1>Logged Out</h1>"
