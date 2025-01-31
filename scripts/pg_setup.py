from functions.create_pg_conn import create_pg_conn
from functions.execute_stmt import execute_stmt

try:
     # Set up db connection
    conn, cur = create_pg_conn()

    # Example
    # execute_stmt(cur, conn, "SELECT 1;")

    # Close db connection
    cur.close()
    conn.close()

    print("Created all tables")

except Exception as e:
    print(f"{e}")