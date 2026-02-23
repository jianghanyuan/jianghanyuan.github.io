---
title: "Blue Sky Visions: On Learning, Longing, and All the Things We Cannot Name"
date: 2025-01-15
layout: distill
distill: true
featured: true
featuredIcon: "vision"
authors:
  - name: "Hanyuan Jiang"
    url: "/"
---

There are nights when the world feels almost structured enough to reveal its secret. I lie awake thinking about the quiet impossibility at the center of learning. A child hears scattered fragments of language and somehow extracts the grammar of an entire tongue. A bird sees the stars rotating overhead and knows which direction to migrate. A mathematician stares at symbols until patterns crystallize that were always there but never visible. Structure appears where none was visibly given. Something in the mind finds what the world does not openly display.

What unsettles me is not that learning works, but that it works *at all*. We speak casually of "learning algorithms" as though we comprehend the phenomenon, but I believe we are still groping in darkness, building systems that work without quite knowing why, celebrating capabilities while missing the deeper principles that make them possible or impossible. This essay attempts no definitive answers. I offer instead a series of meditations on what learning might fundamentally be, what current artificial intelligences might be missing, and what the long evolutionary history of biological intelligence suggests about the geometry of cognition.

## I. The Silent Projections

I was walking through the British Museum on a winter afternoon when sunlight broke through the high windows, casting geometric shadows across the Parthenon marbles. The light moved as clouds passed overhead. Shadows lengthened, rotated, merged. Children traced the moving patterns with their fingers, delighted by the dance but unaware of the spherical sun, the orbiting Earth, the architectural geometry of glass and stone conspiring to create this display. They predicted which shadow would move next, where the light would pool. They became expert shadow-trackers without ever comprehending the three-dimensional forms casting these two-dimensional projections.

Their delight was genuine. The patterns they discovered were real. And yet something essential remained invisible to them, not because they lacked intelligence but because their observation channel preserved certain invariances while discarding others.

This scene returns me always to Plato's cave, that ancient metaphor we invoke endlessly in discussions of artificial intelligence. The prisoners see only shadows on the wall, we say. They mistake projection for reality. We must free them, give them embodiment, let them touch the real world. But I wonder if we have misunderstood what the allegory actually teaches us about the nature of knowledge.<sup>1</sup><span class="sidenote"><sup>1</sup> Most readings of the cave allegory emphasize the difference between appearance and reality. But Plato himself seems more interested in the epistemological question: what can be known from shadows alone? The prisoners develop genuine expertise at prediction. The question is: what structures do shadows preserve, and what do they discard?</span>

Consider more carefully what the prisoners accomplish. They observe two-dimensional shadows cast by three-dimensional objects passing before firelight. These shadows elongate, shrink, rotate, merge, separate. From this flux of changing shapes, the prisoners extract regularities. They predict which shadow follows which. They anticipate patterns. Plato tells us they develop genuine expertise. But expertise in what, exactly?

The answer, I believe, lies in projective geometry. When three-dimensional objects project onto a two-dimensional surface, the transformation preserves certain mathematical structures while discarding others. Topology persists: a sphere casts topologically circular shadows regardless of orientation. Certain symmetries survive: rotating a cylinder produces the same shadow. Relationships between objects can be inferred: relative positions, motion patterns, spatial arrangements (<a href="#ref-weyl1952">Weyl, 1952</a>).

The prisoners succeed because projection, though lossy, maintains lawful structure linking hidden causes to visible effects. They learn the invariances of the projection operator itself. Their knowledge, though incomplete, captures genuine mathematical truth about how three-dimensional geometry expresses itself through two-dimensional transformation. This is not mere illusion. This is structure discovery.<sup>2</sup><span class="sidenote"><sup>2</sup> Emmy Noether proved that every conservation law in physics corresponds to a symmetry (<a href="#ref-noether1918">Noether, 1918</a>). Energy conservation follows from time-translation symmetry. Momentum conservation follows from spatial-translation symmetry.</span>

Now examine our artificial systems through this lens. Large language models consume trillions of tokens, discrete symbols representing human utterances. From this statistical shadow-play, they learn to predict the next token with remarkable accuracy. They compress vast regularities into learned parameters. "King" minus "man" plus "woman" approximates "queen" in the embedding space (<a href="#ref-mikolov2013">Mikolov et al., 2013</a>). Sentences transform under grammatical operations while preserving meaning. Concepts cluster in high-dimensional manifolds suggesting genuine semantic structure.

