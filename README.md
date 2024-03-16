# Crowd behavior modelisation
A simple Python package (based on fluid mechanics) to model the behaviour of crowds at peak times in different situations, such as evacuating a room, moving through a crowded corridor, or managing demonstrations.

This model takes several variables as parameters, such as the `Obstacle avoidance force (obf)size of a closed area`, the ``number of people in the area``, etc., and then generates a simulation that represents the behaviour of the crowd at the exit in an emergency situation or during rush hour. It also generates an ``average evacuation time`` for each individual and the ``average crowd density around obstacles.``
In real life, people make individual decisions based on more complex social and psychological factors. That's why this model focuses only on logical and precise parameters like `Directional force (fdir)` and `Obstacle avoidance force (obf)`, rather than unpredictable factors such as fear or something else.

In the following overview, the large red dots are obstacles and the small yellow dots are people.


## Simple overview

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

