import sqlite3

DB_NAME = "test.db"

def init_db():
    """Initialize a simple SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        region TEXT,
        date TEXT,
        product TEXT,
        sales REAL
    );
    """)

    # Insert sample data if empty
    cursor.execute("SELECT COUNT(*) FROM sales;")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ("North", "2024-01-10", "Electronics", 500.0),
            ("South", "2024-02-11", "Apparel", 300.0),
            ("East", "2024-03-12", "Electronics", 700.0),
            ("West", "2024-04-10", "Electronics", 200.0),
        ]
        cursor.executemany("INSERT INTO sales (region, date, product, sales) VALUES (?, ?, ?, ?);", sample_data)
        conn.commit()

    conn.close()

def execute_sql(sql: str):
    """Run SQL query and return results."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        return {"columns": columns, "rows": rows}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()
