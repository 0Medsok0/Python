class MealPlanner:
    def __init__(self):
        self.recipes = {}
        self.user_preferences = {}

    def add_recipe(self, name, ingredients, instructions, calories, nutrients):
        recipe = {
            "ingredients": ingredients,
            "instructions": instructions,
            "calories": calories,
            "nutrients": nutrients
        }
        self.recipes[name] = recipe

    def set_user_preferences(self, dietary_restrictions, allergies, calorie_limit, nutrient_goals):
        self.user_preferences = {
            "dietary_restrictions": dietary_restrictions,
            "allergies": allergies,
            "calorie_limit": calorie_limit,
            "nutrient_goals": nutrient_goals
        }

    def generate_meal_plan(self, days):
        meal_plan = []
        for _ in range(days):
            suitable_recipes = [name for name, recipe in self.recipes.items() if self.is_suitable_recipe(recipe)]
            if suitable_recipes:
                meal_plan.append(suitable_recipes[0])  # Select the first suitable recipe
            else:
                meal_plan.append("No suitable recipe found.")
        return meal_plan

    def is_suitable_recipe(self, recipe):
        if any(ingredient in self.user_preferences["allergies"] for ingredient in recipe["ingredients"]):
            return False
        if any(ingredient in self.user_preferences["dietary_restrictions"] for ingredient in recipe["ingredients"]):
            return False
        if recipe["calories"] > self.user_preferences["calorie_limit"]:
            return False
        # Add more constraints and checks here
        return True

# Example usage
planner = MealPlanner()

# Add recipes
planner.add_recipe("Pasta Carbonara", ["spaghetti", "eggs", "bacon", "parmesan cheese"], "Cook pasta, mix with eggs and cheese, add bacon.", 500, {"protein": 20, "carbs": 70, "fat": 25})
planner.add_recipe("Chicken Stir-Fry", ["chicken", "vegetables", "soy sauce"], "Stir-fry chicken and vegetables in soy sauce.", 350, {"protein": 30, "carbs": 30, "fat": 10})

# Set user preferences
planner.set_user_preferences(["vegan"], ["eggs"], 400, {"protein": 30, "carbs": 50, "fat": 20})

# Generate a meal plan for 7 days
meal_plan = planner.generate_meal_plan(7)
print(meal_plan)