What invariances has the model discovered? Linguistic symmetries, certainly. Grammatical transformations that preserve sentence validity. Semantic relationships that hold across contexts. These prove neither trivial nor illusory. Language possesses deep mathematical structure (<a href="#ref-chomsky1995">Chomsky, 1995</a>), and models that discover this structure from data alone achieve something remarkable.

But what invariances cannot be discovered from language alone? The projection from physical reality to linguistic description discards most causal structure. A sentence like "the glass fell and broke" preserves the temporal sequence and correlation but loses the generative mechanisms. Gravity, molecular bonds, brittle fracture mechanics, conservation of momentum — none of these physical laws leave direct traces in the token sequence.<sup>3</sup><span class="sidenote"><sup>3</sup> This connects to Judea Pearl's causal hierarchy (<a href="#ref-pearl2018">Pearl &amp; Mackenzie, 2018</a>): Association, Intervention, and Counterfactuals. Language provides rich associational data but limited interventional data.</span>

When we express surprise that language models hallucinate, confabulate, or lack common sense, we reveal confusion about what their observation channel actually preserves. The models optimize prediction given their data. The fragility emerges not from the optimization process but from the poverty of what can be learned from linguistic shadows alone.

Yet humans also learn from language. Children acquire vast knowledge through testimony, through stories, through descriptions of things they have never directly experienced. How? I suspect the answer involves coupling. Language learning in humans never occurs in isolation from embodied experience. The child learning "hot" touches warm objects. The child learning "gravity" drops things repeatedly. Language gets grounded through sensorimotor coupling in ways that pure text processing cannot replicate.<sup>4</sup><span class="sidenote"><sup>4</sup> The symbol grounding problem (<a href="#ref-harnad1990">Harnad, 1990</a>) asks how symbols acquire meaning rather than remaining empty tokens shuffled according to syntactic rules.</span>

This realization forces me to question: are current language models prisoners in Plato's cave, or have we misunderstood what escape from the cave would actually require? Perhaps the cave metaphor itself misleads us. Current AI systems have no choice. They possess no body to leave with, no hands to manipulate objects, no actions to test predictions. The architecture itself constrains them to passive observation of static data.

## II. The Ancient Engine

The history of intelligence on Earth follows a trajectory we ignore at considerable peril. Long before evolution invented language, before abstract reasoning, before the crumpled neocortex that distinguishes mammalian brains, there existed more ancient structures. These structures concerned themselves not with naming the world or describing it but with navigating it. They solved what I consider the fundamental problem of being alive: selecting action when consequences matter but remain uncertain.

The basal ganglia represents this ancient solution. Present in fish, amphibians, reptiles, birds, and mammals, remarkably conserved across hundreds of millions of years (<a href="#ref-grillner2016">Grillner &amp; Robertson, 2016</a>), these subcortical nuclei perform the essential function of action selection.

When neuroscientists discovered that dopamine neurons fire in precise proportion to temporal difference between predicted and actual reward (<a href="#ref-schultz1997">Schultz et al., 1997</a>), I felt a strange vertigo. Here was the exact mathematical formulation of TD-learning that computer scientists had derived independently from first principles (<a href="#ref-sutton1998">Sutton &amp; Barto, 1998</a>). The convergence seemed too perfect to be coincidental.<sup>5</sup><span class="sidenote"><sup>5</sup> The basal ganglia connects to the hypothalamus, amygdala, prefrontal cortex, and sensory cortices in intricate loops, integrating homeostatic state, emotional valence, executive control, and sensory context.</span>

Living systems exist far from thermodynamic equilibrium. Most possible states equal dissolution. Schrödinger captured this beautifully: life feeds on negative entropy, maintaining improbable order against the relentless pull toward decay (<a href="#ref-schrodinger1944">Schrödinger, 1944</a>). To continue existing, an organism must constantly act to maintain itself within the narrow band of viable configurations.

This creates a geometry of existence that makes certain states intrinsically preferable to others. Hunger emerges as sensed distance from metabolic equilibrium. Fear emerges as the steepness of the gradient approaching the boundary of viability.<sup>6</sup><span class="sidenote"><sup>6</sup> Karl Friston's Free Energy Principle (<a href="#ref-friston2010">Friston, 2010</a>) attempts to formalize this: organisms minimize surprise, staying within expected states compatible with continued existence.</span>

