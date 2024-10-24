import mysql.connector as mysql

class MySQLConn:
    conn = None
    cursor = None
    def __init__(self, host, user, pswd, db):
        self.conn = mysql.connect(host=host, user=user, password=pswd, db=db)
        self.cursor = self.conn.cursor()

    def insertApp(self, name, dept, sem, exam_roll, email, whatsapp, team, skill, about):
        self.cursor.execute(
            "INSERT INTO applications (time_add, fullName, dept, sem, examroll, email, whatsapp, team, skill, about) "
            "VALUES (UNIX_TIMESTAMP(), %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, dept, sem, exam_roll, email, whatsapp, team, skill, about)
        )

        self.conn.commit()
    
    def selectAll(self):
        self.cursor.execute("SELECT * FROM applications;")
        
        rows = self.cursor.fetchall()
        
        columns = [column[0] for column in self.cursor.description]
        
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))
        
        return result
    
    def ping(self):
        try:
            self.conn.ping(reconnect=True, attempts=3, delay=5) 
            print("Pinged MySQL instance")
        except mysql.Error as e:
            print(f"Error pinging the server: {e}")
