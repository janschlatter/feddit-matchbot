from db.db import get_connection, release_connection


def is_fixture_scheduled(season, team_id, league_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT COUNT(*) FROM scheduledPosts WHERE season = %s AND team_id = %s AND league_id = %s",
            (season, team_id, league_id),
        )
        count = cursor.fetchone()[0]
        return count > 0
    finally:
        release_connection(conn)


def schedule_post(season, team_id, league_id):
    if is_fixture_scheduled(season, team_id, league_id):
        return "Fixture already scheduled!"

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO scheduledPosts (season, team_id, league_id) VALUES (%s, %s, %s)",
            (season, team_id, league_id),
        )
        conn.commit()
        return "Post scheduled!"
    except Exception as e:
        conn.rollback()
        return f"Error scheduling post: {e}"
    finally:
        release_connection(conn)
