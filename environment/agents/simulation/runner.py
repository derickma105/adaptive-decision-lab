from environment.factory_env import FactoryEnv
from agents.random_agent import RandomAgent

env = FactoryEnv()
agent = RandomAgent()

rewards = []

for step in range(50):
    action = agent.select_action()
    reward = env.step(action)
    rewards.append(reward)

print("Average reward:", sum(rewards)/len(rewards))
