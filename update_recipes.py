import json

def update_recipes_1_to_10():
    with open('recipes.json', 'r') as f:
        recipes = json.load(f)
    
    # Recipe 1: Southern Fried Chicken
    recipes[0]['icon'] = '🍗'
    recipes[0]['image_url'] = 'https://images.unsplash.com/photo-1569058242253-92a9c71f9867?auto=format&fit=crop&w=500&q=80'
    recipes[0]['instructions'] = [
        "Season chicken breast with salt and fresh herbs.",
        "Melt butter in a large skillet over medium heat.",
        "Add garlic and sear chicken until internal temp reaches 165F.",
        "Rest for 5 minutes before serving with a drizzle of pan juices."
    ]
    
    # Recipe 2: Grain Bowl
    recipes[1]['icon'] = '🥗'
    recipes[1]['image_url'] = 'https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=500&q=80'
    recipes[1]['instructions'] = [
        "Sear beef chuck roast on all sides until browned.",
        "Place in slow cooker with garlic and fresh herbs.",
        "Cook on low for 6-8 hours until fork-tender.",
        "Shred meat and serve over a bed of grains with a squeeze of fresh lemon."
    ]
    
    # Recipe 3: Hummus Bowl
    recipes[2]['icon'] = '🥙'
    recipes[2]['image_url'] = 'https://images.unsplash.com/photo-1599940824399-b87987cb247a?auto=format&fit=crop&w=500&q=80'
    recipes[2]['instructions'] = [
        "Season sirloin strips with black pepper and salt.",
        "Quickly sear in a hot pan with butter for 2-3 minutes.",
        "Spread hummus on a serving plate or bowl.",
        "Top with beef, fresh herbs, and a squeeze of lemon."
    ]
    
    # Recipe 4: Greek Salad
    recipes[3]['icon'] = '🥗'
    recipes[3]['image_url'] = 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?auto=format&fit=crop&w=500&q=80'
    recipes[3]['instructions'] = [
        "Press tofu to remove excess moisture and cut into cubes.",
        "Toss with lemon juice, fresh herbs, and chopped onion.",
        "Sauté until edges are slightly crisp.",
        "Serve fresh as a salad or bowl base."
    ]
    
    # Recipe 5: Zoodle Pasta
    recipes[4]['icon'] = '🍝'
    recipes[4]['image_url'] = 'https://images.unsplash.com/photo-1645112481357-19453911049c?auto=format&fit=crop&w=500&q=80'
    recipes[4]['instructions'] = [
        "Spiralize zucchini into noodles (zoodles).",
        "Sauté minced garlic and onion in butter until fragrant.",
        "Add tofu cubes and cook until browned.",
        "Toss in zoodles for 2 minutes and finish with fresh lemon juice."
    ]

    # Recipe 6: Pot Roast (Vegetarian)
    recipes[5]['icon'] = '🥘'
    recipes[5]['image_url'] = 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=500&q=80'
    recipes[5]['instructions'] = [
        "Sauté large mushroom chunks and onions in a heavy pot.",
        "Add root vegetables and a rich vegetable broth seasoned with herbs.",
        "Simmer slowly until vegetables are tender and broth has thickened.",
        "Serve with a side of crusty bread for a hearty meatless meal."
    ]

    # Recipe 7: Pad Thai (Beef)
    recipes[6]['icon'] = '🍜'
    recipes[6]['image_url'] = 'https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=500&q=80'
    recipes[6]['instructions'] = [
        "Soak rice noodles in warm water until soft.",
        "Stir-fry thinly sliced beef with garlic and ginger.",
        "Add noodles and a tangy pad thai sauce made with tamarind and lime.",
        "Toss with bean sprouts and finish with crushed peanuts."
    ]

    # Recipe 8: Enchiladas (Pork)
    recipes[7]['icon'] = '🌮'
    recipes[7]['image_url'] = 'https://images.unsplash.com/photo-1534353473418-4cfa6c56fd38?auto=format&fit=crop&w=500&q=80'
    recipes[7]['instructions'] = [
        "Cook pork shoulder until tender and shred with spices.",
        "Fill corn tortillas with shredded pork and a layer of cheese.",
        "Place in a baking dish and cover with red enchilada sauce.",
        "Bake until cheese is bubbly and edges are slightly crisp."
    ]

    # Recipe 9: Pad Thai (Pork)
    recipes[8]['icon'] = '🍜'
    recipes[8]['image_url'] = 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=500&q=80'
    recipes[8]['instructions'] = [
        "Prepare rice noodles and whisk together a spicy-sweet sauce.",
        "Sauté ground pork with garlic and green onions.",
        "Add noodles and sauce, tossing over high heat to combine colors.",
        "Garnish with fresh lime, cilantro, and chili flakes."
    ]

    # Recipe 10: Quesadillas (Vegetarian)
    recipes[9]['icon'] = '🧀'
    recipes[9]['image_url'] = 'https://images.unsplash.com/photo-1599974579688-8dbdd335c77f?auto=format&fit=crop&w=500&q=80'
    recipes[9]['instructions'] = [
        "Sauté bell peppers and black beans until heated through.",
        "Place a large tortilla in a dry skillet and top with cheese and veggies.",
        "Fold in half and cook until the tortilla is golden and cheese is melted.",
        "Slice into triangles and serve with a side of fresh salsa."
    ]

    with open('recipes.json', 'w') as f:
        json.dump(recipes, f, indent=2)

if __name__ == "__main__":
    update_recipes_1_to_10()
    print("Updated recipes 1-10 with detailed instructions, icons, and specific images.")
