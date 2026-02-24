import re

path = "content/blog/blue-sky-1.md"
with open(path, "r") as f:
    text = f.read()

# 1. Parse the <ol> at the bottom to find all list items.
# We will look for <li>...</li> in the bottom chunk.
lines = text.split("\n")
ol_start = -1
for i, line in enumerate(lines):
    if line.startswith("<ol>"):
        ol_start = i
        break

if ol_start != -1:
    # Get all lines in the ol
    ol_text = "\n".join(lines[ol_start:])
    
    # regex to find <li> tags
    li_pattern = re.compile(r"<li([^>]*)>(.*?)</li>", re.DOTALL)
    
    # We will build a list of (author_key, year, ref_id, new_li)
    extracted_refs = []
    
    def process_li(match):
        attrs = match.group(1)
        content = match.group(2).strip()
        
        # if it already has an id, keep it
        id_match = re.search(r'id=["\']?([^"\'>\s]+)', attrs)
        if id_match:
            ref_id = id_match.group(1)
        else:
            ref_id = None
            
        # Extract author and year from content.
        # usually: "Author, F. (Year)." or "Author, F., & Author, S. (Year)"
        # Let's grab the first word before a comma, and the first 4-digit number in parentheses.
        
        # Author: everything up to the first comma, or just the first word if no comma.
        first_word = content.split(',')[0].strip()
        author_key = first_word.split(' ')[-1] # last word of the first block, e.g. "Jiang" from "Hanyuan Jiang" (though it's usually "Jiang, H.")
        
        year_match = re.search(r'\((\d{4})[a-z]?\)', content)
        year = year_match.group(1) if year_match else ""
        
        if not ref_id and author_key and year:
            ref_id = f"ref-{author_key.lower()}{year}"
            
        if not ref_id:
            ref_id = "ref-unknown"
            
        new_attrs = attrs
        if 'id=' not in new_attrs:
            new_attrs += f' id="{ref_id}"'
            
        extracted_refs.append((author_key, year, ref_id))
        return f"<li{new_attrs}>{content}</li>"

    new_ol_text = li_pattern.sub(process_li, ol_text)
    
    # Now replace the ol_text in the main text
    text = "\n".join(lines[:ol_start]) + "\n" + new_ol_text
    
    # Print what we found so we can see
    print("Found references:")
    for a, y, rid in extracted_refs:
        print(f"  {a} {y} -> {rid}")
        
    # Now let's try to link citations.
    # Citations can look like (Author, Year) or Author (Year).
    # This is tricky because some might already be linked: [Author (Year)](#ref)
    # We will do a generic replacement matching the exact author and year.
    for author, year, ref_id in extracted_refs:
        if not author or not year: continue
        
        # (Author, Year)
        # e.g., (Tomasello, 2014)
        pat1 = re.compile(r'(?<!\[)\((' + author + r'(?:[^)]*?)' + year + r')\)(?!\()')
        text = pat1.sub(r'([\1](#' + ref_id + r'))', text)
        
        # Author (Year)
        # e.g., Tomasello (2014)
        pat2 = re.compile(r'(?<!\[)\b' + author + r'\s+\(' + year + r'\)(?!\()')
        text = pat2.sub(rf'[{author} ({year})](#{ref_id})', text)

with open(path, "w") as f:
    f.write(text)
