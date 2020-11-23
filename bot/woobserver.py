"""
Not asyncronishesge webserver to store webhook data in webhooks.json

Why not async?
I'm to not smart enough yet to prevent overwrites in async :]


The woobserver is just for saving i think

"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "yeet", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

