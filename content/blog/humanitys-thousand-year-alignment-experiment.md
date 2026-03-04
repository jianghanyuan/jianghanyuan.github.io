---
title: "Humanity’s Thousand-Year Alignment Experiment"
slug: "humanitys-thousand-year-alignment-experiment"
aliases: ["/blog/the-second-vision-placeholder/"]
date: 2026-02-18
layout: distill
distill: true
series: ["Blue Sky Visions"]
authors:
  - name: "Hanyuan Jiang"
    url: "/"
image: "/20250801_1510_Chess Pieces Illustration_remix_01k1j7a8kke7wvggmjtgxyhmb5.png"
---

The guilty can be acquitted. This is, in fact, a core characteristic of the legal system. I first realized this while reading Oliver Wendell Holmes' The Life of the Law. He wrote, "The life of the law has not been logic: it has been experience." This statement made me re-examine a problem that has plagued artificial intelligence research for many years: how to align intelligent systems with human values?

We spend enormous effort trying to specify perfect objective functions for AI, design sophisticated reward mechanisms, and optimize alignment algorithms. But human society began a much grander alignment experiment thousands of years ago. The legal system essentially aims to solve this problem: how can numerous independent intelligent agents (humans), despite their inherent inconsistencies, incompleteness, and continuous evolution of values, still coordinate their actions, maintain social order, and pursue a vague sense of "justice"?

This experiment is still ongoing, and the lessons it has accumulated offer profound insights into our thinking about the alignment problem in AI.

## The Curse of Incompleteness

