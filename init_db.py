import sqlite3

def init_test_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ids (
            unique_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            branch TEXT NOT NULL,
            batch TEXT NOT NULL,
            college TEXT NOT NULL,
            image_path TEXT NOT NULL
        )
    ''')

    # Insert sample data
    test_data = [
        ('0126CD221111', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221124', 'Shubham Singh', 'B.Tech', 'CSE-DS', '2022-2024',' OCT', '/static/images/shubham.png'),
        ('0126CD221100', 'Rahul Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/rahul.png'),
        ('0126CD221083', 'Nishant Kushwah', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/nishant.png'),
        ('0126CD221095', 'Prince Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/prince.png'),
        ('0126CD221096', 'Prince Thakre', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/princt.png'),
        ('0126CD221076', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221077', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221078', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221079', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221080', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221081', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221082', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221084', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221085', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221086', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221087', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221088', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221089', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221090', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221091', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221092', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221093', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221094', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221097', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221098', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221101', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221102', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221103', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221104', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221105', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221106', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221107', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221108', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221109', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221110', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221112', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg')
  
    ]

    cursor.executemany(
        'INSERT OR IGNORE INTO ids (unique_id, name, course, branch, batch, college, image_path) VALUES (?, ?, ?, ?, ?, ?, ?)',
        test_data
    )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_test_db()
