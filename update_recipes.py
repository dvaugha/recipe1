import json

def update_recipes_41_to_50():
    with open('recipes.json', 'r') as f:
        recipes = json.load(f)
    
    # Batch 41-50
    data_updates = [
        {"id": 41, "name": "Biscuits & Gravy", "icon": "🥐", "img": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
         "instr": ["Bake flaky buttermilk biscuits until golden brown.", "Prepare a creamy white gravy with sautéed chicken sausage crumbles.", "Season generously with black pepper.", "Split the warm biscuits and smother with the hot gravy."]},
        {"id": 42, "name": "Steak Zoodle Pasta", "icon": "🍝", "img": "https://images.unsplash.com/photo-1645112481357-19453911049c?auto=format&fit=crop&w=800&q=80",
         "instr": ["Sear thinly sliced beef strips until medium-rare.", "Spiralize zucchini and sauté briefly with garlic and red pepper flakes.", "Toss the steak and zoodles together with a splash of soy sauce.", "Garnish with sesame seeds and green onions."]},
        {"id": 43, "name": "Beef Falafel Platter", "icon": "🥘", "img": "https://images.unsplash.com/photo-1547060013-165fb0bbba43?auto=format&fit=crop&w=800&q=80",
         "instr": ["Combine crispy falafel with seasoned ground beef.", "Serve over a platter of hummus and tabbouleh salad.", "Add a side of olives and feta cheese.", "Drizzle with tahini and serve with warm pita bread pieces."]},
        {"id": 44, "name": "Veggie Gyro", "icon": "🥙", "img": "https://images.unsplash.com/photo-1599940824399-b87987cb247a?auto=format&fit=crop&w=800&q=80",
         "instr": ["Grill slices of halloumi cheese and seasoned eggplant.", "Warm a pita and spread with a thick layer of tzatziki.", "Stuff with the grilled cheese, veggies, and fresh tomatoes.", "Finish with red onions and a sprinkle of dried oregano."]},
        {"id": 45, "name": "Rainbow Roasted Veggies", "icon": "🥗", "img": "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?auto=format&fit=crop&w=800&q=80",
         "instr": ["Chop bell peppers, zucchini, carrots, and sweet potatoes.", "Toss with olive oil, salt, and rosemary.", "Roast at 400F until caramelized and tender.", "Serve as a main bowl with a dollop of Greek yogurt or tahini."]},
        {"id": 46, "name": "Black Bean Burger", "icon": "🍔", "img": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
         "instr": ["Mash black beans with spices, breadcrumbs, and finely chopped onions.", "Form into patties and pan-sear until crispy on the outside.", "Serve on a toasted bun with avocado, sprouts, and spicy mayo.", "Add a slice of pepper jack cheese for extra flavor."]},
        {"id": 47, "name": "Beef Teriyaki", "icon": "🍜", "img": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?auto=format&fit=crop&w=800&q=80",
         "instr": ["Sauté thinly sliced beef with a homemade teriyaki glaze.", "Add snap peas and carrots for crunch.", "Serve over a bowl of steamed jasmine rice.", "Garnish with sesame seeds and fresh scallions."]},
        {"id": 48, "name": "Al Pastor Pork Tacos", "icon": "🌮", "img": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80",
         "instr": ["Marinate pork in achiote, chili, and pineapple juice.", "Grill until charred and thinly slice.", "Serve in soft corn tortillas with fresh pineapple chunks.", "Top with cilantro, onion, and a squeeze of lime."]},
        {"id": 49, "name": "Pork & Ginger Stir-Fry", "icon": "🍛", "img": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=80",
         "instr": ["Wok-fry pork strips with plenty of fresh ginger and garlic.", "Add broccoli, peppers, and a savory soy-oyster sauce.", "Toss over high heat until the vegetables are tender-crisp.", "Serve immediate over white or brown rice."]},
        {"id": 50, "name": "Ultimate Bean Burrito", "icon": "🌯", "img": "https://images.unsplash.com/photo-1534353436294-0dbd4bdac845?auto=format&fit=crop&w=800&q=80",
         "instr": ["Refry black beans with cumin and lime.", "Fill a large tortilla with beans, Mexican rice, and plenty of cheese.", "Add fresh salsa and a dollop of sour cream.", "Fold and grill the burrito for 1 minute per side to melt the cheese."]}
    ]

    for update in data_updates:
        idx = update['id'] - 1
        recipes[idx]['name'] = update['name']
        recipes[idx]['icon'] = update['icon']
        recipes[idx]['image_url'] = update['img']
        recipes[idx]['instructions'] = update['instr']

    with open('recipes.json', 'w') as f:
        json.dump(recipes, f, indent=2)

if __name__ == "__main__":
    update_recipes_41_to_50()
    print("Completed all 50 recipes with HD images and full instructions.")
