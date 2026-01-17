# Fichier : main.py
from fastapi import FastAPI
from recipe_scrapers import scrape_me
import re

app = FastAPI()

@app.get("/scrape")
def get_recipe(url: str, target_servings: int):
    scraper = scrape_me(url)
    # Extraction du nombre de personnes original
    original_yield = scraper.yields()
    original_servings = int(re.search(r'\d+', original_yield).group())
    
    ratio = target_servings / original_servings
    
    ingredients_list = []
    for ing in scraper.ingredients():
        # Logique de parsing simplifiée
        ingredients_list.append({"raw": ing, "ratio": ratio})
        
    return {
        "title": scraper.title(),
        "ingredients": ingredients_list,
        "image": scraper.image()
    }