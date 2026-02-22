---
title: "My First Distill-Style Post"
description: "Longform technical note with Distill components"
date: 2026-02-21
slug: "my-first-distill-post"
layout: "distill"
distill: true
math: true
authors:
  - name: "Hanyuan Jiang"
    url: "https://jianghanyuan.github.io"
    affiliation: "CS PhD Program"
  - name: "Collaborator B"
    url: "https://example.org"
    affiliation: "AI Systems Group"
bibliography: "references.bib"
tags: ["distill", "math"]
---

This post mixes regular Markdown with Distill components.

We build on <dt-cite key="vaswani2017attention"></dt-cite> and related work.

This line has a hover footnote <dt-fn>Distill footnotes appear on hover.</dt-fn>.

## A Distill code block

<dt-code block language="python">
def greet(name):
    return f"hello, {name}"
</dt-code>

## Math

MathJax is enabled for this page:

$$
\mathrm{softmax}(x_i)=\frac{e^{x_i}}{\sum_j e^{x_j}}
$$
