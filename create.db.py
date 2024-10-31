import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor() 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS COURSE(
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)
    con.commit()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
            roll INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            admission TEXT,
            course TEXT,
            state TEXT,
            city TEXT,
            pin TEXT,
            address TEXT
        )
    """)
    con.commit()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS result(
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks_ob TEXT,
            full_marks TEXT,
            per TEXT
            
        )
    """)
    con.commit()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            email TEXT
        )
    """)
    con.commit()
    
    
    
    
    con.close()
create_db()