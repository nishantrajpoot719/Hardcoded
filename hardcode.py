from flask import Flask, jsonify
import random

output1 = {
    "Emotion" : "Anxious",
    "Products" : ["Taaza Jeera Chaach", "Dark Chocolate 55% - Nuts Infused", "Roasted Makhana - Cheese"],
    "Combos" : ["Mango Yogurt & Muesli and Flakes - Chocolate Muesli", "Malabar Parata & Pickles", "Chips - Magic Masala - Potato Chips & No Maida Puffs - Disney Cream & Onion Puffs"]
}

output2 = {
    "Emotion": "Excited",
    "Products": ["Roasted Makhana - Cheese","Taaza Jeera Chaach","Spicy Boondi"],
    "Combos": ["Malabar Parata & Pickles","Taaza Jeera Chaach & Malabar Parata","Spicy Boondi & Malabar Parata"]
}

output3 = {
    "Emotion": "Content",
    "Products": ["Taaza Pudina Masala Chaach","Mango Yogurt","Mango Lassi"],
    "Combos": ["Taaza Pudina Masala Chaach & Muesli","Mango Yogurt & Muesli and Flakes - Muesli","Mango Lassi & Muesli"]
}

app = Flask(__name__)

@app.route("/", methods=["GET"])
def running():
    return "Welcome to the Must Duplicate API!"

@app.route("/result", methods=["POST","GET"])
def result():
    output = [output1, output2, output3]
    return jsonify(random.choice(output))


if __name__ == "__main__":
    app.run(debug = True)
    
