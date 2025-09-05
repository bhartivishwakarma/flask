from flask import Flask, request, jsonify,render_template   
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",          # change if needed
    password="Demo@100",  # change
    database="shopdb"     # make sure this DB exists
)
@app.route("/")
def home():
    return render_template("new.html")
@app.route("/products", methods=["GET"])
def get_products():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    return jsonify(products)

@app.route("/add", methods=["POST"])
def add_data():
    try:
        data = request.get_json()
        print("📩 Received:", data)

        name = data.get("name")
        price = int(data.get("price", 0))
        description = data.get("description")
        cursor = db.cursor()
        sql = "INSERT INTO products (name, price,description) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, price, description,))
        db.commit()
        new_id = cursor.lastrowid
        cursor.close()

        print("✅ Inserted ID:", new_id)
        return jsonify({"id": new_id, "name": name, "price": price,"description":description}), 201
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)