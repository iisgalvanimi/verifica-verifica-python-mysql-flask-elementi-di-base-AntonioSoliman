import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase" 
)

mycursor = mydb.cursor()


smartphones_data = [
    ("Apple", "iPhone 14 Pro Max", "iOS", "6.7 pollici", "4323mAh"),
    ("Samsung", "Galaxy S23 Ultra", "Android", "6.8 pollici", "5000mAh"),
    ("Google", "Pixel 7 Pro", "Android", "6.7 pollici", "5000mAh"),
    ("Xiaomi", "13 Pro", "Android", "6.7 pollici", "4820mAh"),
    ("OnePlus", "11", "Android", "6.7 pollici", "5000mAh"),
    ("Huawei", "P60 Pro", "HarmonyOS", "6.67 pollici", "4800mAh"),
    ("OPPO", "Find X6 Pro", "Android", "6.82 pollici", "5000mAh"),
    ("Vivo", "X90 Pro+", "Android", "6.78 pollici", "4700mAh"),
    ("Realme", "GT3 Pro", "Android", "6.74 pollici", "5000mAh"),
    ("Nothing", "Phone (2)", "Android", "6.7 pollici", "4700mAh")
]


sql = "INSERT INTO Smartphones (Marca, Modello, Sistema_operativo, Dimensioni_schermo, Capacita_batteria) VALUES (%s, %s, %s, %s, %s)"


mycursor.executemany(sql, smartphones_data)


mydb.commit()

print("Dati inseriti con successo.")
