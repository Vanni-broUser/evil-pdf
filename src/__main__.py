from flask import Flask, request, send_file
from flask_cors import CORS

from database_api import set_database

from .constants import DATABASE_URL


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
  client_ip = request.remote_addr
  user_agent = request.headers.get('User-Agent')
  referer = request.headers.get('Referer', 'No referrer')
  accept_language = request.headers.get('Accept-Language', 'No language specified')

  print(f"Request received from IP: {client_ip}")
  print(f"User-Agent: {user_agent}")
  print(f"Referer: {referer}")
  print(f"Accept-Language: {accept_language}")

  return send_file('../static/LogisticDashboardReport.pdf', mimetype='application/pdf')


# Main

if __name__ == '__main__':
  set_database(DATABASE_URL)
  app.run(host='0.0.0.0', port=8080)
