import gym
import numpy as np
import tensorflow as tf

env = gym.make("MsPacman-v0")
env.reset()
img = env.render(mode="rgb_array")
img_arr = np.array(img)
print(img_arr)

def build_model():
    

