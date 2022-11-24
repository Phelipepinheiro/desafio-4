from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'localhost' # 127.0.0.1
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)