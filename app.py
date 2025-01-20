import tkinter as tk

INGREDIENTS = "ingredients"
# TODO Enable the user to update their ingredients list in the final version
INGREDIENTS_LIST: list[str] = ["tomato", "garlic", "olive oil", "pasta", "salt"]
NAME = "name"
RECIPES = []


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

search_button = tk.Button(root, text="Search Recipes", command=search_recipes)
search_button.pack(pady=5)

ingredients_text = tk.StringVar()
ingredients_display = tk.Label(root, textvariable=ingredients_text, justify=tk.LEFT)
ingredients_display.pack(pady=10)

update_ingredients_display()

result_text = tk.StringVar()
result_display = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_display.pack(pady=10)

root.mainloop()
