from flask import Flask, jsonify
import random

output1 = {
    "Emotion" : "Anxious",
    "Products" : [{"Name" : "Taaza Jeera Chaach", "Size" : "250 ml", "Discount" : "28.5", "Price" : "30", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png"}, 
    {"Name" : "Dark Chocolate 55% - Nuts Infused", "Size" : "17 gm", "Discount" : "57", "Price" : "63", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}, 
    {"Name" : "Roasted Makhana - Cheese", "Size" : "25 gm", "Discount" : "67", "Price" : "74", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/roasted%20makhana.png"}],
    "Combos" : [{"Quote" : "Energetic Start", "Name" : "Chocolate Muesli & Milk", "Discount" : "285", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"},
    {"Quote" : "Tangy Filler", "Name" :"Malabar Parata & Pickles", "Discount" : "180", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}, 
    {"Quote" : "5 in 1 magic", "Name" : "Potato Chips - 5 flavours", "Discount" : "36/pack", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}]
}

output2 = {
    "Emotion": "Excited",
    "Products": [{"Name" : "Roasted Makhana - Cheese", "Size" : "25 gm", "Discount" : "67", "Price" : "74", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/roasted%20makhana.png"},
    {"Name" : "Taaza Jeera Chaach", "Size" : "250 ml", "Discount" : "28.5", "Price" : "30", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png"},
    {"Name" : "Spicy Boondi", "Size" : "120 gm", "Discount" : "61", "Price" : "68", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/spicy%20boondi.png"}],
    "Combos": [{"Quote" : "Tangy Filler", "Name" :"Malabar Parata & Pickles", "Discount" : "180", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}, 
    {"Quote" : "Heatwave Killer", "Name" : "Taaza Jeera Chaach & Malabar Parata", "Discount" : "130", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"},
    {"Quote" : "5 in 1 magic", "Name" : "Potato Chips - 5 flavours", "Discount" : "36/pack", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}]
}

output3 = {
    "Emotion": "Content",
    "Products": [{"Name" : "Taaza Pudina Masala Chaach", "Size" : "250 ml", "Discount" : "28.5", "Price" : "30", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/pudina%20masala%20chaach.png"},
    {"Name" : "Mango Yogurt", "Size" : "85 gm", "Discount" : "37", "Price" : "39", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/mango%20yogurt.png"},
    {"Name" : "Mango Lassi", "Size" : "140 ml", "Discount" : "42", "Price" : "44.5", "Link" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/mango%20lassi.png"}],
    "Combos": [{"Quote" : "Energetic Start", "Name" : "Chocolate Muesli & Milk", "Discount" : "285", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"},
    {"Quote" : "Tangy Filler", "Name" :"Malabar Parata & Pickles", "Discount" : "180", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}, 
    {"Quote" : "5 in 1 magic", "Name" : "Potato Chips - 5 flavours", "Discount" : "36/pack", "Link1" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/taaza%20jeera%20chach.png", "Link2" : "https://jiffktocmulaasqyzktz.supabase.co/storage/v1/object/public/user-input/FlutterImages/dark%20chocolate.png"}]
}

app = Flask(__name__)

@app.route("/", methods=["GET"])
def running():
    return "Welcome to the Must Duplicate API!"

@app.route("/result", methods=["POST","GET"])
def result():
    # output = [output1, output2, output3]
    output = [output1, output3]
    return jsonify(random.choice(output))


if __name__ == "__main__":
    app.run(debug = True)
