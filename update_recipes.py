import json

def update_first_five():
    with open('recipes.json', 'r') as f:
        recipes = json.load(f)
    
    # Recipe 1
    recipes[0]['icon'] = '🍗'
    recipes[0]['instructions'] = [
        "Season chicken breast with salt and fresh herbs.",
        "Melt butter in a large skillet over medium heat.",
        "Add garlic and sear chicken until internal temp reaches 165F.",
        "Rest for 5 minutes before serving with a drizzle of pan juices."
    ]
    
    # Recipe 2
    recipes[1]['icon'] = '🥗'
    recipes[1]['instructions'] = [
        "Sear beef chuck roast on all sides until browned.",
        "Place in slow cooker with garlic and fresh herbs.",
        "Cook on low for 6-8 hours until fork-tender.",
        "Shred meat and serve over a bed of grains with a squeeze of fresh lemon."
    ]
    
    # Recipe 3
    recipes[2]['icon'] = '🥙'
    recipes[2]['instructions'] = [
        "Season sirloin strips with black pepper and salt.",
        "Quickly sear in a hot pan with butter for 2-3 minutes.",
        "Spread hummus on a serving plate or bowl.",
        "Top with beef, fresh herbs, and a squeeze of lemon."
    ]
    
    # Recipe 4
    recipes[3]['icon'] = '🥗'
    recipes[3]['instructions'] = [
        "Press tofu to remove excess moisture and cut into cubes.",
        "Toss with lemon juice, fresh herbs, and chopped onion.",
        "Sauté until edges are slightly crisp.",
        "Serve fresh as a salad or bowl base."
    ]
    
    # Recipe 5
    recipes[4]['icon'] = '🍝'
    recipes[4]['instructions'] = [
        "Spiralize zucchini into noodles (zoodles).",
        "Sauté minced garlic and onion in butter until fragrant.",
        "Add tofu cubes and cook until browned.",
        "Toss in zoodles for 2 minutes and finish with fresh lemon juice."
    ]

    # For the rest of the recipes, add a default icon based on cuisine just to be safe
    cuisine_icons = {
        'Italian': '🍝', 'Mexican': '🌮', 'American': '🥩', 'Mediterranean': '🥙',
        'Asian': '🍜', 'Seafood': '🐟', 'Southern': '🍗', 'Healthy': '🥗'
    }
    for r in recipes[5:]:
        r['icon'] = cuisine_icons.get(r['cuisine'], '🍴')

    with open('recipes.json', 'w') as f:
        json.dump(recipes, f, indent=2)

if __name__ == "__main__":
    update_first_five()
    print("Updated first 5 recipes with better instructions and icons.")
