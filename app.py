from flask import Flask, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
import os

from football_api.data_client import FootballDataClient
from football_api.data_utils import parse_matches
from config.settings import api_key

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    internal_user = os.getenv("INTERNAL_USER")
    internal_pw = os.getenv("INTERNAL_PW")

    if username == internal_user and password == internal_pw:
        return redirect(url_for("manage_bot"))
    else:
        return render_template("login.html", login_failed=True)


@app.route("/manage_bot")
def manage_bot():
    return render_template("managebot.html")


@app.route("/get_next_fixture", methods=["GET"])
def get_next_fixture():
    season = request.args.get("season")
    team_id = request.args.get("team_id")
    league_id = request.args.get("league_id")

    # Replace this with your code to fetch the next fixture based on the input data
    client = FootballDataClient(api_key)
    next_fixture_data = client.get_next_fixture(
        int(team_id), int(season), int(league_id)
    )
    next_fixture = parse_matches(next_fixture_data)

    return jsonify(next_fixture)


@app.route("/send_to_lemmy", methods=["POST"])
def send_to_lemmy():
    # Replace this with your code to send the next fixture to Lemmy
    return "Next fixture sent to Lemmy!"


if __name__ == "__main__":
    app.run()
