---
title: "Shaping dynamics through the environment"
created: 2026-11-26
updated: 2026-11-26
type: video
video_id: Uyc5weX460Q
published: 2026-11-24
tags: [#video, #ai-architecture, #basal-cognition, #information-theory]
sources: [raw/transcripts/2026-11-24-Uyc5weX460Q.txt]
---

# Shaping dynamics through the environment

- **Date published:** 2026-11-24
- **Speakers:** Andrea Roli (guest talk to the Levin lab), with discussion with Michael Levin
- **Format:** Guest talk and discussion (56 min)
- **Watch:** https://www.youtube.com/watch?v=Uyc5weX460Q
- **Topics:** [[ai-and-biology|AI and biology]], [[cognition-in-cells|Cognition in cells]], [[control-and-energy|Control and energy]], [[platonic-space-and-ingressing-minds|Platonic space and ingressing minds]]

## In one paragraph

Roli asks how far simple models of gene networks can go as robot controllers. He uses random Boolean networks, Stuart Kauffman's 1969 model of gene regulation, in which each node is on or off and switches according to a rule over a few inputs. With only a light adaptive tweak, these networks learn robot tasks, and in his later experiments he never changes the network at all, only which sensors and motors are wired to which nodes. Networks tuned to the "critical" regime between order and chaos do best. He says he is still puzzled that it is this cheap. Levin connects this to his own question of why some systems give more than was paid for in design, selection or training, and previews unpublished work on gene networks that learn without any change to their parameters.

## Main ideas (plain words)

- Random Boolean networks have an ordered regime (disturbances die out) and a chaotic one (tiny differences blow up), with a critical line between them. He cites work that critical networks match general statistical properties of real cells, and says criticality balances robustness against the ability to produce new behaviour.
- To control a robot, some nodes are overwritten by sensor readings and others drive the motors. Adaptation is an "adaptive walk": make a small random change, keep it if the robot does no worse.
- Offline (design-time) result: networks of 20 and 100 nodes, changing only single entries of the node rules, learned a task where a robot follows light and switches to fleeing it after a clap. He says 10 to 20% of runs produced a working robot, the working networks were robust to noise, and they behaved the same on real robots as in simulation. He says the experiments were made at IRIDIA, where he works now.
- Online (run-time) adaptation is harder because no two trials start from the same state, and the robot can only judge itself with information it can sense. He links it to Pask's electrochemical devices that grew their own sensors and to Ashby, under the idea of "epistemic autonomy": a system shaping its interactions around what matters to it.
- In these runs the network's wiring and rules stay frozen; only the coupling to sensors and motors adapts. With networks up to 1,000 nodes, all runs learned collision avoidance, about 70% learned an object-carrying (foraging) task, and critical networks beat ordered and chaotic ones. The same batch of networks served for different tasks.
- Fault tolerance: a robot with 24 light sensors kept near-normal performance with up to six to nine sensors broken (disconnected, stuck, or noisy). In each fault type there was one level where the damaged robot did better than the intact one; he floats "information overload" as a possible reason and says it needs testing.
- His closing question: can the abstract properties of a task be matched to the dynamical properties of a network? He says it resonates with Levin's Platonic space idea.
- Levin's frame: the "cost of competency". The usual ways to pay for order are design, selection or training; he is interested in cases where you get more than you put in, and says what comes free is not just order but behaviour that behavioural scientists would recognise. Roli agrees it is not free, but says he expected to pay more.
- Levin mentions a preprint (paper to follow) in which biological regulatory networks play video games and some are better at some games than others. He also previews work he says will be out soon from his postdoc Federico Pigozzi: training these networks raises their integration (causal emergence), and forcing them to forget does not undo the gain, a one-way ratchet; random networks are already strongly biased toward this, so evolution had little to do.

## Key quotes (word for word from YouTube's auto-generated captions)

> "investigation of the possibilities of using Boolean networks to control robots."  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=85s

> "critical networks were performing better than ordered and chaotic ones."  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=1720s

> "it might be a signal of the fact that sometimes it is not necessary, not even better to use all the information that is available."  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=1974s

> "I expected to pay more for that."  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=2503s

> "It's not a free lunch. It's a heavily discounted or some sort of subsidized lunch"  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=2611s

> "I think it's really important not to lose our wonder at these things."  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=2682s

> "Our networks are completely frozen. So this is dynamical system learning."  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=3180s

> "It looks to me like the math might be fine tuned too a little bit."  
https://www.youtube.com/watch?v=Uyc5weX460Q&t=3302s


> Source: YouTube auto-generated captions, speakers not labeled; wording is provisional. Timestamps point to the start of the stretch that holds the quote, give or take a few seconds. The first four quotes are Roli; the last four are Levin. The video-game networks work is a preprint by Levin's account; the forgetting/ratchet work is described as not yet out.
