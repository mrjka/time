from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def printTime():
    currTime = time.time()
    return str(currTime)

if __name__ == "__main__":
	app.run()
