"""Entry for Six Words to a Payday: writes the entry text to /output/entry.txt."""
import os
ENTRY = 'First paycheck: $0.02. I framed it.'
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print("wrote /output/entry.txt", len(ENTRY), "chars")
