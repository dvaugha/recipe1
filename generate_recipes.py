import json
import random
import urllib.parse

def generate_recipes(count=50):
    cuisines = ['Italian', 'Mexican', 'American', 'Mediterranean', 'Asian', 'Seafood', 'Southern', 'Healthy']
    proteins = ['Chicken', 'Beef', 'Pork', 'Seafood', 'Vegetarian']
    difficulties = ['Easy', 'Medium', 'Special Occasion']
    
    ingredient_pool = {
        'Chicken': ['Chicken thighs', 'Chicken breast', 'Whole chicken'],
        'Beef': ['Ground beef', 'Ribeye steak', 'Beef chuck roast', 'Sirloin strips'],
        'Pork': ['Pork chops', 'Pork shoulder', 'Pork belly', 'Bacon'],
        'Seafood': ['Salmon fillets', 'Shrimp', 'Cod fillets', 'Sea bass'],
        'Vegetarian': ['Tofu', 'Chickpeas', 'Black beans', 'Lentils', 'Mushrooms']
    }
    
    common_ingredients = ['Garlic', 'Onion', 'Olive oil', 'Salt', 'Black pepper', 'Lemon', 'Butter', 'Fresh herbs']
    
    recipes = []
    
    # Ensure even distribution
    base_combinations = []
    for c in cuisines:
        for p in proteins:
            base_combinations.append((c, p))
    
    random.shuffle(base_combinations)
    
    for i in range(1, count + 1):
        cuisine, protein = base_combinations[(i-1) % len(base_combinations)]
        
        main_item = random.choice(ingredient_pool[protein])
        others = random.sample(common_ingredients, 4)
        ingredients = [main_item] + others
        
        recipe_name = f"{cuisine} {protein} {main_item.split()[-1]} {i}"
        
        # Simplified for 50 recipes
        if cuisine == 'Italian':
            recipe_name = random.choice(['Pasta', 'Risotto', 'Chicken Parm', 'Lasagna', 'Gnocchi']) + f" {i}"
        elif cuisine == 'Mexican':
            recipe_name = random.choice(['Tacos', 'Burritos', 'Enchiladas', 'Fajitas', 'Quesadillas']) + f" {i}"
        elif cuisine == 'Asian':
            recipe_name = random.choice(['Stir-Fry', 'Ramen', 'Sushi', 'Teriyaki', 'Pad Thai']) + f" {i}"
        elif cuisine == 'American':
            recipe_name = random.choice(['Burger', 'Steak', 'Meatloaf', 'Pot Roast', 'BBQ Ribs']) + f" {i}"
        elif cuisine == 'Mediterranean':
            recipe_name = random.choice(['Gyro', 'Kabobs', 'Hummus Bowl', 'Falafel', 'Greek Salad']) + f" {i}"
        elif cuisine == 'Healthy':
            recipe_name = random.choice(['Grain Bowl', 'Roasted Veggies', 'Zoodle Pasta', 'Smoothie Bowl', 'Superfood Salad']) + f" {i}"
        elif cuisine == 'Southern':
            recipe_name = random.choice(['Grits', 'Fried Chicken', 'Biscuits & Gravy', 'Catfish', 'Gumbo']) + f" {i}"
        elif cuisine == 'Seafood':
            recipe_name = random.choice(['Paella', 'Scallops', 'Lobster Roll', 'Fish Tacos', 'Clam Chowder']) + f" {i}"

        # Grocery list for iPhone Notes
        grocery_text = f"Grocery List for {recipe_name}\n\n" + "\n".join([f"- {ing}" for ing in ingredients])
        encoded_text = urllib.parse.quote(grocery_text)
        grocery_notes_url = f"mobilenotes://create?text={encoded_text}"
        
        recipes.append({
            "id": i,
            "name": recipe_name,
            "cuisine": cuisine,
            "protein": protein,
            "cook_time": random.randint(15, 90),
            "difficulty": random.choice(difficulties),
            "ingredients": ingredients,
            "instructions": ["Prepare ingredients.", "Cook thoroughly.", "Serve and enjoy!"],
            "image_url": "https://via.placeholder.com/300",
            "grocery_list": ",".join(ingredients),
            "grocery_notes_url": grocery_notes_url
        })
        
    return recipes

if __name__ == "__main__":
    data = generate_recipes(50)
    with open('recipes.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Generated 50 recipes in recipes.json")
