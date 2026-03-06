import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    conn = psycopg2.connect(
        dbname="property_db",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Create Table
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS profiles (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        email VARCHAR,
        phone_number VARCHAR,
        bio TEXT,
        profile_picture_url VARCHAR
    );
    """
    )

    # Insert default profile if not exists
    cursor.execute("SELECT COUNT(*) FROM profiles WHERE id = 1;")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute(
            """
        INSERT INTO profiles (id, first_name, last_name, email, phone_number, bio, profile_picture_url)
        VALUES (1, 'Alex', 'Morgan', 'alex.morgan@estateflow.com', '+1 (555) 000-0000', 'Senior property manager with 10+ years of experience in luxury real estate.', 'https://lh3.googleusercontent.com/aida-public/AB6AXuDrz2EtVkE4e9LH9AIgQr4JX4vA8UVZAZI_tJG7kwMQnL4d4sLzJxafdc48wETajzsDQexZkK579DR21mqbfo01BWuJIzAui9atyHSuU2Vjc3q7EZtY1TIUl6vBFZo2KXIJzm9tiZDBTQQfnazd6eEYyJHpawrZ-hRaqezNiFa--cmVcKIRxgBuclMnEEQwID-V9LY3k7afPrDgSMNHgTZGfFE5Mn1UnUSqOVim_kwlmNOW7ogfCRsAkHAU0r95smPzujR6VrkttAEG');
        """
        )
        print("Default profile inserted.")

    cursor.close()
    conn.close()
    print("Database table 'profiles' ready.")
except Exception as e:
    print(f"Error updating database: {e}")
