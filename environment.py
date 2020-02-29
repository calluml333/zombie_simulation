"""
Module that contains the environment class.
"""

import random
import math
import pygame

class Environment:
    """
    A class that defines the behaviour of the environment that will be used 
    for the simulation.
    """

    def __init__(self, height, width, Human, Zombie, n_humans, n_zombies):
        self._height = height
        self._width = width
        self._n_humans = n_humans
        self._n_zombies = n_zombies
        self._Human = Human
        self._Zombie = Zombie

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) == int or type(value) == float:
            self._height = value
        else:
            raise TypeError("x is required to be either an int or a float")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) == int or type(value) == float:
            self._width = value
        else:
            raise TypeError("y is required to be either an int or a float")
   
    def is_touching(self, agent1, agent2):
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip([agent1.x, agent1.y], [agent2.x, agent2.y])]))
        return  distance < (agent1.size + agent2.size)

    def handle_collisions(self, agents):
        humans, zombies = agents
        new_agent_dicts = []
        for human_id, human in humans.copy().items():
            for other_agents in humans, zombies:
                for other_agent_id, other_agent in other_agents.copy().items():
                    if human != other_agent:
                        
                        if self.is_touching(human, other_agent):
                            sum_agents = human + other_agent
                            if sum_agents:
                                if other_agent_id in list(zombies):
                                    del zombies[other_agent_id]
                                break
                            else:
                                human_pos = human.position
                                if human_id in list(humans):
                                    del humans[human_id]
                                
                                new_Zombie = self._Zombie(self._width, self._height, was_human = True)
                                new_Zombie.position = human_pos
                                new_z_key = max(zombies.keys()) + 1
                                zombies.update({new_z_key: new_Zombie})
                                break
        return humans, zombies

    @staticmethod
    def check_empty_populations(*args):
        for population in args:
            if len(population) == 0:
                pygame.quit()
                quit()

    @staticmethod
    def check_for_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    pass