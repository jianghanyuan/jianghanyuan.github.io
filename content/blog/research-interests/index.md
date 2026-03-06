---
title: "Research Interests"
description: "From efficient inference to reliable deployment — building the systems that power modern AI."
date: 2026-02-22
slug: "research-interests"
layout: "distill"
distill: true
math: true
authors:
  - name: "Hanyuan Jiang"
    url: "https://jianghanyuan.github.io"
    affiliation: ""
tags: ["research", "systems", "llm"]
image: "/20250802_2319_Intersecting Squares Design_remix_01k1nnmkwdftnvqeyzwk3970da-modified.png"
featured: true
featuredIcon: "research"
---

## The Systems Behind Intelligence

Modern AI is not just about better models — it is about the **systems** that make those models useful. Every breakthrough in model architecture eventually meets the same question: *how do we deploy this at scale, reliably, and efficiently?*

My research lives at this intersection. I study how to build the infrastructure that bridges the gap between a trained model and a production service that millions of people depend on.

## Efficient LLM Serving

Large language models are extraordinarily expensive to run. A single inference request can consume gigabytes of GPU memory and milliseconds of precious compute. When you multiply this by millions of concurrent users, the engineering challenge becomes immense.

I work on **scheduling algorithms** that intelligently batch and prioritize requests to maximize throughput while meeting strict latency targets. The key insight is that not all requests are equal — some are short and urgent, others are long and tolerant of delay. By understanding this structure, we can serve significantly more users with the same hardware.

### Key Questions

- How do we schedule heterogeneous requests on shared GPU clusters?
- Can we predict request complexity before execution begins?
- What is the theoretical throughput limit for a given model and hardware configuration?

## Training-Serving Co-Design

Traditionally, training and serving are treated as separate problems. You train a model, freeze the weights, and hand them to a different team to deploy. But this separation leaves performance on the table.

I explore **co-design** approaches where the training process is aware of deployment constraints. For example:

- Training with quantization-aware methods that produce models naturally suited for efficient inference
- Architecture modifications that trade a small amount of accuracy for significant serving speedups
- Distillation pipelines that produce smaller, faster models tailored to specific deployment targets

## Reliability and Safety

A model that is fast but unreliable is worse than useless — it is dangerous. My work on reliability focuses on:

- **Monitoring**: How do we detect when a model is producing low-quality or harmful outputs in real time?
- **Evaluation**: How do we build comprehensive test suites that capture the full range of model behavior?
- **Graceful degradation**: How should a system behave when it encounters inputs outside its training distribution?

These questions are not purely academic. Every production AI system faces them daily, and the answers have real consequences for the people who rely on these systems.

## Looking Forward

The next generation of AI systems will be **agentic** — they will plan, act, and learn from their environment. Building reliable infrastructure for these systems is an open and urgent challenge. I am particularly excited about:

- Long-horizon planning under uncertainty
- Multi-agent coordination and resource allocation
- Safety guarantees for autonomous systems

The systems we build today will determine what kind of AI is possible tomorrow.
