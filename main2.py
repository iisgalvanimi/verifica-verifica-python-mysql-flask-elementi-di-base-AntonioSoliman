import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"  
)

mycursor = mydb.cursor()


mycursor.execute("""
CREATE TABLE IF NOT EXISTS Smartphones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Marca VARCHAR(255),
  Modello VARCHAR(255),
  Sistema_operativo VARCHAR(255),
  Dimensioni_schermo VARCHAR(50),
  Capacita_batteria VARCHAR(50)
)
""")
