from db.db import get_connection, release_connection


def schedule_post(season, team_id, league_id):
    # Save the data into the "scheduledPosts" table using the database connection
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
