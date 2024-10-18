from flask import Flask, request, send_file
from flask_cors import CORS

from .database.schema import Request
from database_api import set_database
from database_api.operations import create

from .constants import DATABASE_URL


app = Flask(__name__)
CORS(app)


@app.route('/<number>/logistic-dashboard-report.pdf', methods=['GET'])
def index(number):
  create(Request, {
    'number': int(number),
    'data': f'Request received from IP: {request.remote_addr} ' +
            f'User-Agent: {request.headers.get("User-Agent")} ' +
            f'Referer: {request.headers.get("Referer", "No referrer")} ' +
            f'Accept-Language: {request.headers.get("Accept-Language", "No language specified")}'
  })

  return send_file('../static/logistic-dashboard-report.pdf', mimetype='application/pdf')


# Main

if __name__ == '__main__':
  set_database(DATABASE_URL)
  app.run(host='0.0.0.0', port=8080)
