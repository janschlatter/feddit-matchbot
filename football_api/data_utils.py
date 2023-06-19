def parse_matches(matches_data):
    matches = []
    for match_data in matches_data["response"]:
        match = {
            "home_team": match_data["teams"]["home"]["name"],
            "away_team": match_data["teams"]["away"]["name"],
            "date": match_data["fixture"]["date"],
            "status": match_data["fixture"]["status"],
            "score": match_data["score"]["fulltime"],
        }
        matches.append(match)
    return matches


def parse_teams(teams_data):
    teams = []
    for team_data in teams_data["response"]:
        team = {
            "id": team_data["team"]["id"],
            "name": team_data["team"]["name"],
        }
        teams.append(team)
    return teams
