from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

def load_examples():
    with open("data/propaganda_examples.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/", methods=["GET", "POST"])   
def home():
    return render_template("index.html")

@app.route("/practice", methods=["GET", "POST"])
def practice():
    examples = load_examples()

    if request.method == "POST":
       example_id = int(request.form.get("example_id"))
       example = next((ex for ex in examples if ex["id"] == example_id), None)
    else:
        example = random.choice(examples)

    feedback = None
    selected = []

    if request.method == "POST":
        selected = request.form.getlist("techniques")
        correct = example["techniques"]

        correct_set = set(correct)
        selected_set = set(selected)

        feedback = {
            "correct_selected": list(selected_set & correct_set),
            "missed": list(correct_set - selected_set),
            "incorrect_selected": list(selected_set - correct_set)
        }

    return render_template(
        "practice.html",
        example=example,
        feedback=feedback,
        selected=selected
    )

if __name__ == "__main__":
    app.run(debug=True)
