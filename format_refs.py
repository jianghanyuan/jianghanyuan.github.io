import re

path = "/Users/mikejiang/Documents/GitHub/jianghanyuan.github.io/content/blog/blue-sky-1.md"
with open(path, "r") as f:
    text = f.read()

# 1. Update References with IDs
# Let's map Authors to their IDs
refs = [
    ("Arendt", "1958", "arendt1958"),
    ("Arbib", "2012", "arbib2012"),
    ("Bishop", "2006", "bishop2006"),
    ("Hassabis", "2017", "hassabis2017"),
    ("Marcus", "2018", "marcus2018"),
    ("McGilchrist", "2009", "mcgilchrist2009"),
    ("Mitchell", "2019", "mitchell2019"),
    ("Noether", "1918", "noether1918"),
    ("Polanyi", "1966", "polanyi1966"),
    ("Sutton", "2019", "sutton2019"),
    ("Sutton", "1998", "sutton1998"),
    ("Tomasello", "2003", "tomasello2003"),
    ("Tomasello", "2014", "tomasello2014"),
    ("Weber", "1922", "weber1922"),
    ("Weyl", "1952", "weyl1952"),
    ("Wolpert", "1996", "wolpert1996"),
    ("Zhang", "2016", "zhang2016"),
]

for author, year, ref_id in refs:
    # Update the li
    # e.g. <li>Noether, E. (1918)
    li_pattern = r"(<li>)(" + author + r".*?\(" + year + r".*?\))"
    text = re.sub(li_pattern, rf'<li id="ref-{ref_id}">\2', text)
    
    # Update the text citation
    # e.g. (Noether, 1918)
    cit_pattern = r"\(" + author + r"(.*?),?\s*" + year + r"\)"
    # Some citations might be (Author et al., Year)
    text = re.sub(cit_pattern, rf'[({author}\1, {year})](#ref-{ref_id})', text)

# Find remaining pure (Author, Year) using (Author et al., Year|Author, Year) that were not caught
text = text.replace("[(Noether, 1918)](#ref-noether1918)", "([Noether, 1918](#ref-noether1918))")
for author, year, ref_id in refs:
    text = text.replace(f"[({author}, {year})](#ref-{ref_id})", f"([{author}, {year}](#ref-{ref_id}))")
    text = text.replace(f"[({author} et al., {year})](#ref-{ref_id})", f"([{author} et al., {year}](#ref-{ref_id}))")
    text = text.replace(f"[{author}, {year}](#ref-{ref_id})", f"[{author}, {year}](#ref-{ref_id})") # already linked

# 2. Add philosophical emphasis (bold/italics)
claims = [
    ("The ancient engine of human learning is not merely pattern recognition; it is longing.", 
     "**The ancient engine of human learning is not merely pattern recognition; it is longing.**"),
    ("We are building minds that can compute anything but care about nothing.",
     "**We are building minds that can compute anything but care about nothing.**"),
    ("Intelligence, it turns out, is trivially easy to simulate. It is caring that is hard.",
     "**Intelligence, it turns out, is trivially easy to simulate. It is *caring* that is hard.**"),
    ("what we can learn about a system equals the invariant structure preserved under transformations we can observe.",
     "**what we can learn about a system equals the invariant structure preserved under transformations we can observe**."),
    ("Their learning is driven by the necessity of survival, the vulnerability of the body, and the need for attachment.",
     "**Their learning is driven by the necessity of survival, the vulnerability of the body, and the need for attachment.**")
]

for old, new in claims:
    text = text.replace(old, new)
    
with open(path, "w") as f:
    f.write(text)
