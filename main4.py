from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

db_config = {
    'host': 'localhost',      
    'user': 'root',     
    'password': '', 
    'database': 'mydatabase'  
}


@app.route('/dati', methods=['GET'])
def get_data(filtro=None, valore=None, valore_min=None, valore_max=None):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM Smartphones"
        params = ()

   
        
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile connettersi al database"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


@app.route('/dati/crea', methods=['POST'])
def create_smartphone():
    data = request.get_json()

    marca = data.get('Marca')
    modello = data.get('Modello')
    sistema_operativo = data.get('Sistema_operativo')
    dimensioni_schermo = data.get('Dimensioni_schermo')
    capacita_batteria = data.get('Capacita_batteria')

    if not marca or not modello or not sistema_operativo or not dimensioni_schermo or not capacita_batteria:
        return jsonify({"errore": "Tutti i campi sono obbligatori"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "INSERT INTO Smartphones (Marca, Modello, Sistema_operativo, Dimensioni_schermo, Capacita_batteria) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (marca, modello, sistema_operativo, dimensioni_schermo, capacita_batteria))
        conn.commit()

        return jsonify({"successo": "Nuovo smartphone creato", "id": cursor.lastrowid}), 201
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile inserire lo smartphone nel database"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


@app.route('/dati/elimina/<int:id>', methods=['DELETE'])
def delete_smartphone(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "DELETE FROM Smartphones WHERE Id = %s"
        cursor.execute(query, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"errore": "Smartphone non trovato"}), 404

        return jsonify({"successo": "Smartphone eliminato"}), 200
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile eliminare lo smartphone dal database"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run()
