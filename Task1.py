# Flask route Decorator Uses

from flask import Flask
app = Flask(__name__)

          # >>>>>> Write one line here for correct route
def tableof2():
    return str([i*2 for i in range(1, 10+1)])

app.run(debug=True)