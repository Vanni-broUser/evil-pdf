from flask import Flask
from flask_cors import CORS

from database_api import set_database

from .constants import DATABASE_URL


app = Flask(__name__, static_folder='../static')
CORS(app)


@app.route('/', methods=['GET'])
def index():
  return 'Hello World', 200


# Main

if __name__ == '__main__':
  set_database(DATABASE_URL)
  app.run(host='0.0.0.0', port=8080)
