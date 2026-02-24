# Recipe1 - Structured Dinner Recipes

This repository contains a JSON database of 50 unique dinner recipes, designed for home cooks.

## Features
- **50 Structured Recipes**: JSON format with ID, name, cuisine, protein, cook time, difficulty, ingredients, and instructions.
- **iPhone Notes Integration**: Each recipe includes a `grocery_notes_url` using the `mobilenotes://` scheme to automatically open the Notes app on an iPhone with a pre-filled grocery list.
- **Even Distribution**: Varied cuisines and proteins.

## Files
- `recipes.json`: The generated recipe database.
- `generate_recipes.py`: The Python script used to generate the database.

## Usage
Simply import `recipes.json` into your application or use the `grocery_notes_url` to trigger grocery list creation on mobile devices.
