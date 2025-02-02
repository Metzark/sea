from sys import argv
from functions.create_pg_conn import create_pg_conn
from functions.exec_stmt import exec_stmt

#region up

create_schema_sea_stmt = "CREATE SCHEMA IF NOT EXISTS sea;"

create_table_sessions_stmt = """
CREATE TABLE IF NOT EXISTS sea.sessions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    token TEXT
);"""

create_table_entity_types_stmt = """
CREATE TABLE IF NOT EXISTS sea.entity_types (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT
);"""

create_table_entities_stmt = """
CREATE TABLE IF NOT EXISTS sea.entities (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    type_id INT REFERENCES sea.entity_types(id),
    name TEXT,
    color TEXT
);"""

#endregion up

#region down

drop_schema_sea_stmt = "DROP SCHEMA IF EXISTS sea;"

drop_table_sessions_stmt = "DROP TABLE IF EXISTS sea.sessions;"

drop_table_entity_types_stmt = "DROP TABLE IF EXISTS sea.entity_types;"

drop_table_entities_stmt = "DROP TABLE IF EXISTS sea.entities;"

#endregion down

try:
    # Get action, up == create tables, down == drop tables
    action = argv[1] if len(argv) > 1 else "up"

     # Set up db connection
    conn, cur = create_pg_conn()

    # Execute all 'up' statements
    if action == "up":
        exec_stmt(cur, conn, create_schema_sea_stmt)
        exec_stmt(cur, conn, create_table_sessions_stmt)
        exec_stmt(cur, conn, create_table_entity_types_stmt)
        exec_stmt(cur, conn, create_table_entities_stmt)

    # Execute all 'down' statements
    if action == "down":
        exec_stmt(cur, conn, drop_table_entities_stmt)
        exec_stmt(cur, conn, drop_table_entity_types_stmt)
        exec_stmt(cur, conn, drop_table_sessions_stmt)
        exec_stmt(cur, conn, drop_schema_sea_stmt)

    # Close db connection
    cur.close()
    conn.close()

    print("Created all tables")

except Exception as e:
    print(f"{e}")