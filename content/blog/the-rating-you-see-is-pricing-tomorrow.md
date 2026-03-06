---
title: "The Rating You See Is Pricing Tomorrow"
slug: "the-rating-you-see-is-pricing-tomorrow"
aliases: ["/blog/the-third-vision-placeholder/"]
date: 2026-02-26
layout: distill
distill: true
series: ["Blue Sky Visions"]
authors:
  - name: "Hanyuan Jiang"
    url: "/"
image: "/20250801_1510_Chess Pieces Illustration_remix_01k1j7a8kke7wvggmjtgxyhmb5.png"
---


In competitive games like [*League of Legends*](https://en.wikipedia.org/wiki/League_of_Legends) (which I am a big fan of) or [*Valorant*](https://en.wikipedia.org/wiki/Valorant), your visible rank updates after every match. The standard story says that number measures skill. But something 'stranger' happens the moment the same number also determines who you face next, which queues you can enter, and whether your friends can still play with you.

Imagine a new ranked arena with clean outcomes: two players, one match, one rating that rises when you win and falls when you lose. The official explanation sounds familiar. The number tracks your underlying strength. This is the good old [Elo](https://en.wikipedia.org/wiki/Elo_rating_system) dream in modern UI, and recent theory gives that dream real substance by showing that Elo can be understood as a serious online learning rule under a Bradley-Terry-Luce model.<sup>1</sup><span class="sidenote"><sup>1</sup> Olesker-Taylor and Zanetti ([2024](#ref-olesker2024)) analyze Elo through Markov chains and formalize when it tracks latent skill rather than just acting as competitive folklore.</span> Yet the moment the rating also allocates your next opponents and your next set of options, it begins to do more than estimate what you are.

Now place a player one win away from promotion. Crossing the threshold sends them into a sharper queue: stronger opponents, longer waits, lower future win rates, less room to duo with weaker friends, and more stress for roughly the same evening of play. Staying just below the line means easier matches, faster queues, more visible victories, and a more relaxed social experience. Professionals or folk players on Reddit already have names for these situations. They talk about "avoiding Elo hell," dodging promotion traps, farming lower brackets, or even losing on purpose to manipulate a system they suspect is optimizing engagement rather than competitive integrity.<sup>2</sup><span class="sidenote"><sup>2</sup> I would say these folk theories are not pure fantasy. Chen et al. ([2017](#ref-chen2017)) and Wang et al. ([2024](#ref-wang2024)) explicitly study matchmaking systems that optimize engagement objectives, not just skill balance.</span>

The uncomfortable question emerges almost by itself. Should you actually try your hardest to win the next match? The answer depends on more than skill. I will argue that the rating is far more than just a summary of the past, but an allocation rule for the future.

## A Ladder That Allocates Futures

Once a rating determines future opponents, social constraints, prestige, or access to special queues, it stops behaving like a passive measurement device and becomes a device that prices future states of the world. Think of the platform as committing to three linked rules: first, a rating update rule in which wins move you up and losses move you down; second, a matchmaking rule in which your current rating affects the distribution of opponents you face next; and third, a regime rule in which certain rating bands unlock different futures, whether that means harder lobbies, special rewards, altered social options, tournament eligibility, or restrictions on who you can queue with.

Freeze the rest of the ecosystem for a moment. Hold fixed how everyone else behaves. From the perspective of one player inside that temporarily stable environment, the problem is simple: choose effort. High effort costs focus, energy, and emotional strain. Low effort is cheaper, but it reduces the probability of winning.

The key object is the continuation value of rating $r$. Call it $V(r)$: the value of waking up tomorrow with rating $r$. That function compresses everything the current rating buys you in expectation, including opponent quality, queue times, prestige, stress, rewards, and future social possibilities. Once you see the system that way, every rating point becomes a packet of future access. A point upward means one distribution of future worlds. A point downward means another. The ladder is no longer just estimating skill. It is pricing tomorrow.

## The Incentive Condition

Let $M(r^{\prime} \mid r)$ denote the matchmaking distribution. Conditional on your current rating being $r$, it gives the probability of facing an opponent at rating $r^{\prime}$. If your effort level is $a$, your win probability is

$$
q_a(r) = \int P(\text{win} \mid a, r, r^{\prime}) \, dM(r^{\prime} \mid r).
$$

Let $r^+$ be the next rating after a win and $r^-$ the next rating after a loss. In the frozen environment, the value of rating $r$ solves the Bellman equation

$$
V(r) = \max_{a \in \lbrace H, L \rbrace} \left\lbrace q_a(r)\left[u_W(r) + \delta V(r^+)\right] + \left(1 - q_a(r)\right)\left[u_L(r) + \delta V(r^-)\right] - c_a \right\rbrace.
$$

Here $u_W(r)$ and $u_L(r)$ are the immediate utilities from winning and losing, $c_a$ is the effort cost, and $\delta$ discounts the future. The player chooses between high effort $H$ and low effort $L$. Subtract the low-effort payoff from the high-effort payoff and the incentive condition becomes explicit: high effort is optimal exactly when

$$
\left(q_H(r) - q_L(r)\right)
\left[
u_W(r) - u_L(r) + \delta \left(V(r^+) - V(r^-)\right)
\right]
\geq c_H - c_L.
$$

This inequality is the core mechanism. The first term, $q_H(r) - q_L(r)$, measures how much trying harder actually changes your chance of winning. The second term measures what the extra win is worth: immediate satisfaction plus the difference between the future after a win and the future after a loss. If promotion improves tomorrow, the ladder rewards effort. If promotion makes tomorrow worse, the ladder quietly pays you not to try.

## Why Folk Theories Keep Reappearing

The above framework, in fact, unifies a surprising number of player intuitions that otherwise look like isolated complaints. Once the ladder is treated as a continuation-value machine, the familiar stories all collapse into variations on the same logic.

"Elo hell" avoidance appears when $V(r^+) < V(r^-)$. Promotion raises your visible status but moves you into a future with tougher games, lower win rates, and less enjoyable sessions. The formal condition is simple, and so is its implication: the continuation-value gap turns negative, so effort stops looking attractive.

Point-loss exploitation appears when the rating update rule is asymmetric, so the gain from a win is smaller than the loss from a defeat near a threshold. The phenomenon looks quirky from the outside, but the logic is straightforward: players who throw to reset are responding to the implied geometry of state transitions rather than simply behaving irrationally.

Strategic sandbagging is what happens when $V(r^+) < V(r)$. Climbing itself becomes undesirable because higher ratings mean fewer easy wins, more pressure, and worse reward farming. In other words, the value function slopes the wrong way.

Engagement-based matchmaking theories are different in flavor but not in logic. If players believe the platform shifts $M(r^{\prime} \mid r)$ based on recent outcomes to maximize retention, then even deliberate losses can look instrumentally useful because they may move a player into a softer bracket where future win probabilities temporarily rise. Whether those beliefs are accurate or exaggerated, the strategic structure is the same. Our formal model adds to the folk vocabulary by not just saying promotion can feel bad. By identifying the condition under which that feeling becomes strategically rational, it makes the incentive quantitative, shows which levers belong to platform design, and clarifies exactly where the incentive to sandbag changes sign.

## The Measurement Problem

There is a deeper issue here. Once effort becomes endogenous, the rating system also starts corrupting the very data it uses to infer skill.

Suppose the platform thinks it has an accurate estimate of a player's ability. But outcomes reflect ability plus effort, and effort is partly hidden. A strong player deliberately underperforming near a promotion boundary can look observationally identical to a weaker player exerting honest effort. The system sees the same loss either way. The estimator is learning from behavior that its own incentives helped produce.<sup>3</sup><span class="sidenote"><sup>3</sup> This is the old hidden-action problem in a new costume. Holmstrom ([1979](#ref-holmstrom1979)) and Lazear and Rosen ([1981](#ref-lazear1981)) show how outcomes in tournament settings mix skill and effort in ways that make clean inference difficult.</span>

Now this is the real conceptual shift I want to flag. Elo in isolation is an estimator. Elo embedded in a live ranking ecosystem is part of a control system. The estimate affects future allocations, future allocations reshape incentives, incentives alter effort, and effort contaminates the data generating the estimate. Measurement and intervention collapse into one loop. This is also why superficial anti-sandbagging fixes so often fail. If a platform only punishes suspicious losses without changing the continuation-value landscape, players do not stop responding to incentives. They'll just hide the response more carefully.

## Design Implications

The full equilibrium problem is difficult. In reality, every player's strategy affects the rating distribution, and that rating distribution feeds back into each player's continuation value. Solving the entire system requires a fixed point over population behavior, state distributions, and individual responses.<sup>4</sup><span class="sidenote"><sup>4</sup> This is close to a mean-field control problem. Bergemann and Valimaki ([2010](#ref-bergemann2010)) analyze dynamic mechanism design in settings where current allocations reshape future incentives and information.</span> But the local incentive condition already tells us where the pressure points are.

If a platform wants less sandbagging, it can smooth regime discontinuities so that $V(r^+) - V(r^-)$ does not swing sharply at promotion boundaries. It can increase immediate rewards for wins. It can add compensating benefits to higher tiers so promotion is not experienced as a punishment. It can reduce the precision of visible ratings so players cannot optimize continuation values as cleanly. None of these ideas require solving the full equilibrium first. They require understanding that the ladder is a mechanism, not just a ruler.

The practical lesson is surprisingly simple, and this is why I try to maintain an 'informal' narrative throughout. When players throw a game near a threshold, the mystery is not primarily in the player. The mystery is in the Bellman equation the platform has written for them. The ladder is indeed a promise, but what it promises depends on whether climbing makes tomorrow better or worse. Until ranking systems account for how ratings shape futures, how futures shape effort, and how effort reshapes ratings, they should expect players to answer the question the system actually asked, not the one the designer imagined.

## References

<ol class="references-list">
<li id="ref-bergemann2010">Bergemann, D., &amp; Valimaki, J. (2010). The dynamic pivot mechanism. <em>Econometrica</em>.</li>
<li id="ref-chen2017">Chen, Z., Xue, S., Kolen, J., Aghdaie, N., Zaman, K. A., Sun, Y., &amp; Seif El-Nasr, M. (2017). EOMM: An engagement optimized matchmaking framework.</li>
<li id="ref-holmstrom1979">Holmstrom, B. (1979). Moral hazard and observability. <em>The Bell Journal of Economics</em>.</li>
<li id="ref-lazear1981">Lazear, E. P., &amp; Rosen, S. (1981). Rank-order tournaments as optimum labor contracts. <em>Journal of Political Economy</em>.</li>
<li id="ref-olesker2024">Olesker-Taylor, S., &amp; Zanetti, L. (2024). An analysis of Elo rating systems via Markov chains. <em>NeurIPS</em>.</li>
<li id="ref-wang2024">Wang, K., et al. (2024). EnMatch: Matchmaking for better player engagement via neural combinatorial optimization. <em>AAAI</em>.</li>
</ol>
