def format_match_post(match):
    title = f"{match['home_team']} vs {match['away_team']} - Match Thread"
    content = f"""
    **{match['home_team']} vs {match['away_team']}**

    Date: {match['date']}

    Status: {match['status']['long']}

    Score: {match['score']['home']} - {match['score']['away']}
    """
    return title, content
