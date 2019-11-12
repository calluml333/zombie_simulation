import math 
from agent import Agent, Human, Zombie
from environment import Environment


n_humans = 15
n_zombies = 1

WIDTH = 800
HEIGHT = 600

def main():
    env = Environment(HEIGHT, WIDTH, Human, Zombie, n_humans, n_zombies)
    env.generate()


def calc_norm(list1, list2):
    diff_list = [a + b for a, b in zip(list1, list2)]
    abs_list = [abs(x) for x in diff_list]
    print(abs_list)
    norm = math.sqrt(sum(abs_list))
    return norm



if __name__ == "__main__":
    main()