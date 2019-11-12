import math 
from agent import Agent, Human, Zombie
from environment import Environment


n_humans = 15
n_zombies = 1

WIDTH = 500
HEIGHT = 500

def main():
    env = Environment(HEIGHT, WIDTH, Human, Zombie, n_humans, n_zombies)
    env.generate()


if __name__ == "__main__":
    main()