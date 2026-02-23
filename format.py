import re

def process():
    with open('/Users/mikejiang/Documents/GitHub/jianghanyuan.github.io/content/blog/vision/blue sky.md', 'r') as f:
        content = f.read()

    # Split into sections
    parts = content.split('References\n')
    main_text = parts[0]
    ref_and_foot = parts[1].split('Footnotes\n')
    references_text = ref_and_foot[0].strip()
    footnotes_text = ref_and_foot[1].strip() if len(ref_and_foot) > 1 else ""

    # Parse footnotes
    footnotes = {}
    for line in footnotes_text.split('\n'):
        if not line.strip(): continue
        match = re.match(r'^(\d+)\.\t(.*)', line)
        if match:
            num = match.group(1)
            # Remove the return arrow if it exists
            text = match.group(2).replace(' ↩', '').strip()
            footnotes[num] = text

    # Parse main text lines
    processed_lines = []
    lines = main_text.split('\n')
    
    # Custom headers
    header_patterns = [
        "I. The Silent Projections",
        "II. The Ancient Engine",
        "III. The Fragile Virtuosity",
        "IV. The Mathematics of Caring",
        "V. The Distributed Mind",
        "VI. The Emergent Polity",
        "VII. The Shape of Wonders to Come",
        "VIII. Beyond the Lights",
        "IX. Coda"
    ]

    for line in lines:
        line = line.strip()
        if not line:
            processed_lines.append("")
            continue
            
        if line == "Blue Sky Visions: On Learning, Longing, and All the Things We Cannot Name":
            continue

        if line in header_patterns:
            processed_lines.append(f"\n## {line}\n")
            continue

        # Check for footnotes at end of words/punctuation (1-24)
        # We need to replace instances like `knowledge.1` with the sidenote.
        # But be careful not to replace numbers in general, only those corresponding to footnotes.
        # We'll use a regex that looks for punctuation followed by digits, or spaces followed by digits at the end of a sentence
        # Actually usually it's `word.1` or `word?9` or `word)10`.
        
        # A simple pass: find all numbers 1-24
        # We can iterate through footnotes in reverse order so 24 matches before 2
        for fn_num in sorted(footnotes.keys(), key=lambda x: int(x), reverse=True):
            fn_text = footnotes[fn_num]
            sidenote_html = f'<sup>{fn_num}</sup><span class="sidenote"><sup>{fn_num}</sup> {fn_text}</span>'
            # Look for that number at the end of a word or sentence.
            # e.g., "knowledge.1" -> "knowledge." + sidenote
            # We use regex \b or punctuation followed by the number
            pattern = r'([a-zA-Z\.\?\!\)\]])' + fn_num + r'(?!\d)'
            line = re.sub(pattern, r'\g<1>' + sidenote_html, line)
            
        processed_lines.append(line)

    # Process References
    ref_lines = [line.strip() for line in references_text.split('\n') if line.strip()]
    ref_html = ['<ol class="references-list">']
    for i, ref in enumerate(ref_lines):
        # We can just output the reference, or try to add ids. We'll simply output the html
        # Extract the key like (Barlow, 1985) roughly to assign id, but it's not strictly necessary.
        ref_html.append(f'<li>{ref}</li>')
    ref_html.append('</ol>')

    # Synthesize new content
    frontmatter = """---
title: "On Learning, Longing, and All the Things We Cannot Name"
date: 2025-01-15
layout: distill
distill: true
series: ["Blue Sky Visions"]
authors:
  - name: "Hanyuan Jiang"
    url: "/"
---
"""
    final_content = frontmatter + "\n" + "\n".join(processed_lines) + "\n\n## References\n\n" + "\n".join(ref_html) + "\n"

    with open('/Users/mikejiang/Documents/GitHub/jianghanyuan.github.io/content/blog/vision/index.md', 'w') as f:
        f.write(final_content)

process()
