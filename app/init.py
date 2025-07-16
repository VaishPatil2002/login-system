from flask import Flask

app = Flask(__name__)
app.secret_key = 'secret123'  # Use environment variable in real-world apps

from app import routes
