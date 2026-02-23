---
title: "Part II: The Cartography of Neural Landscapes"
date: 2026-02-23
layout: distill
distill: true
series: ["Blue Sky Visions"]
authors:
  - name: "Hanyuan Jiang"
    url: "/"
---

As models scale to encompass trillions of parameters, their internal representations cease to resemble neat human categories and increasingly resemble vast, alien landscapes. We wander through these high-dimensional spaces like early explorers mapping an unknown continent, observing phenomena we can barely classify, let alone understand.

## I. Dimensions of Meaning

When we train a language model, we force it to compress the statistical structure of human language into floating-point numbers. The resulting geometry is staggering. Words, concepts, and relationships are encoded as vectors in thousands of dimensions. We intuitively understand three-dimensional space, but a space with 10,000 dimensions possesses mathematical properties that defy our evolutionary intuitions (<a href="#ref-bengio2013">Bengio et al., 2013</a>).

In high-dimensional space, nearly all points are far apart, and the "volume" of the space grows exponentially. Yet, within this vast emptiness, the neural network learns to construct intricate, tightly packed manifolds representing human knowledge. Related concepts cluster together. Analogies appear as parallel vectors. Structure naturally emerges through optimization.<sup>1</sup><span class="sidenote"><sup>1</sup> Deep learning relies heavily on the manifold hypothesis, which suggests that real-world, high-dimensional data actually lies on low-dimensional manifolds embedded within the larger space.</span>

## II. Interrogating the Void

The challenge we face today is not merely building larger spaces, but developing the tools to interrogate them. Mechanistic interpretability aims to reverse-engineer these neural landscapes, identifying the specific circuits and attention heads responsible for particular behaviors (<a href="#ref-olah2020">Olah et al., 2020</a>). 

But there is a lingering fear among researchers: what if the concepts learned by artificial networks cannot be cleanly mapped onto human concepts? What if the network has discovered alien abstractions—features that are entirely predictive and mathematically valid, but fundamentally incomprehensible to the human mind?<sup>2</sup><span class="sidenote"><sup>2</sup> This raises philosophical questions about the limits of human cognition. If a system discovers mathematical truths that we cannot comprehend, can we truly say we understand the system?</span> If so, our cartography will always be an approximation, a projection of an n-dimensional reality down to a 3-dimensional map that our brains can parse.

## References

<ol class="references-list">
<li id="ref-bengio2013">Bengio, Y., Courville, A., & Vincent, P. (2013). <em>Representation Learning: A Review and New Perspectives.</em> IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(8), 1798–1828.</li>
<li id="ref-olah2020">Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., & Carter, S. (2020). <em>Zoom In: An Introduction to Circuits.</em> Distill, 5(3), e00024.001. <a href="https://distill.pub/2020/circuits/zoom-in/" target="_blank">[link]</a></li>
</ol>
