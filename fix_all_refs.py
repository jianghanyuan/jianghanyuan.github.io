import re

path = "content/blog/blue-sky-1.md"
with open(path, "r") as f:
    text = f.read()

# Separate the main text and the bibliography
lines = text.split("\n")
ol_start = -1
for i, line in enumerate(lines):
    if line.startswith("<ol"):
        ol_start = i
        break

if ol_start == -1:
    print("No bibliography found.")
    exit(1)

main_text = "\n".join(lines[:ol_start])
bib_text = "\n".join(lines[ol_start:])

# 1. Parse all bibliography items.
# They look like: <li id="ref-marcus2018">Marcus, G. (2018)...</li>
# or without an id.
bib_entries = []
li_pattern = re.compile(r"<li([^>]*)>(.*?)</li>", re.DOTALL)
def process_bib(match):
    attrs = match.group(1)
    content = match.group(2).strip()
    
    id_match = re.search(r'id=["\']?([^"\'>\s]+)', attrs)
    ref_id = id_match.group(1) if id_match else None
    
    # We want to map these to potential text strings.
    # E.g., "(Smith & Jones, 2020)" -> "smith", "jones", "2020"
    
    # Let's extract year
    year_match = re.search(r'\((\d{4}[a-z]?)\)', content)
    year = year_match.group(1) if year_match else ""
    
    # Let's extract the first few authors' last names.
    # Usually: "Name, A., Name2, B., & Name3, C. (Year)"
    authors_part = content.split('(' + year + ')')[0] if year else content
    
    # A simple heuristic: all capitalized words before the year that are > 2 letters might be author names.
    # Or just grab the very first word before a comma.
    first_author_last = authors_part.split(',')[0].strip().split()[-1]
    
    if not ref_id and first_author_last and year:
        ref_id = f"ref-{first_author_last.lower()}{year}"
    if not ref_id:
        ref_id = "ref-unknown"
        
    return first_author_last, year, ref_id, attrs, content

parsed_bibs = []
for m in li_pattern.finditer(bib_text):
    first_author, year, ref_id, attrs, contentStr = process_bib(m)
    parsed_bibs.append({
        'author': first_author,
        'year': year,
        'id': ref_id,
        'original': m.group(0),
        'content': contentStr
    })
    
# Rebuild bibliography with IDs if they were missing
new_bib_text = bib_text
for bib in parsed_bibs:
    old_li = bib['original']
    if 'id=' not in old_li:
        # replace the <li ...> with <li id="...">
        new_li = re.sub(r'<li', f'<li id="{bib["id"]}"', old_li, count=1)
        new_bib_text = new_bib_text.replace(old_li, new_li)

# 2. Find all citations in the main text.
# Types of citations:
# (Author, Year) -> (Chomsky, 1995)
# (Author & Author, Year) -> (Pearl & Mackenzie, 2018)
# (Author et al., Year) -> (Mikolov et al., 2013)
# Author (Year) -> Chomsky (1995)
# Author et al. (Year) -> Mikolov et al. (2013)

# We will search for any 4-digit code in parentheses or preceeded by a name.
# Let's use a regex to find all matches of:  (Name [Name ...] [et al.] [,] Year)
# and Name [Name ...] [et al.] (Year)

import string

def get_best_ref(text_snippet):
    # Try to find exactly one matching bib entry
    # text_snippet might be "Pearl & Mackenzie, 2018"
    year_match = re.search(r'\b(\d{4}[a-z]?)\b', text_snippet)
    if not year_match: return None
    year = year_match.group(1)
    
    words = text_snippet.replace(',', ' ').split()
    first_word = words[0]
    
    # Find matching bib entry
    for bib in parsed_bibs:
        if bib['year'] == year and bib['author'].lower() == first_word.lower().strip(string.punctuation):
            return bib['id']
            
    # If not found, try second word if first word is something like "("
    if len(words) > 1:
        second_word = words[1]
        for bib in parsed_bibs:
            if bib['year'] == year and bib['author'].lower() == second_word.lower().strip(string.punctuation):
                return bib['id']
                
    return None

# Find (Something 19XX/20XX)
# This regex looks for ( ... 19xx ... ) or ( ... 20xx ... )
# and replaces it if it's not already linked.
# To avoid double linking, we skip if it's inside []
# Actually, an easier way is to just do a global replace on the unlinked text.
# We will temporarily remove existing links, then recreate all.
# Wait, let's just find unlinked ones.

unlinked_pattern_1 = re.compile(r'(?<!\[)\(([^)]+?\s(?:19|20)\d{2}[a-z]?)\)(?!\()')
def replacer_1(m):
    inner = m.group(1)
    ref_id = get_best_ref(inner)
    if ref_id:
        return f"([{inner}](#{ref_id}))"
    return m.group(0)

main_text = unlinked_pattern_1.sub(replacer_1, main_text)

# Find Name (Year)
# Regex: a capitalized word, optionally "et al." or "& Name", followed by (Year)
# E.g. Tomasello (2014)
unlinked_pattern_2 = re.compile(r'(?<!\[)([A-Z][a-z]+(?:\s+et\s+al\.)?(?:\s+&\s+[A-Z][a-z]+)?)\s+\(((?:19|20)\d{2}[a-z]?)\)(?!\()')
def replacer_2(m):
    inner = m.group(1) + " (" + m.group(2) + ")"
    ref_id = get_best_ref(inner)
    if ref_id:
        return f"[{inner}](#{ref_id})"
    return m.group(0)

main_text = unlinked_pattern_2.sub(replacer_2, main_text)

# Also check for ones already inside brackets that missed the link? No, we didn't do that.

with open(path, "w") as f:
    f.write(main_text + "\n" + new_bib_text)

print("Updated text.")
