import sqlite3
import os

def create_sample_database(db_path):
    """Create sample database with related tables"""
    # Ensure directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to database (creates it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        signup_date TEXT
    )
    ''')
    
    # Create orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT,
        total_amount REAL,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    ''')
    
    # Insert sample data
    cursor.executemany(
        "INSERT INTO customers VALUES (?, ?, ?, ?)",
        [
            (1, "John Smith", "john@example.com", "2023-01-15"),
            (2, "Jane Doe", "jane@example.com", "2023-02-20"),
            (3, "Bob Johnson", "bob@example.com", "2023-03-10")
        ]
    )
    
    cursor.executemany(
        "INSERT INTO orders VALUES (?, ?, ?, ?)",
        [
            (101, 1, "2023-03-15", 150.75),
            (102, 1, "2023-04-10", 89.99),
            (103, 2, "2023-03-20", 45.50),
            (104, 3, "2023-05-05", 210.25)
        ]
    )
    
    conn.commit()
    conn.close()
    
    print(f"Sample database created at {db_path}")

if __name__ == "__main__":
    create_sample_database("data/sample.db")
