---
title: "Distill Components Demo: Efficient LLM Serving"
description: "Demo post using dt-cite, dt-fn, dt-code, and bibliography support."
date: 2026-02-22
slug: "distill-components-demo"
layout: "distill"
distill: true
math: true
authors:
  - name: "Han Yuan Jiang"
    url: "https://jianghanyuan.github.io"
affiliations:
  - name: "CS PhD Lab"
    url: "https://example.edu"
bibliography: "references.bib"
---

This post demonstrates **real Distill tags** inside Hugo + PaperMod.

Latency-aware batching can improve serving efficiency <dt-cite key="vaswani2017attention"></dt-cite>.

A Distill footnote example <dt-fn>Use this for concise hover explanations.</dt-fn>.

## Distill Code Snippet

<dt-code block language="python">
class Scheduler:
    def score(self, queue_len, token_budget):
        return queue_len / max(token_budget, 1)
</dt-code>

## Equation

$$
\text{throughput} = \frac{\text{tokens}}{\text{second}}
$$
