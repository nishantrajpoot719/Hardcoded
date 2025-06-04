import random
import json

output1 = {
    "Emotion" : "Anxious",
    "Top Products" : ["Taaza Jeera Chaach", "Dark Chocolate 55% - Nuts Infused", "Roasted Makhana - Cheese"],
    "Top Combos" : ["Mango Yogurt & Muesli and Flakes - Chocolate Muesli", "Malabar Parata & Pickles", "Chips - Magic Masala - Potato Chips & No Maida Puffs - Disney Cream & Onion Puffs"]
}

output2 = {
    "Emotion": "Excited",
    "Top Products": ["Roasted Makhana - Cheese","Taaza Jeera Chaach","Spicy Boondi"],
    "Top Combos": ["Malabar Parata & Pickles","Taaza Jeera Chaach & Malabar Parata","Spicy Boondi & Malabar Parata"]
}

output3 = {
    "Emotion": "Content",
    "Top Products": ["Taaza Pudina Masala Chaach","Mango Yogurt","Mango Lassi"],
    "Top Combos": ["Taaza Pudina Masala Chaach & Muesli","Mango Yogurt & Muesli and Flakes - Muesli","Mango Lassi & Muesli"]
}

output = [output1, output2, output3]
print(json.dumps(random.choice(output), indent=4))