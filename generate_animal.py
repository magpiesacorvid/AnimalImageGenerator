import json
import random
from pathlib import Path

animals = json.loads(Path("animals.json").read_text())

chosen = random.choice(animals)

name = chosen["name"]
url = chosen["url"]

output = f"""
## 🐾 Random Animal

### {name}

![{name}]({url})
"""

Path("ANIMAL.md").write_text(output)

print("Selected:", name)
