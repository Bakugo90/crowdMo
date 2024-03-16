# Crowd Behavior Modeling

Welcome to my Python package! I've developed a very simple, yet powerful, tool based on fluid mechanics principles to simulate crowd behavior in various scenarios. Whether it's evacuating a room during an emergency, navigating a crowded corridor, or managing large-scale demonstrations, our model can help you understand and predict crowd dynamics.

## How It Works

Our model uses several parameters to generate a realistic simulation of crowd behavior. These parameters include:

- `Size of a closed area`: The total area that the crowd occupies.
- `Number of people in the area`: The total number of individuals in the crowd.

Based on these parameters, the model calculates the ``Steering Force (fdir)`` and ``Obstacle Avoidance Force (fobs)`` and then generates a simulation that represents crowd behaviour at peak times or in emergency situations.

At the end of the simulation, we can also obtain the ``average evacuation time`` for each individual and the ``average crowd density around obstacles``. These results can be used in civil engineering or architecture to design more effective evacuation plans for public buildings, stadiums or shopping centres.

Please note that this model focuses on logical and precise parameters, rather than unpredictable factors such as fear or panic. This is because in real life, people make decisions based on complex social and psychological factors that are difficult to quantify.


## Visualization

To help you better understand the output of our model,I've included a simple visualization. In the image below, large red dots represent obstacles, while small yellow dots represent individuals in the crowd.

![preview](/screenshot.png)

## Contents

## 1. Acknowledgement
*This project was submitted as an assessment subject for the Phy 330 course (Techniques for simulating physical problems). I would like to express my gratitude to my teacher [PhD BELTAKO](https://scholar.google.com/citations?user=zv1Yy-EAAAAJ&hl=fr) for developing a learning programme that enabled me to learn how to model physical phenomena using Python and for guiding me through the realisation of this project.*

## 2. Installation and test
- Naviguate to ``crowdMo/`` directorie and run:

```
python3 -m pip install -e .
```
- Run the file ``test_simulation.py`` to see what my package can do:

```
python test_simulation.py
```



