# Dino_AI

Using q-learning AI learn how to play T-rex run, popular game of chrome browser. After millions iteration bot becomes unbeatble.

#  How it works?

With help of convolutional nueral network and q-learning, bot learn how to play this game.Q-learning is a model-less implementation of Reinforcement Learning where a table of Q values is maintained against each state, action taken and the resulting reward.first, PIL capture screen continuously and each frame preprocessed by open cv to transform it to suitable input for CNN.
Output of CNN is highest Q-value. this Q-value decides next action to take.

### Prerequisites

Python 3.6,
Selenium,
OpenCV,
PIL,
Chromium driver for Selenium,
Keras.
