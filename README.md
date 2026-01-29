Flask MySQL Products API (Practice Project)

This is a beginner practice project using Flask, MySQL, and REST API concepts.
It allows you to view products and add new products to a MySQL database.

Features

Flask backend
MySQL database connection
REST API using JSON
CORS enabled
Fetch all products
Add new product
HTML template rendering

#Technologies Used
Python
Flask
Flask-CORS
MySQL
mysql-connector-python
HTML

📂 Project Structure
project/
│
├── app.py
├── templates/
│   └── new.html
└── README.md

🗄 Database Setup

Create database and table in MySQL:

CREATE DATABASE shopdb;

USE shopdb;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    description TEXT
);

▶️ How to Run the Project

Install required packages:

pip install flask flask-cors mysql-connector-python


Update MySQL credentials in app.py:

user="root"
password=""
database=""


Run the application:
python app.py


Open in browser:
http://localhost:5000/

🔗 API Endpoints
1️⃣ Get All Products

GET /products

Response:

[
  {
    "id": 1,
    "name": "Laptop",
    "price": 50000,
    "description": "Gaming laptop"
  }
]

2️⃣ Add New Product

POST /add

Request Body (JSON):

{
  "name": "Mobile",
  "price": 15000,
  "description": "Android phone"
}


Response:

{
  "id": 2,
  "name": "Mobile",
  "price": 15000,
  "description": "Android phone"
}

#Purpose
This project is created for learning and practice:
Flask basics
API creation
MySQL integration
JSON handling
