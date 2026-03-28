import os
import sys
import json
import asyncio

class AppedietEngine:
    """
    Reverse-engineered Appediet.com Logic:
    1. Vision Processing: Analyzing food images (simulated).
    2. Calorie Estimation: Mapping food items to caloric values.
    3. Health Expert (AppeChat): Conversational nutrition advice.
    4. Daily Tracking: Hydration and weight logging.
    """

    def __init__(self, user_profile=None):
        self.user_profile = user_profile or {"daily_goal": 2000, "current_calories": 0}
        self.food_db = {
            "apple": 95,
            "chicken breast": 165,
            "avocado": 160,
            "latte": 120,
            "pizza slice": 285
        }

    async def analyze_food_image(self, image_path):
        print(f"[*] Appediet Vision: Analyzing food in '{image_path}'...")
        # Simulates AI Vision identification
        detected_food = "avocado" # Hardcoded for simulation
        return detected_food

    async def get_nutrition_facts(self, food_name):
        print(f"[*] Fetching nutrition facts for: {food_name}")
        calories = self.food_db.get(food_name.lower(), 100) # Default to 100
        return {"item": food_name, "calories": calories, "protein": "low", "macros": "stable"}

    async def diet_evaluation(self, daily_log):
        print(f"[*] AppeChat: Evaluating today's diet...")
        total_cal = sum(item['calories'] for item in daily_log)
        if total_cal > self.user_profile['daily_goal']:
            return "Alert: You've exceeded your daily goal. Suggesting light dinner."
        return "Good progress! You are on track for your health goals."

    async def recommend_recipe(self, preference="low carb"):
        print(f"[*] Recipe Expert: Finding {preference} recipes for you...")
        return ["Grilled Salmon with Asparagus", "Zucchini Noodles", "Cauliflower Fried Rice"]

    async def run_flow(self, action, data=None):
        print(f"🚀 Appediet Flow Init: Action -> '{action}'")
        if action == "SCAN":
            food = await self.analyze_food_image(data or "sample_meal.jpg")
            facts = await self.get_nutrition_facts(food)
            print(f"  [Result] {facts['item']}: {facts['calories']} kcal")
            return facts
        elif action == "EVALUATE":
            log = data or [{"calories": 500}, {"calories": 600}]
            advice = await self.diet_evaluation(log)
            print(f"  [Advice] {advice}")
            return advice
        elif action == "RECIPE":
            recipes = await self.recommend_recipe()
            print(f"  [Recipes] Found: {recipes}")
            return recipes
            
        print("[+] Appediet Engine Sequence Complete.")

if __name__ == "__main__":
    engine = AppedietEngine()
    action = sys.argv[1] if len(sys.argv) > 1 else "SCAN"
    asyncio.run(engine.run_flow(action))
