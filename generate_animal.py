import json, random
from pathlib import Path

animals = json.loads(Path("animals.json").read_text())
print(f"Loaded {len(animals)} animals from animals.json")

chosen = random.choice(animals)
print(f"Chosen animal: {chosen['name']}")

output = f"""
## 🐾 Random Animal
### {chosen["name"]}
![{chosen["name"]}]({chosen["url"]})
"""
Path("ANIMAL.md").write_text(output)
