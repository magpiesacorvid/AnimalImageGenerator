import json, random
from pathlib import Path

animals = json.loads(Path("animals.json").read_text())
chosen = random.choice(animals)

output = f"""
## 🐾 Random Animal

### {chosen["name"]}

![{chosen["name"]}]({chosen["url"]})
"""

Path("ANIMAL.md").write_text(output)
