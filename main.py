from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
  return "Alive"

def run():
  app.run(host="0.0.0.0",port=10000, debug=True)

def keep_alive():  
  t1 = Thread(target=run)
  t1.start()

keep_alive()
