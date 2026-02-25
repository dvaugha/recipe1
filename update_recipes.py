import json

def update_recipes_11_to_15():
    with open('recipes.json', 'r') as f:
        recipes = json.load(f)
    
    # Recipe 11: Shrimp and Grits
    recipes[10]['icon'] = '🥣'
    recipes[10]['image_url'] = 'https://images.unsplash.com/photo-1505253304499-671c5ecfb3ae?auto=format&fit=crop&w=800&q=80'
    recipes[10]['instructions'] = [
        "Cook grits according to package instructions with extra butter and cheese.",
        "Sauté shrimp with garlic, green onions, and a dash of hot sauce.",
        "Serve the spicy shrimp over the hot, creamy cheesy grits.",
        "Garnish with fresh parsley and extra black pepper."
    ]
    
    # Recipe 12: Roasted Pork Grain Bowl
    recipes[11]['icon'] = '🥗'
    recipes[11]['image_url'] = 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80'
    recipes[11]['instructions'] = [
        "Roast pork loin with garlic and herbs until the center is juicy.",
        "Prepare a base of warm quinoa or brown rice.",
        "Thinly slice the pork and arrange over the grains with fresh veggies.",
        "Drizzle with a light balsamic glaze or lemon-tahini dressing."
    ]
    
    # Recipe 13: Sizzling Beef Fajitas
    recipes[12]['icon'] = '🌮'
    recipes[12]['image_url'] = 'https://images.unsplash.com/photo-1534352956274-4390974ed281?auto=format&fit=crop&w=800&q=80'
    recipes[12]['instructions'] = [
        "Batch-cook bell pepper and onion strips in a very hot skillet.",
        "Sear thinly sliced beef strips with cumin and chili powder.",
        "Combine meat and veggies in the skillet for a final sizzle.",
        "Serve with warm flour tortillas, lime, and fresh salsa."
    ]
    
    # Recipe 14: BBQ Baby Back Ribs
    recipes[13]['icon'] = '🍖'
    recipes[13]['image_url'] = 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80'
    recipes[13]['instructions'] = [
        "Apply a dry rub of brown sugar and spices to the pork ribs.",
        "Slow-bake in the oven at 275F for 3 hours until tender.",
        "Brush with your favorite BBQ sauce and broil for 3-5 mins.",
        "Let the ribs rest before slicing for that classic fall-off-the-bone finish."
    ]
    
    # Recipe 15: Chicken Ramen
    recipes[14]['icon'] = '🍜'
    recipes[14]['image_url'] = 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80'
    recipes[14]['instructions'] = [
        "Simmer chicken in a rich ginger and garlic flavored broth.",
        "Cook ramen noodles until just tender (al dente).",
        "Assemble the bowl with noodles, broth, and sliced chicken.",
        "Add a soft-boiled egg, green onions, and a sheet of nori."
    ]

    with open('recipes.json', 'w') as f:
        json.dump(recipes, f, indent=2)

if __name__ == "__main__":
    update_recipes_11_to_15()
    print("Updated recipes 11-15 with large images and full instructions.")
