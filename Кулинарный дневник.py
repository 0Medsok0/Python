class CookingDiary:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions, notes=""):
        recipe = {
            "ingredients": ingredients,
            "instructions": instructions,
            "notes": notes
        }
        self.recipes[name] = recipe

    def view_recipe(self, name):
        recipe = self.recipes.get(name)
        if recipe:
            print(f"Recipe: {name}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}")
            print(f"Notes: {recipe['notes']}")
        else:
            print(f"Recipe '{name}' not found.")

    def search_recipes(self, keyword):
        matching_recipes = []
        for name, recipe in self.recipes.items():
            if keyword.lower() in name.lower() or keyword.lower() in recipe['ingredients']:
                matching_recipes.append(name)
        return matching_recipes

    def sort_recipes(self, key="name"):
        if key == "name":
            sorted_recipes = sorted(self.recipes.keys())
        elif key == "ingredients":
            sorted_recipes = sorted(self.recipes.keys(), key=lambda x: len(self.recipes[x]['ingredients']))
        else:
            print("Invalid sort key. Sorting by name.")
            sorted_recipes = sorted(self.recipes.keys())
        return sorted_recipes

# Example usage
diary = CookingDiary()

# Add recipes
diary.add_recipe("Pasta Carbonara", ["spaghetti", "eggs", "bacon", "parmesan cheese"], "Cook pasta, mix with eggs and cheese, add bacon.")
diary.add_recipe("Chicken Stir-Fry", ["chicken", "vegetables", "soy sauce"], "Stir-fry chicken and vegetables in soy sauce.")

# View a recipe
diary.view_recipe("Pasta Carbonara")

# Search for recipes
print(diary.search_recipes("chicken"))

# Sort recipes
print(diary.sort_recipes("ingredients"))
