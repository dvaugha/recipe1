import json

def update_recipes_21_to_40():
    with open('recipes.json', 'r') as f:
        recipes = json.load(f)
    
    # Refresh Recipe 1 image (Extra HD link)
    recipes[0]['image_url'] = 'https://images.unsplash.com/photo-1626645738196-c2a7c8d38f58?auto=format&fit=crop&w=1000&q=80'

    # Batch 21-40
    data_updates = [
        {"id": 21, "name": "Crispy Pork Belly", "icon": "🥓", "img": "https://images.unsplash.com/photo-1593001874117-c99c800e3eb7?auto=format&fit=crop&w=800&q=80", 
         "instr": ["Score the pork belly skin in a diamond pattern.", "Rub with plenty of salt and five-spice powder.", "Roast at a low temperature until tender, then blast with high heat to crisp the skin.", "Slice into thick pieces and serve with a hot mustard dip."]},
        {"id": 22, "name": "Pan-Seared Scallops", "icon": "🐚", "img": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?auto=format&fit=crop&w=800&q=80",
         "instr": ["Pat scallops dry with a paper towel; this is the key to a good sear.", "Sear in a smoking hot pan with oil for 90 seconds per side until golden.", "Add butter and lemon to the pan to baste for the final 30 seconds.", "Serve immediately on a bed of pea purée or with crusty bread."]},
        {"id": 23, "name": "Spicy Seafood Ramen", "icon": "🍜", "img": "https://images.unsplash.com/photo-1547928576-a4a33237bec3?auto=format&fit=crop&w=800&q=80",
         "instr": ["Simmer a seafood broth with ginger, garlic, and chili paste.", "Add shrimp, squid, and mussels until they just open.", "Pour the hot broth over fresh ramen noodles.", "Top with a soft egg, scallions, and a drizzle of sesame oil."]},
        {"id": 24, "name": "Vegetarian Pad Thai", "icon": "🍜", "img": "https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=800&q=80",
         "instr": ["Stir-fry tofu cubes with garlic and bok choy.", "Add soaked rice noodles and a tangy sweet-sour tamarind sauce.", "Toss in bean sprouts, cilantro, and green onions.", "Finish with a squeeze of lime and a handful of crushed peanuts."]},
        {"id": 25, "name": "Seafood Grain Bowl", "icon": "🥗", "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80",
         "instr": ["Cook farro or quinoa in salted water until tender.", "Top with chilled shrimp, avocado slices, and cucumber.", "Add a scoop of seaweed salad and some pickled ginger.", "Drizzle with a light soy-sesame dressing before serving."]},
        {"id": 26, "name": "Grilled Tuna Steak", "icon": "🐟", "img": "https://images.unsplash.com/photo-1514326640560-7d06307a0db4?auto=format&fit=crop&w=800&q=80",
         "instr": ["Brush tuna steaks with olive oil and season with lemon pepper.", "Grill over high heat for only 1-2 minutes per side to keep central rare.", "Serve with a side of grilled asparagus and a lemon wedge.", "Garnish with fresh parsley or cilantro."]},
        {"id": 27, "name": "Shrimp Burritos", "icon": "🌯", "img": "https://images.unsplash.com/photo-1534353436294-0dbd4bdac845?auto=format&fit=crop&w=800&q=80",
         "instr": ["Sauté shrimp with taco seasoning and lime juice.", "Fill large tortillas with rice, beans, shrimp, and cheese.", "Roll tightly and toast on a dry pan until the exterior is golden.", "Serve with a side of guacamole and cool sour cream."]},
        {"id": 28, "name": "Classic Lobster Roll", "icon": "🦞", "img": "https://images.unsplash.com/photo-1599487488170-a309e46a784d?auto=format&fit=crop&w=800&q=80",
         "instr": ["Chop cooked lobster meat into large, bite-sized chunks.", "Lightly toss with a small amount of mayo, celery, and lemon juice.", "Toast a split-top bun in plenty of butter.", "Stuff the warm bun with the chilled lobster and sprinkle with chives."]},
        {"id": 29, "name": "Pork Ragu Pasta", "icon": "🍝", "img": "https://images.unsplash.com/photo-1546549032-9571cd6b27df?auto=format&fit=crop&w=800&q=80",
         "instr": ["Slow-cook ground pork with tomatoes, garlic, and red wine for 2 hours.", "Toss the rich sauce with al dente pappardelle or rigatoni.", "Add a splash of heavy cream for a silkier texture.", "Serve with plenty of freshly grated parmesan cheese."]},
        {"id": 30, "name": "Classic Meatloaf", "icon": "🍞", "img": "https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?auto=format&fit=crop&w=800&q=80",
         "instr": ["Mix ground beef with breadcrumbs, onion, and egg.", "Press into a loaf pan and top with a glaze of ketchup and brown sugar.", "Bake at 350F for about an hour until cooked through.", "Let rest for 10 minutes before slicing to keep it moist."]},
        {"id": 31, "name": "Zoodle Chicken Pasta", "icon": "🍝", "img": "https://images.unsplash.com/photo-1645112481357-19453911049c?auto=format&fit=crop&w=800&q=80",
         "instr": ["Pan-sear chicken strips until golden and cooked.", "In the same pan, sauté garlic and cherry tomatoes until they burst.", "Toss in zucchini noodles for just 2 minutes so they stay crisp.", "Finish with fresh basil and a sprinkle of parmesan."]},
        {"id": 32, "name": "Honey Garlic Scallops", "icon": "🐚", "img": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?auto=format&fit=crop&w=800&q=80",
         "instr": ["Sear scallops in a hot pan until golden brown on both sides.", "Whisk together honey, soy sauce, and minced garlic.", "Pour the sauce into the pan for the last minute to glaze the scallops.", "Serve over steamed rice with some steamed broccoli."]},
        {"id": 33, "name": "Beef Fried Chicken Style", "icon": "🥩", "img": "https://images.unsplash.com/photo-1594041680534-e8c8cdebd679?auto=format&fit=crop&w=800&q=80",
         "instr": ["Thinly slice beef and coat in a seasoned flour batter.", "Deep fry until extremely crispy (like country fried steak).", "Top with a creamy white gravy and secondary herbs.", "Serve with mashed potatoes and buttery corn."]},
        {"id": 34, "name": "Classic Chicken Parm", "icon": "🍝", "img": "https://images.unsplash.com/photo-1632778149975-420e0e32e672?auto=format&fit=crop&w=800&q=80",
         "instr": ["Bread chicken cutlets and fry until golden.", "Layer with marinara and thick slices of mozzarella.", "Bake until cheese is bubbly and edges are crisp.", "Serve on a bed of spaghetti with extra sauce."]},
        {"id": 35, "name": "Vegetarian Paella", "icon": "🥘", "img": "https://images.unsplash.com/photo-1534080564607-198f9dd5d61a?auto=format&fit=crop&w=800&q=80",
         "instr": ["Sauté bell peppers, artichokes, and peas in a wide pan.", "Add saffron-infused broth and short-grain rice (calasparra).", "Cook undisturbed until the 'socarrat' (crispy bottom) forms.", "Garnish with lemon wedges and fresh parsley."]},
        {"id": 36, "name": "Chicken Meatloaf", "icon": "🍞", "img": "https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?auto=format&fit=crop&w=800&q=80",
         "instr": ["Mix ground chicken with herbs, onion, and breadcrumbs.", "Brush with a savory balsamic glaze instead of ketchup.", "Bake until internal temp reaches 165F.", "Serve with steamed green beans and mashed sweet potatoes."]},
        {"id": 37, "name": "Seafood Gyro", "icon": "🥙", "img": "https://images.unsplash.com/photo-1599940824399-b87987cb247a?auto=format&fit=crop&w=800&q=80",
         "instr": ["Grill seasoned shrimp and squid until tender.", "Warm a pita and spread with a thick layer of tzatziki.", "Stuff with the seafood, tomatoes, cucumbers, and red onion.", "Finish with a dash of Greek seasoning and lemon juice."]},
        {"id": 38, "name": "Steak & Scallops", "icon": "🥩", "img": "https://images.unsplash.com/photo-1594041680534-e8c8cdebd679?auto=format&fit=crop&w=800&q=80",
         "instr": ["Pan-sear a thick steak until medium-rare, then rest.", "In the same pan, sear scallops until golden brown.", "Deglaze the pan with butter and garlic to drizzle over both.", "Serve with a side of smashed potatoes and green beans."]},
        {"id": 39, "name": "Chicken Soft Tacos", "icon": "🌮", "img": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=800&q=80",
         "instr": ["Season shredded chicken with lime, cumin, and chili.", "Warm soft corn tortillas over an open flame.", "Fill with chicken, fresh pico de gallo, and avocado.", "Top with cotija cheese and fresh cilantro."]},
        {"id": 40, "name": "Chicken Falafel Bowl", "icon": "🥗", "img": "https://images.unsplash.com/photo-1547060013-165fb0bbba43?auto=format&fit=crop&w=800&q=80",
         "instr": ["Serve crispy falafel balls alongside grilled chicken strips.", "Arrange over a bed of baby spinach and cucumber salad.", "Add a generous scoop of hummus and some pickled cabbage.", "Drizzle with tahini sauce and sprinkle with sesame seeds."]}
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
    update_recipes_21_to_40()
    print("Updated recipes 21-40 and refreshed Recipe 1.")
