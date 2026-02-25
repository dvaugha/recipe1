import json

def update_recipes_16_to_20():
    with open('recipes.json', 'r') as f:
        recipes = json.load(f)
    
    # Recipe 16: Beef Parmigiana
    recipes[15]['name'] = 'Beef Parmigiana'
    recipes[15]['icon'] = '🍖'
    recipes[15]['image_url'] = 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80'
    recipes[15]['instructions'] = [
        "Tenderize beef steaks and coat in flour, egg, and seasoned breadcrumbs.",
        "Fry until golden brown and place in a baking dish.",
        "Top with marinara sauce and a generous amount of mozzarella cheese.",
        "Bake at 400F until the cheese is bubbly and slightly browned."
    ]
    
    # Recipe 17: Mushroom Risotto
    recipes[16]['name'] = 'Mushroom Risotto'
    recipes[16]['icon'] = '🍚'
    recipes[16]['image_url'] = 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?auto=format&fit=crop&w=800&q=80'
    recipes[16]['instructions'] = [
        "Sauté mushrooms and onions in butter until soft and golden.",
        "Add arborio rice and toast slightly before adding warm broth one ladle at a time.",
        "Stir continuously until the rice is creamy and perfectly cooked.",
        "Finish with parmesan cheese, fresh herbs, and a final knob of butter."
    ]
    
    # Recipe 18: Seafood Fra Diavolo
    recipes[17]['name'] = 'Seafood Fra Diavolo'
    recipes[17]['icon'] = '🍝'
    recipes[17]['image_url'] = 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80'
    recipes[17]['instructions'] = [
        "Sauté a mix of shrimp, scallops, and squid in a spicy garlic tomato sauce.",
        "Add red pepper flakes and a splash of white wine for that signature kick.",
        "Toss with al dente linguine pasta until well coated.",
        "Garnish with fresh parsley and serve immediately while hot."
    ]
    
    # Recipe 19: Pork Souvlaki
    recipes[18]['name'] = 'Pork Souvlaki'
    recipes[18]['icon'] = '🍢'
    recipes[18]['image_url'] = 'https://images.unsplash.com/photo-1603073163308-9654c3fb70b5?auto=format&fit=crop&w=800&q=80'
    recipes[18]['instructions'] = [
        "Marinate pork chunks in olive oil, lemon, oregano, and garlic for 2 hours.",
        "Thread the meat onto skewers and grill over high heat until charred and cooked.",
        "Serve with warm pita bread, sliced onions, and a scoop of cool tzatziki.",
        "Drizzle with extra lemon juice and a sprinkle of paprika."
    ]
    
    # Recipe 20: Fried Tofu Nuggets
    recipes[19]['name'] = 'Fried Tofu Nuggets'
    recipes[19]['icon'] = '🍗'
    recipes[19]['image_url'] = 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80'
    recipes[19]['instructions'] = [
        "Press extra-firm tofu and cut into bite-sized nugget shapes.",
        "Dip in a seasoned flour batter and fry until extremely crispy and golden.",
        "Toss with a dash of salt and your favorite Southern-style spices.",
        "Serve with a smoky BBQ or honey mustard dipping sauce."
    ]

    with open('recipes.json', 'w') as f:
        json.dump(recipes, f, indent=2)

if __name__ == "__main__":
    update_recipes_16_to_20()
    print("Updated recipes 16-20 with detailed instructions, icons, and specific images.")
