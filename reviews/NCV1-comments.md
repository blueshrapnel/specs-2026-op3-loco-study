# Nicola's review — NCV1

Source: `specs_2026_op3_loco_study_NCV1.pdf` (48 annotations across 2 pages).

Each entry shows the marked-up text from our manuscript (quoted), followed by Nicola's note. Sorted top-to-bottom by page.


## Abstract / front matter

- **p1 · comment** — “maller”
  > "smaller" than what? Why is it relevant that is small? I see that this becomes clear later but I would suggest to simply remove it here, where it is not clear yet

- **p1 · insertion / replacement** — “t a”
  > robot

- **p1 · suggested deletion** — “using the same joystick command abstraction of forward velocity, lateral velocity, and yaw rate.”
  > too specific information for the abstract (you could re-use it somewhere else in the text; or it could be removed in case you will need to do some pruning for lack of space).
  >
  > Also,

- **p1 · suggested deletion** — “not a new reinforcement-learning algorithm, but”

- **p1 · insertion / replacement** — “.”
  > ", however, differently from these larger robotic platforms, OP3's real-hardware deployment has not being tested yet."
  >
  > which "paper"? I would not mention papers directly in the abstract (with no reference). In few words, remove their mention here.

- **p1 · comment** — “Playground OP3 policy”
  > from the point of view of the reader, what is this? I imagine is the one offered by Mujoco Playground in simulation... but the reader does not know that. So, in case, say it.

- **p1 · comment** — “MJX/Brax PPO training, actuator-order alignment with ROBOTIS motor IDs, ONNX export, ROS 2 policy execution, MuJoCo-to-Webots”
  > there is a list of acronyms here. The problem is that the reader does not know what they stand for. Apart from very obvious ones (e.g., AI), for all acronyms, each time they appear for the first time, you first use the complete work they stand for, add the corresponding acronym in parenthesis (adding the citation to a reference, when meaningful), and only from that point onwards you can use the acronym on it own for the remaining of the paper. 
  >
  > A similar problem is that the reader may not know what they mean even when the full expansion of each letter is provided. For this reason, you should also add a couple of words that define what these words represent. 
  >
  > In few words, what are "MJX", "Brax", "PPO", "ROBOTIS", "ONNX", "ROS 2"?
  > I will not necessarily repeat the same comment for the main text (you need to define them once over all anyway), nor for new acronyms that will come.
  >
  > An alternative would be to remove the highlighted text from the abstract (which according to me would be better than as the text is now) and leave the explanation of what these are in the main text, where you will have more space to do so.

- **p1 · suggested deletion** — “MuJoCo-to-Webots”

- **p1 · insertion / replacement** — “s”
  > preliminary

- **p1 · suggested deletion** — “measurement-driven”

- **p1 · insertion / replacement** — “i”
  > finding

- **p1 · comment** — “simulator contact assumptions”
  > ?

- **p1 · insertion / replacement** — “e”
  > determine

- **p1 · comment** — “into a second simulator or”
  > As we have discussed... This can be confusing if the overall presentation of the paper is not changed. 
  > I would not change it this stage, but I would rather keep the main goal to get the sim-to-real working with the OP3, and the sim to sim as a preliminary testing step towards the achievement of the main sim-to-real goal (this why I have also added the "preliminary" adjective above)


## Motivation

- **p1 · sticky note** — “”
  > add a couple of references to support these two statements

- **p1 · suggested deletion** — “High-throughput”

- **p1 · suggested deletion** — “visually”

- **p1 · comment** — “sam”
  > "same" of what? Same with the physical closed-loop system.
  >
  > I also wonder if it is exactly same that one wants in the general case (since yours sounds like a general statement), because is domain randomization to work these two do not need to be the same, but the simulated policy is actually more general and "contains" the physical one.
  >
  > I was also asking my self whether all this component integrated with each other still constitute a "closed loop system"? probably yes, simply a very complex one, but I am not 100% sure.

- **p1 · comment** — “MuJoCo Playground”
  > what is it? Add a reference here and put the paragraph below (which actually describes it and the reader will then be in a better position to understand what follows) before this sentence.
  >
  > Check also the English of this sentence.

- **p1 · insertion / replacement** — “s”
  > offers

- **p1 · comment** — “implementation”
  > "implementation" of what?

- **p1 · insertion / replacement** — “d”
  > , according to the authors,

- **p1 · insertion / replacement** — “:”
  > performance

- **p1 · comment** — “ros2-control”
  > is the different font used here meant to represent something in particular (which the reader may not know)? E.g. a library? Something related with the code?
  >
  > To be honest I would keep references to code name spaces to the bare minimum. If it was for me I would not include them at all (move them to the Appendix if necessary). But it may be a matter of personal style and experience.

- **p1 · comment** — “ONNX Runtime”
  > ?

- **p1 · insertion / replacement** — “s,”
  > of training

- **p1 · comment** — “estimator”
  > "estimator" of what?

- **p1 · comment** — “The RSS paper”
  > you refer to a paper by the name of its authors, or bib code word, not by the name of the venue it has been disseminated.

- **p1 · insertion / replacement** — “s”
  > "Mujoco"
  >
  > from now onwards, often, you do not mention the "Mujoco" word anymore. In principle it is fine, you simply want to be sure that the reader will not get confused with this.

- **p1 · insertion / replacement** — “n”
  > standard

- **p1 · comment** — “reproducible notebooks, hyperparameters, training curves, and deployment examples”
  > these do not sound relevant to me wrt research, but more for a tutorial or documentation. Some of them are also a bit vague.

- **p1 · insertion / replacement** — “t”
  > one

- **p1 · comment** — “Related frameworks make the same infrastructure question timely”
  > why?

- **p1 · comment** — “robot-learning stacks”
  > is it still about humanoid locomotion?

- **p1 · comment** — “legged-gym”
  > these small case initials are suspicious

- **p1 · comment** — “contextualis”
  > ?

- **p2 · sticky note** — “”
  > probably is obvious already, but consider adding a picture of the physical robot somewhere

- **p2 · suggested deletion** — “of”

- **p2 · insertion / replacement** — “k f”
  > robots

- **p2 · insertion / replacement** — “e”
  > tested for

- **p2 · suggested deletion** — “in the paper or RSS 2025 demo.”
  > You continue to not use proper references.
  >
  >  Anyway, I would remove this anyway here.

- **p2 · insertion / replacement** — “s i”
  > transfer

- **p2 · insertion / replacement** — “S”
  > an interesting

- **p2 · comment** — “obbyist-tier”
  > does this mean something technically relevant to the problem addressed here? Otherwise, I would remove it and simply say "to another...". You could still add in parenthesis "(in our case, a hobbyist tier...)".

- **p2 · suggested deletion** — “are still informative because they”

- **p2 · insertion / replacement** — “y”
  > would

- **p2 · insertion / replacement** — “e”
  > loose

- **p2 · suggested deletion** — “Our goal is deliberately conservative: reproduce the reference walking behaviour, adapt it to a ROBOTIS-ordered STRIDE pipeline, and identify fidelity gaps before making strong hardware claims.”
  > I would remove this.
  >
  > Also, still for the reader, what is "STRIDE"?
