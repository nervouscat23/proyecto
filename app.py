import tkinter as tk

RECIPES = []


# Function to load recipes from a file
def load_recipes(filename: str = "recipes.txt"):
    with open(filename) as file:
        for line in file:
            name, ingredients = line.strip().split(":")
            ingredients = ingredients.split(",")
            RECIPES.append({"name": name, "ingredients": ingredients})


if __name__ == "__main__":
    # Load recipes from the file
    load_recipes()

    # Set up the GUI
    root = tk.Tk()
    root.title("Recipe Suggestion App")

    root.mainloop()
