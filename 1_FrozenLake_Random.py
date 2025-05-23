import gymnasium as gym
import random

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")

random.seed(0)

print("## Frozen Lake ##")

action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}
reward = 0
counter = 0
successful_path = []
while reward <1:
    episode_done = False
    state = env.reset(seed=0)

    print("Start state:")
    print(env.render())
    path = []
    counter += 1
    while not episode_done:
        action = random.randint(0, 3)  # choose a random action
        state, reward, episode_done, _, _ = env.step(action)
        print(f"\nAction:{action2string[action]}, new state:{state}, reward:{reward}")
        print(env.render())
        path.append((state, action))
        if reward > 0:
            successful_path = path

print("Counter: {}".format(counter))
#Counter: 170
print("Successful path: {}".format(successful_path))
#Successful path: [(4, 1), (8, 1), (9, 2), (8, 0), (4, 3), (0, 3), (0, 0), (4, 1), (8, 1), (9, 2), (10, 2), (14, 1), (14, 1), (15, 2)]