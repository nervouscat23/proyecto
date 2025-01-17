import tkinter as tk

RECIPES = []


# Function to load recipes from a file
def load_recipes(filename: str = "recipes.txt"):
    with open(filename) as file:
        for line in file:
            name, ingredients = line.strip().split(":")
            ingredients = ingredients.split(",")
            RECIPES.append({"name": name, "ingredients": ingredients})


# Load recipes from the file
load_recipes()

# Set up the GUI
root = tk.Tk()
root.title("Recipe Suggestion App")

result_text = tk.StringVar()
result_display = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_display.pack(pady=10)

root.mainloop()
