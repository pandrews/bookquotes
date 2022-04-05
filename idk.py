import json
from flask import Flask, request, jsonify

app = Flask(__name__)

f = open('bookquotes.json')
records = json.load(f)

quotes = []

@app.route('/quotes', methods=['GET'])
def get_quotes():
  return jsonify(records)

app.run()
