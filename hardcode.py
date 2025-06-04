from flask import Flask, jsonify
import random

output1 = {
    "Emotion" : "Anxious",
    "Top Products" : [{"Name" : "Taaza Jeera Chaach", "Size" : "250 ml", "Discount" : "28.5", "Price" : "30", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png"}, 
    {"Name" : "Dark Chocolate 55% - Nuts Infused", "Size" : "17 gm", "Discount" : "57", "Price" : "63", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}, 
    {"Name" : "Roasted Makhana - Cheese", "Size" : "25 gm", "Discount" : "67", "Price" : "74", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/roasted%20makhana.png"}],
    "Top Combos" : [{"Quote" : "Energetic Start", "Name" : "Chocolate Muesli & Milk", "Discount" : "285", "Link1" : "", "Link2" : ""},
    {"Quote" : "Tangy Filler", "Name" :"Malabar Parata & Pickles", "Discount" : "180", "Link1" : "", "Link2" : ""}, 
    {"Quote" : "5 in 1 magic", "Name" : "Potato Chips - 5 flavours", "Discount" : "36/pack", "Link1" : "", "Link2" : ""}]
}

output2 = {
    "Emotion": "Excited",
    "Top Products": [{"Name" : "Roasted Makhana - Cheese", "Size" : "25 gm", "Discount" : "67", "Price" : "74", "Link" : ""},
    {"Name" : "Taaza Jeera Chaach", "Size" : "250 ml", "Discount" : "28.5", "Price" : "30", "Link" : ""},
    {"Name" : "Spicy Boondi", "Size" : "120 gm", "Discount" : "61", "Price" : "68", "Link" : ""}],
    "Top Combos": [{"Quote" : "Tangy Filler", "Name" :"Malabar Parata & Pickles", "Discount" : "180", "Link1" : "", "Link2" : ""}, 
    {"Quote" : "Heatwave Killer", "Name" : "Taaza Jeera Chaach & Malabar Parata", "Discount" : "130", "Link1" : "", "Link2" : ""},
    {"Quote" : "5 in 1 magic", "Name" : "Potato Chips - 5 flavours", "Discount" : "36/pack", "Link1" : "", "Link2" : ""}]
}

output3 = {
    "Emotion": "Content",
    "Top Products": [{"Name" : "Taaza Pudina Masala Chaach", "Size" : "250 ml", "Discount" : "28.5", "Price" : "30", "Link" : ""},
    {"Name" : "Mango Yogurt", "Size" : "85 gm", "Discount" : "37", "Price" : "39", "Link" : ""},
    {"Name" : "Mango Lassi", "Size" : "140 ml", "Discount" : "42", "Price" : "44.5", "Link" : ""}],
    "Top Combos": [{"Quote" : "Energetic Start", "Name" : "Chocolate Muesli & Milk", "Discount" : "285", "Link1" : "", "Link2" : ""},
    {"Quote" : "Tangy Filler", "Name" :"Malabar Parata & Pickles", "Discount" : "180", "Link1" : "", "Link2" : ""}, 
    {"Quote" : "5 in 1 magic", "Name" : "Potato Chips - 5 flavours", "Discount" : "36/pack", "Link1" : "", "Link2" : ""}]
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
