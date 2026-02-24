import re

path = "/Users/mikejiang/Documents/GitHub/jianghanyuan.github.io/content/blog/vision/blue-sky-1.md"
with open(path, "r") as f:
    text = f.read()

parts = text.split("---\n")
if len(parts) >= 3:
    frontmatter = "---\n" + parts[1] + "---\n"
    body = "---\n".join(parts[2:])
else:
    frontmatter = ""
    body = text

lines = body.split("\n")
new_lines = []

for i, line in enumerate(lines):
    stripped = line.strip()
    
    if line.startswith("## "):
        if len(new_lines) > 0 and new_lines[-1].strip() != "":
            new_lines.append("")
        if line.startswith("## II. The Ancient Engine"):
            new_lines.append("## II. Ancient Engines")
        else:
            new_lines.append(line)
        new_lines.append("")
        continue

    if not stripped:
        new_lines.append(line)
        continue
        
    new_lines.append(line)
    
    if i + 1 < len(lines):
        next_obj = lines[i+1].strip()
        if stripped and next_obj:
            if not next_obj.startswith("##") and not next_obj.startswith("<") and not stripped.startswith("<") and not next_obj.startswith("---") and not next_obj.startswith("1"):
                new_lines.append("")

cleaned = re.sub(r'\n{3,}', '\n\n', "\n".join(new_lines))

with open(path, "w") as f:
    f.write(frontmatter + cleaned)
