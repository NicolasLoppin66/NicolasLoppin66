import datetime
import re

README_PATH = "README.md"
DATE_NAISSANCE = datetime.date(2000, 5, 5)  # À modifier si besoin

# Calcul de l'âge
aujourd_hui = datetime.date.today()
age = (
    aujourd_hui.year
    - DATE_NAISSANCE.year
    - (
        (aujourd_hui.month, aujourd_hui.day)
        < (DATE_NAISSANCE.month, DATE_NAISSANCE.day)
    )
)

badge_pattern = (
    r"(https://img\.shields\.io/badge/Âge-)(\d+)_ans(-red\?style=for-the-badge)"
)

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(badge_pattern, rf"\\1{age}_ans\\3", content)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)
