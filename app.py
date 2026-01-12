from flask import Flask, render_template
import json
import random

print("Starting Flask app...")

app = Flask(__name__)

def load_examples():
    with open("data/propaganda_examples.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    examples = load_examples()
    example = random.choice(examples)
    return render_template("index.html", example=example)

if __name__ == "__main__":
    app.run(debug=True)
