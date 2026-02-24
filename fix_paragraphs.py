import re

path = "/Users/mikejiang/Documents/GitHub/jianghanyuan.github.io/content/blog/vision/blue-sky-1.md"
with open(path, "r") as f:
    text = f.read()

parts = text.split("## I. The Silent Projections")
if len(parts) < 2:
    print("Error splitting")
    
front = parts[0]
body = "## I. The Silent Projections" + parts[1]

lines = body.split("\n")
new_lines = []

for i, line in enumerate(lines):
    new_lines.append(line)
    if not line.strip():
        continue
    if i + 1 < len(lines):
        next_line = lines[i+1]
        if line.strip() and next_line.strip():
            # If both lines are text, and not headers or HTML
            if not line.startswith("##") and not next_line.startswith("##") and not next_line.startswith("---") and not next_line.startswith("<") and not line.startswith("<"):
                if not next_line.startswith("The basal ganglia") and not next_line.startswith("Their delight was") and not next_line.startswith("Consider more") and not next_line.startswith("The answer, I") and not next_line.startswith("The prisoners succeed") and not next_line.startswith("What invariances has") and not next_line.startswith("But what invariances") and not next_line.startswith("Yet humans also") and not next_line.startswith("This realization forces"):
                    # The user already fixed some manual ones in the diff, we'll just broadly add newline.
                    new_lines.append("")

with open(path, "w") as f:
    f.write(front + "\n".join(new_lines))
