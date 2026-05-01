# SPECS OP3 Paper

Working draft for a SPECS conference paper on reproducing and adapting the MuJoCo Playground OP3 joystick locomotion pipeline for the ROBOTIS OP3.

## Build

Use LuaLaTeX and biber:

```bash
latexmk -lualatex main.tex
```

On Overleaf, set:

- Compiler: `LuaLaTeX`
- Bibliography: `biber` if prompted
- Main file: `main.tex`

## Positioning

This is framed as a reproduction, deployment, and sim-to-real fidelity paper. It should not claim a novel RL algorithm. The likely contribution is the engineering audit: what must match between Playground, STRIDE training, ONNX export, ROS 2 deployment, and the measured physical OP3.

## Local Source Notes

Primary local documentation used for the outline:

- `/media/merlin/mujoco/docs/shared/training-pipeline.md`
- `/media/merlin/mujoco/docs/shared/playground-internals.md`
- `/media/merlin/mujoco/docs/shared/observations.md`
- `/media/merlin/mujoco/docs/shared/network-architecture.md`
- `/media/merlin/mujoco/docs/op3/physics-fidelity.md`
- `/media/merlin/mujoco/docs/op3/trajectory-shaping.md`
- `/media/merlin/mujoco/docs/op3/motor-setup-sim-to-real.md`
- `/media/merlin/mujoco/docs/op3/friction-and-domain-randomisation.md`

## Placeholder Authors

Authors are intentionally non-specific placeholders until the final author list and ordering are agreed.
