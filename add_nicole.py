import json

def add_nicole_top_10():
    with open('recipes.json', 'r') as f:
        recipes = json.load(f)
    
    # Calculate starting ID
    start_id = len(recipes) + 1
    
    nicole_recipes = [
        {
            "id": start_id,
            "name": "Meatball Sub Casserole",
            "cuisine": "American",
            "protein": "Beef",
            "cook_time": 45,
            "difficulty": "Easy",
            "ingredients": ["Frozen meatballs", "Marinara sauce", "Refrigerated biscuits", "Mozzarella cheese", "Italian seasoning", "Garlic powder"],
            "instructions": [
                "Preheat oven to 375F.",
                "Cut biscuits into quarters and toss with garlic powder and herbs.",
                "Lay biscuits in a baking dish, top with meatballs and marinara sauce.",
                "Bake for 20 minutes, then top with mozzarella and bake until bubbly."
            ],
            "image_url": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80",
            "icon": "🥘"
        },
        {
            "id": start_id + 1,
            "name": "Turkey Taco Casserole",
            "cuisine": "Mexican",
            "protein": "Pork", # Using Ground Turkey usually, but following your protein list
            "cook_time": 35,
            "difficulty": "Easy",
            "ingredients": ["Ground turkey (or pork)", "Taco seasoning", "Corn chips", "Black beans", "Shredded cheddar", "Salsa"],
            "instructions": [
                "Brown meat in a skillet and stir in taco seasoning.",
                "In a baking dish, layer corn chips, meat mixture, beans, and salsa.",
                "Top with plenty of cheese.",
                "Bake at 350F for 15-20 minutes until cheese is melted."
            ],
            "image_url": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80",
            "icon": "🌮"
        },
        {
            "id": start_id + 2,
            "name": "Sheet Pan Chicken Fajitas",
            "cuisine": "Mexican",
            "protein": "Chicken",
            "cook_time": 30,
            "difficulty": "Easy",
            "ingredients": ["Chicken breasts", "Bell peppers", "Onion", "Fajita seasoning", "Olive oil", "Tortillas"],
            "instructions": [
                "Slice chicken, peppers, and onions into strips.",
                "Toss everything on a sheet pan with oil and fajita seasoning.",
                "Roast at 400F for 20 minutes until chicken is cooked through.",
                "Serve with warm tortillas and your favorite toppings."
            ],
            "image_url": "https://images.unsplash.com/photo-1534352956274-4390974ed281?auto=format&fit=crop&w=800&q=80",
            "icon": "🌮"
        },
        {
            "id": start_id + 3,
            "name": "French Onion Mac and Cheese",
            "cuisine": "American",
            "protein": "Vegetarian",
            "cook_time": 50,
            "difficulty": "Medium",
            "ingredients": ["Macaroni", "Caramelized onions", "Gruyere cheese", "Milk", "Butter", "Flour", "Beef broth splash"],
            "instructions": [
                "Caramelize onions slowly in butter until dark and sweet.",
                "Make a cheese sauce with flour, butter, milk, and Gruyere.",
                "Combine cooked macaroni, onions, and sauce.",
                "Top with extra cheese and bake until golden brown."
            ],
            "image_url": "https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=800&q=80",
            "icon": "🧀"
        },
        {
            "id": start_id + 4,
            "name": "Lemon Chicken and Rice Casserole",
            "cuisine": "Healthy",
            "protein": "Chicken",
            "cook_time": 60,
            "difficulty": "Easy",
            "ingredients": ["Chicken thighs", "White rice", "Chicken broth", "Lemon juice", "Garlic", "Butter", "Oregano"],
            "instructions": [
                "Combine rice, broth, lemon juice, and seasonings in a baking dish.",
                "Place seasoned chicken thighs on top of the rice.",
                "Cover with foil and bake at 375F for 45 minutes.",
                "Remove foil and bake for 15 more minutes to crisp the chicken skin."
            ],
            "image_url": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=800&q=80",
            "icon": "🍋"
        },
        {
            "id": start_id + 5,
            "name": "Sheet Pan Steak Bites",
            "cuisine": "American",
            "protein": "Beef",
            "cook_time": 25,
            "difficulty": "Easy",
            "ingredients": ["Sirloin steak cubes", "Asparagus", "Baby potatoes", "Garlic butter", "Thyme", "Salt", "Pepper"],
            "instructions": [
                "Toss potatoes with oil and roast for 15 minutes first.",
                "Add steak bites and asparagus to the pan.",
                "Drizzle everything with garlic butter and herbs.",
                "Broil for 5-7 minutes until steak is seared and tender."
            ],
            "image_url": "https://images.unsplash.com/photo-1594041680534-e8c8cdebd679?auto=format&fit=crop&w=800&q=80",
            "icon": "🥩"
        },
        {
            "id": start_id + 6,
            "name": "Everything Bagel Salmon",
            "cuisine": "Seafood",
            "protein": "Seafood",
            "cook_time": 20,
            "difficulty": "Easy",
            "ingredients": ["Salmon fillets", "Everything bagel seasoning", "Honey", "Dijon mustard", "Broccoli", "Sweet potatoes"],
            "instructions": [
                "Mix honey and mustard; brush over salmon fillets.",
                "Coat generously with everything bagel seasoning.",
                "Place on a sheet pan with veggies.",
                "Roast at 400F for 12-15 minutes."
            ],
            "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80",
            "icon": "🐟"
        },
        {
            "id": start_id + 7,
            "name": "Pierogi and Sausage Sheet Pan",
            "cuisine": "American",
            "protein": "Pork",
            "cook_time": 30,
            "difficulty": "Easy",
            "ingredients": ["Frozen pierogis", "Kielbasa sausage", "Bell peppers", "Onion", "Olive oil", "Cajun seasoning"],
            "instructions": [
                "Slice sausage and vegetables.",
                "Toss pierogis, sausage, and veggies with oil and seasoning on a sheet pan.",
                "Roast at 400F for 20-25 minutes, flipping halfway.",
                "Serve with a side of sour cream."
            ],
            "image_url": "https://images.unsplash.com/photo-1541529086526-db283c563270?auto=format&fit=crop&w=800&q=80",
            "icon": "🥘"
        },
        {
            "id": start_id + 8,
            "name": "Easy Meaty Sheet Pan Meal",
            "cuisine": "American",
            "protein": "Beef",
            "cook_time": 30,
            "difficulty": "Easy",
            "ingredients": ["Ground beef", "Potatoes", "Carrots", "Onion", "Worcestershire sauce", "Garlic"],
            "instructions": [
                "Form seasoned ground beef into small patties or balls.",
                "Arrange on a pan with thinly sliced potatoes and carrots.",
                "Drizzle with oil and Worcestershire sauce.",
                "Bake at 400F for 25 minutes."
            ],
            "image_url": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?auto=format&fit=crop&w=800&q=80",
            "icon": "🥩"
        },
        {
            "id": start_id + 9,
            "name": "Sheet Pan Quesadillas",
            "cuisine": "Mexican",
            "protein": "Vegetarian",
            "cook_time": 25,
            "difficulty": "Easy",
            "ingredients": ["Tortillas", "Shredded cheese", "Black beans", "Corn", "Jalapenos", "Butter"],
            "instructions": [
                "Overlap tortillas on a large sheet pan so they hang off the edges.",
                "Fill the center with cheese, beans, and corn.",
                "Fold the tortillas over the filling and place another sheet pan on top to weigh it down.",
                "Bake at 425F for 20 minutes until golden and melty."
            ],
            "image_url": "https://images.unsplash.com/photo-1599974579688-8dbdd335c77f?auto=format&fit=crop&w=800&q=80",
            "icon": "🌮"
        }
    ]

    # Generate grocery list and notes URL for each
    import urllib.parse
    for r in nicole_recipes:
        r['grocery_list'] = ",".join(r['ingredients'])
        grocery_text = f"Grocery List for {r['name']}\n\n" + "\n".join([f"- {ing}" for ing in r['ingredients']])
        encoded_text = urllib.parse.quote(grocery_text)
        r['grocery_notes_url'] = f"mobilenotes://create?text={encoded_text}"
        recipes.append(r)

    with open('recipes.json', 'w') as f:
        json.dump(recipes, f, indent=2)

if __name__ == "__main__":
    add_nicole_top_10()
    print("Added Nicole McLaughlin's Top 10 Recipes to the database.")