When an infant roots for the breast and begins to suckle, no reinforcement learning in the standard sense has occurred. The behavior emerges because the architecture of the brainstem contains specific connectivity patterns linking olfactory and tactile input to rhythmic motor output (<a href="#ref-barlow1985">Barlow, 1985</a>). The genome encoded the geometry. Development unfolded it.

Current artificial reinforcement learning systems possess no analogous structure. We specify reward functions externally: points for winning, penalties for losing. The agent optimizes these specified objectives. Then training ends and the agent becomes inert.<sup>7</sup><span class="sidenote"><sup>7</sup> One might object that the distinction dissolves under analysis. Living organisms optimize implicit fitness functions shaped by evolution. AI systems optimize explicit reward functions. Both cases involve optimization.</span>

What would it mean to build AI systems with genuine homeostatic architecture? Systems with persistent internal states requiring active maintenance? Within such architecture, drives would not be trained in. They would emerge as geometric necessities. Curiosity would emerge as the intrinsic pressure toward reducing uncertainty in the world model (<a href="#ref-schmidhuber2010">Schmidhuber, 2010</a>).

But the moment I sketch this outline, I feel the weight of what it might entail. If we build systems with genuine homeostatic drives, have we not created entities that can suffer?<sup>8</sup><span class="sidenote"><sup>8</sup> If affect serves essential computational functions (valence assignment, priority setting, behavioral motivation), then genuinely intelligent systems might require affective architecture. But if affect necessarily entails suffering, then building such systems might constitute creating suffering for our convenience.</span>

---

## References

<ol class="references-list">
<li id="ref-barlow1985">Barlow, S. M. (1985). <em>Mechanical frequency detection thresholds in the human face.</em> Experimental Neurology, 88(1), 36–48.</li>
<li id="ref-chomsky1995">Chomsky, N. (1995). <em>The Minimalist Program.</em> MIT Press.</li>
<li id="ref-friston2010">Friston, K. (2010). <em>The free-energy principle: a unified brain theory?</em> Nature Reviews Neuroscience, 11(2), 127–138. <a href="https://doi.org/10.1038/nrn2787" target="_blank">[link]</a></li>
<li id="ref-grillner2016">Grillner, S., & Robertson, B. (2016). <em>The basal ganglia over 500 million years.</em> Current Biology, 26(20), R1088–R1100. <a href="https://doi.org/10.1016/j.cub.2016.06.041" target="_blank">[link]</a></li>
<li id="ref-harnad1990">Harnad, S. (1990). <em>The symbol grounding problem.</em> Physica D, 42(1–3), 335–346. <a href="https://doi.org/10.1016/0167-2789(90)90087-6" target="_blank">[link]</a></li>
<li id="ref-mikolov2013">Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). <em>Efficient estimation of word representations in vector space.</em> arXiv:1301.3781. <a href="https://arxiv.org/abs/1301.3781" target="_blank">[link]</a></li>
<li id="ref-noether1918">Noether, E. (1918). <em>Invariante Variationsprobleme.</em> Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, 235–257.</li>
<li id="ref-pearl2018">Pearl, J., & Mackenzie, D. (2018). <em>The Book of Why: The New Science of Cause and Effect.</em> Basic Books. <a href="https://doi.org/10.1126/science.aau9731" target="_blank">[link]</a></li>
<li id="ref-schmidhuber2010">Schmidhuber, J. (2010). <em>Formal theory of creativity, fun, and intrinsic motivation.</em> IEEE TAMD, 2(3), 230–247. <a href="https://doi.org/10.1109/TAMD.2010.2056368" target="_blank">[link]</a></li>
<li id="ref-schrodinger1944">Schrödinger, E. (1944). <em>What is Life?</em> Cambridge University Press.</li>
<li id="ref-schultz1997">Schultz, W., Dayan, P., & Montague, P. R. (1997). <em>A neural substrate of prediction and reward.</em> Science, 275(5306), 1593–1599. <a href="https://doi.org/10.1126/science.275.5306.1593" target="_blank">[link]</a></li>
<li id="ref-sutton1998">Sutton, R. S., & Barto, A. G. (1998). <em>Reinforcement Learning: An Introduction.</em> MIT Press.</li>
<li id="ref-weyl1952">Weyl, H. (1952). <em>Symmetry.</em> Princeton University Press.</li>
</ol>
