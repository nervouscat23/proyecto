import tkinter as tk

from tkinter import messagebox

INGREDIENTS = "ingredients"
INGREDIENTS_LIST: list[str] = []
NAME = "name"
RECIPES = []


# Function to add ingredients to the list
def add_ingredient():
    ingredient = ingredient_entry.get()
    if ingredient:
        INGREDIENTS_LIST.append(ingredient)
        ingredient_entry.delete(0, tk.END)
        update_ingredients_display()
    else:
        messagebox.showwarning("Input Error", "Please enter an ingredient")


# Function to display the list of ingredients
def update_ingredients_display():
    ingredients_text.set("\n".join(INGREDIENTS_LIST))


# Function to search for matching recipes
def search_recipes():
    matches = []
    for recipe in RECIPES:
        if all(item in INGREDIENTS_LIST for item in recipe[INGREDIENTS]):
            matches.append(recipe[NAME])

    result_text.set("\n".join(matches) if matches else "No matching recipes found")


# Function to load recipes from a file
def load_recipes(filename: str = "recipes.txt"):
    with open(filename) as file:
        for line in file:
            name, ingredients = line.strip().split(":")
            ingredients = ingredients.split(",")
            RECIPES.append({NAME: name, INGREDIENTS: ingredients})


# Load recipes from the file
load_recipes()

# Set up the GUI
root = tk.Tk()
root.title("Recipe Suggestion App")

ingredient_entry = tk.Entry(root, width=30)
ingredient_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Ingredient", command=add_ingredient)
add_button.pack(pady=5)

search_button = tk.Button(root, text="Search Recipes", command=search_recipes)
search_button.pack(pady=5)

ingredients_text = tk.StringVar()
ingredients_display = tk.Label(root, textvariable=ingredients_text, justify=tk.LEFT)
ingredients_display.pack(pady=10)

result_text = tk.StringVar()
result_display = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_display.pack(pady=10)

root.mainloop()