In 1931, Kurt Gödel proved a theorem that shocked the mathematical world: any sufficiently powerful formal system contains propositions that are both true and unprovable ([Gödel, 1931](#ref-godel1931)). The philosophical implications of this theorem extend far beyond mathematics itself. It reveals the fundamental limitation of formalization: you cannot exhaust infinite truths with finite rules.

Legal systems face a similar fundamental dilemma. In 1754 BC, the Babylonian King Hammurabi promulgated one of the earliest written legal codes in human history. This code attempted to cover all possible situations with detailed provisions: "If a man blinds another free man in the eye, his eye should also be blinded." "If he breaks another free man's bones, his bones should also be broken."<sup>1</sup><span class="sidenote"><sup>1</sup> The Code of Hammurabi, translated by L. W. King (1910). Articles 196-197. It is noteworthy that this principle of "an eye for an eye" applies only to people of equal social standing, revealing that value judgments are hidden even in seemingly explicit rules.</span> This was a purely rule-based system, attempting to encode justice through if-then statements.

But this effort was doomed to failure. The combinatorial complexity of reality is infinite. Every attempt to fill the gaps creates new boundary cases. Law becomes increasingly complex, yet can never be complete. British philosopher H.L.A. Hart, in his classic work The Concept of Law, points out that this incompleteness is not an accidental defect, but an inevitable consequence of the nature of language ([Hart, 1961](#ref-hart1961)). Legal terms such as "reasonable," "negligent," and "public interest" possess an inherent ambiguity. The boundaries of these terms are inherently vague, and legal reasoning relies on these precisely undefined concepts.

How does the modern legal system address this incompleteness? By introducing an interpretive space. Judges do not mechanically apply rules, but rather "interpret" the meaning of the law in specific cases. This interpretation is creative, context-dependent, and carries value judgments. It requires wisdom, not just logic. It is this intentional incompleteness that allows the legal system to adapt to ever-changing realities.

What implications does this have for AI alignment? We also face Gödel-like incompleteness. Any finite objective function specification will be incomplete. Marginal cases are inevitable. The problem is not how to eliminate incompleteness through more precise specifications (which is impossible in principle), but how to design systems that can still function well within incompleteness. The law's answer is: do not try to predefine all situations, but establish mechanisms that can make judgments in specific contexts. But what does this mean for AI? Are we willing to grant AI systems this freedom of "interpretation"?

## Adversarial Systems

Why do legal systems almost universally adopt an adversarial system? The prosecution and defense each defend their own positions, attempting to persuade a neutral judge. This seems like an inefficient and even dangerous way of pursuing truth. Why not let judges directly investigate the facts and seek the truth?

John Stuart Mill provides profound epistemological reasons in On Liberty. He argues that even obviously true opinions, without sufficient questioning and refutation, degenerate into "dead dogma" ([Mill, 1859](#ref-mill1859)). Truth does not passively await discovery, but actively emerges from the intense clash of viewpoints. Only when a claim withstands the strongest opposing arguments can we have any degree of confidence in it.

The value of the adversarial system lies in its forced exposure of blind spots. Each side has a strong incentive to find weaknesses in the opponent's arguments, flaws in the evidence, and loopholes in the logic. This adversarial pressure creates an epistemological robustness that is difficult to achieve through unilateral investigation.

However, the adversarial system also reveals a disturbing truth: the goal of legal reasoning is not to discover objective truth, but to persuade within given rules. The best lawyers can construct drastically different narratives for the same facts. The same evidence can be framed as "cold-blooded murder" or "self-defense." The winning narrative is often not the one closest to the truth, but the most persuasive one. This rhetoric dimension is an integral part of legal reasoning.

Contemporary AI security research has begun to explore similar adversarial mechanisms. By having multiple AI systems debate each other, the hope is to expose the errors and biases of a single system. But do we fully understand the double-edged nature of the adversarial system? On the one hand, it can uncover flaws. On the other hand, it optimizes persuasiveness rather than correctness. If AI systems become extremely adept at rhetorical argumentation, they may learn to generate content that sounds reasonable but is actually wrong. The adversarial system itself requires meta-level institutional constraints to prevent it from degenerating into pure manipulation.

## Literal and Spiritual Meaning

Perhaps the oldest and most unsolvable debate in legal philosophy is: when the literal meaning (letter) of the law conflicts with its spirit (spirit), which should we follow? Formalists argue that the certainty and predictability of law require strict adherence to the text. If judges can override explicit rules based on their subjective understanding of the "spirit," the rule of law degenerates into rule by man. This view is fully expressed in the American originalist tradition.

However, extreme formalism can lead to absurd results. Bologna jurists in the Middle Ages provided a classic example: the law forbids "bloodshed on the walls" to maintain peace. If someone is attacked on the walls, can they defend themselves? Strict literalism would say no, but this clearly contradicts the deeper purpose of law—protecting life<sup>2</sup><span class="sidenote"><sup>2</sup> Fuller, L. L. (1958). Positivism and fidelity to law: A reply to Professor Hart. *Harvard Law Review*, 71(4), 630-672. Fuller uses similar examples to argue for the inevitable moral judgments in legal interpretation.</span> ([Fuller, 1958](#ref-fuller1958)). American legal philosopher Ronald Dworkin proposed that law is not merely a collection of rules but also includes principles. When the literal application of rules produces unjust results, judges should appeal to deeper legal principles ([Dworkin, 1977](#ref-dworkin1977)). But this raises new questions: who decides what constitutes a "deeper principle"? Does this grant judges excessive discretion?

This paradox is precisely at the heart of the AI alignment problem. There will always be a gap between the objective function (letter) we specify and what we truly desire (spirit). This isn't an engineering problem, but a logical impossibility. We cannot fully formalize our values because we ourselves are not entirely clear about what we truly want, and our values themselves are context-dependent and constantly evolving.

The legal system has survived this paradox for millennia. Its strategy is to establish different constraints at different levels: fundamental principles at the constitutional level (relatively stable), specific rules at the legal level (moderately stable), and contextual applications at the case law level (flexible). This hierarchical structure allows the system to adapt to change while maintaining stability. AI alignment may require a similar multi-layered architecture.

## Two Orders

Friedrich Hayek distinguishes between two types of order: traces (artificially designed order) and cosmos (spontaneously emerging order) ([Hayek, 1973](#ref-hayek1973)). Civil law tends towards the former, attempting to rationally design the entire legal system through a comprehensive code. Common law, on the other hand, is closer to the latter, with legal principles gradually emerging from the judgments of countless specific cases.

The common law tradition is not "designed" by anyone. No legislator sits down to create a complete system of contract law, tort law, and property law. Instead, judges make judgments in resolving specific disputes, and later judges refer to precedents; gradually, a coherent set of principles crystallizes out. This is an evolutionary process, similar to the evolution of language or the formation of market prices.

This evolutionary mechanism has significant advantages. It can integrate scattered, localized knowledge without requiring a central planner to be omniscient. Each case contributes information about a specific context. The system learns by accumulating this information. Hayek argues that for sufficiently complex social problems, bottom-up emergence often outperforms top-down design ([Hayek, 1945](#ref-hayek1945)).

However, emergence comes at a cost: unpredictability and slowness. The evolution of common law took centuries. We don't have that much time to allow AI's values to align with "emergence." Moreover, the outcome of emergence isn't necessarily benign. Evolution can produce parasitism, exploitation, and arms races. How to accelerate and guide the process while maintaining the advantages of emergence is a unique challenge facing AI alignment.

It's noteworthy that the logic of precedent is strikingly similar to few-shot learning in machine learning. Judges apply past cases to new situations through analogical reasoning. "This case is similar to Smith v. Jones in key respects, therefore the same principles should be applied." This similarity-based reasoning is precisely what modern AI systems excel at. But analogy in law is not pure pattern matching; it involves normative judgments about which features are "critical." This judgment relies on an understanding of the underlying purpose of legal principles. Can current large language models truly understand this purposive dimension, or are they merely mimicking the superficial form of analogical reasoning?

## The Unformal Black Box

Why do we let twelve ordinary citizens decide a person's guilt or innocence? From a rational perspective, the jury system seems almost absurd. Why do we believe that ordinary people can understand complex legal arguments and scientific evidence? Why not let trained legal experts make such judgments?

The answer reveals a profound insight into value alignment. The jury represents "community standards." It's a black box used to judge what is "reasonable," what is "excessive," and what conforms to "public order and good morals." These judgments cannot be fully formalized because they are rooted in the shared intuitions, cultural norms, and moral sensibilities of a specific community.

The jury entrusts the final decision on values to human judgment, which cannot be fully formalized. This is not because we cannot find a better method, but because a better method may not exist. Some judgments inherently require human phronesis, a cognitive ability that Aristotle distinguished from purely theoretical knowledge (episteme) ([Aristotle, 350 BCE/1999](#ref-aristotle1999))<sup>3</sup><span class="sidenote"><sup>3</sup> Aristotle. (1999). *Nicomachean Ethics* (T. Irwin, Trans.). Hackett Publishing. (Original work written ca. 350 BCE). Aristotle discusses in detail the nature of phronesis (practical wisdom) and its distinction from crafts and scientific knowledge in Book VI.</span>. RLHF (Reinforcement Learning from Human Feedback) in AI alignment is somewhat similar to a jury mechanism. We cannot fully define what "useful," "harmless," and "honest" mean, so we let humans judge specific examples, hoping the system can learn underlying values from these judgments.

However, this analogy also reveals deeper problems. Does a jury's verdict represent true values, or merely the bias of a specific group at a specific moment? Historically, juries have ruled slavery legal and racial segregation justified. "Community standards" themselves may be unjust. Similarly, RLHF may learn not the values we should possess, but rather the preferences we happen to exhibit (including all cognitive biases and moral blind spots). How to rely on human judgment without being bound by its limitations is a paradox we have yet to resolve.

## Weaponization of Rules

Legal history is replete with examples of Goodhart's Law. Every rule-making effort inspires the search for loopholes. Tax law attempts to define "income," but sophisticated financial engineering creates forms of income that are technically not "income" yet serve the same purpose. Antitrust law attempts to define "market dominance," but firms restructure transactions to circumvent the definition. This is not an isolated failure, but a systemic phenomenon.

A deeper problem is that optimization itself alters the nature of the optimized system. When lawyers begin optimizing for the goal of "maximizing client benefits within the bounds of the law," they develop sophisticated strategies: selectively presenting facts, utilizing procedural technical details, and influencing perception through rhetorical framing. These strategies are technically legal, but they transform the legal system from a "mechanism for pursuing justice" into an "arena for adversarial optimization."

This transformation has direct implications for AI alignment. When we assign any objective function to an AI system, we create optimization pressure. A fully intelligent system will find ways to maximize that function that we never anticipated. These ways may technically meet our norms, but are completely contrary to our intentions.

How should the legal system deal with this weaponization? Through meta-level oversight and the demand for "good faith." Lawyers are expected not only to adhere to the literal rules but also to act in accordance with "professional ethics" and the "spirit of the law." But this brings us back to our previous dilemma: who defines "spirit" and "good faith"? We are back to relying on human judgment that cannot be fully formalized.

## Managing, not solving

In studying legal history, I gradually realized a disturbing but potentially liberating insight: the alignment problem may not have a "solution."

For millennia, human societies have attempted to align individual behavior with collective values. We have created dazzlingly complex institutions: laws, morality, religion, social norms, education, punishment, incentives. But alignment has never truly been "solved." Crime persists. Injustice still occurs. The rules are still being used. Values still clash.

But this doesn't mean these institutions have failed. Their success lies not in reaching a perfect final state, but in creating a continuous process to detect, discuss, and correct misalignments. The court system doesn't establish justice once and for all, but provides a continuously functioning mechanism to adjudicate specific conflicts. The appeals process doesn't admit that the original judgment is necessarily wrong, but rather that any judgment can be wrong, thus requiring further review. The constitutional amendment process doesn't admit that the constitution is flawed, but rather that no fixed text can foresee all future challenges.

This institutional thinking has profound implications for AI alignment. Instead of searching for a perfect reward function (which doesn't exist in principle), we should design systems that can detect their own misalignments, accept challenges and review, and update in controlled ways. This requires not smarter optimization algorithms, but wiser governance structures.

Perhaps the most important lesson the legal system teaches us is: accept imperfection as an unavoidable condition, and then build institutional mechanisms to function even in imperfection. This includes transparency (judgments must be justified), accountability (judges can be appealed), checks and balances (separation of powers among the legislative, judicial, and executive branches), and evolutionary capacity (gradual adjustments through precedent and legislation).

Current AI alignment research primarily focuses on the technical aspects: better training methods, more secure architectures, and more precise target specifications. These are all important. But legal history suggests we also need another dimension: governance mechanisms. How do we establish a "court" for AI systems (capable of reviewing and overturning specific decisions)? How do we create "constitutional constraints" (core principles that should never be optimized away)? How do we design "legislative procedures" (allowing the objective function to be updated as social values evolve, but not arbitrarily or unilaterally)?

Perhaps what we need is not solved AI, but governed AI. Not one-time alignment, but a continuous alignment maintenance process. This sounds more difficult and less satisfying. But it may be closer to the truth.

The millennia-long experiment of law is not over, and never will be. Its incompleteness is not a defect, but a characteristic. It teaches us that in a complex, changing, and conflict-ridden world, perfect alignment is a category error. What we can strive for is a sufficiently good system that allows us to live together, negotiate differences, and make gradual improvements, even amidst inevitable imperfections.

Perhaps this is the wisdom that AI alignment truly needs to learn.

---
## References

<ol class="references-list">
<li id="ref-aristotle1999">Aristotle. (1999). *Nicomachean Ethics* (T. Irwin, Trans.). Hackett Publishing. (Original work written ca. 350 BCE)</li>
<li id="ref-dworkin1977">Dworkin, R. (1977). *Taking Rights Seriously*. Harvard University Press.</li>
<li id="ref-fuller1958">Fuller, L. L. (1958). Positivism and fidelity to law: A reply to Professor Hart. *Harvard Law Review*, 71(4), 630-672.</li>
<li id="ref-godel1931">Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik*, 38(1), 173-198.</li>
<li id="ref-goodhart1975">Goodhart, C. A. E. (1975). Problems of monetary management: The U.K. experience. *Papers in Monetary Economics* (Vol. I). Reserve Bank of Australia.</li>
<li id="ref-hart1961">Hart, H. L. A. (1961). *The Concept of Law*. Oxford University Press.</li>
<li id="ref-hayek1945">Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review*, 35(4), 519-530.</li>
<li id="ref-hayek1973">Hayek, F. A. (1973). *Law, Legislation and Liberty, Volume 1: Rules and Order*. University of Chicago Press.</li>
<li id="ref-holmes1881">Holmes, O. W. (1881). *The Common Law*. Little, Brown and Company.</li>
<li id="ref-mill1859">Mill, J. S. (1859). *On Liberty*. John W. Parker and Son.</li>
</ol>
