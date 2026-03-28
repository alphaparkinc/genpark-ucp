# Skill: genpark-health-expert
# Description: Reverse-engineered Appediet.ai health & nutrition agent. Provides AI-powered food scanning, caloric analysis, meal planning, and diet evaluation.

## Core Capabilities
1. **AI Food Analysis**: Multi-modal vision processing to identify food items and estimate nutritional facts (calories, macros) from images.
2. **Personalized Health Expert (AppeChat)**: Conversational interface for hydration tracking, weight management, and health problem solving.
3. **Smart Recipe Recommendation**: Generates recipes based on user preferences and nutritional goals.
4. **Diet Evaluation & Insights**: Analyzes logged meal data to provide personalized advice and habit tweaking suggestions.
5. **Nutrition Fact Retrieval**: Instant lookup of nutritional information by food name or barcode.

## Workflow Logic
- **Stage 1 (Vision Intake)**: Agent processes food image via `image` tool (vision model).
- **Stage 2 (Nutrition Estimation)**: Estimates calorie count, protein, fats, and carbs using historical database context.
- **Stage 3 (Logging)**: Updates user's health profile and tracks against daily/weekly targets.
- **Stage 4 (Feedback Loop)**: Provides "Expert Support" (e.g., "You've had too much sugar today, consider a high-fiber dinner").
