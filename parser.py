import json

with open("skills.json") as skills_json:
    skill_data = json.load(skills_json)

meta_skills = skill_data["meta_skills"]
offensive_auras = skill_data["offensive_auras"]
defensive_auras = skill_data["defensive_auras"]
utility_auras = skill_data["utility_auras"]
utilities = skill_data["utilities"]

for meta_skill in meta_skills:
    print(meta_skill["name"])