# Han Yuan Jiang - Personal Website

This repository is a Hugo site using PaperMod, with optional Distill-style post pages.

## Local setup

1. Install Hugo (extended).
2. Run:

```bash
hugo server -D
```

## Distill-enabled posts

Use a leaf bundle and set:

```yaml
layout: distill
distill: true
math: true
```

Example: `content/posts/my-distill-post/index.md`.
