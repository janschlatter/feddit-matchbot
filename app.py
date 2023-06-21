from flask import Flask, render_template, request, redirect, url_for, jsonify
from db.db import get_connection, release_connection
from dotenv import load_dotenv
import os
import requests

from football_api.data_client import FootballDataClient
from football_api.data_utils import parse_matches, parse_teams
from config.settings import api_key
from db.post_scheduler import schedule_post

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
    num_fixtures = request.args.get("num_fixtures")

    client = FootballDataClient(api_key)
    next_fixtures_data = client.get_next_fixtures(
        int(team_id),
        int(season),
        int(league_id),
        int(num_fixtures),  # Pass the num_fixtures parameter
    )
    next_fixtures = parse_matches(next_fixtures_data)

    return jsonify(next_fixtures)


@app.route("/send_to_lemmy", methods=["POST"])
def send_to_lemmy():
    # Replace this with your code to send the next fixture to Lemmy
    return "Next fixture sent to Lemmy!"


@app.route("/schedule_post", methods=["POST"])
def handle_schedule_post():
    season = request.json.get("season")
    team_id = request.json.get("teamId")
    league_id = request.json.get("leagueId")

    result = schedule_post(season, team_id, league_id)
    return result


@app.route("/scheduledPosts")
def scheduled_posts():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM scheduledPosts")
        scheduled_posts = cursor.fetchall()
        print("Retrieved scheduled posts:", scheduled_posts)  # Debug print
        return render_template("scheduledPosts.html", scheduled_posts=scheduled_posts)
    except Exception as e:
        print("Error retrieving scheduled posts:", e)  # Debug print
    finally:
        release_connection(conn)


@app.route("/delete_post/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM scheduledPosts WHERE id = %s", (post_id,))
        conn.commit()
        return "Post deleted!"
    except Exception as e:
        conn.rollback()
        return f"Error deleting post: {e}"
    finally:
        release_connection(conn)


@app.route("/teams")
def get_teams():
    season = request.args.get("season")
    league_id = request.args.get("leagueId")

    # Create an instance of the FootballDataClient
    client = FootballDataClient(api_key)

    # Make the API call to fetch the list of teams
    teams_data = client.get_teams(league_id, season)

    # Parse the teams data (you may need to create a new function for this)
    teams = parse_teams(teams_data)

    return jsonify(teams)


@app.route("/settings")
def settings():
    return render_template("settings.html")


if __name__ == "__main__":
    app.run()
