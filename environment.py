"""
Module that contains the environment class.
"""

import random
import pygame
import math

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
        self.game_display = pygame.display.set_mode((self._width, self._height))
        self.clock = pygame.time.Clock()   
    
    pygame.display.set_caption("Zombie Outbreak Simulation")

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


    def calc_norm(self, list1, list2):
        diff_list = [a - b for a, b in zip(list1, list2)]
        abs_list = [abs(x) for x in diff_list]
        norm = math.sqrt(sum(abs_list))
        return norm
    
    def is_touching(self, agent1, agent2):
        return self.calc_norm(agent1.position, agent2.position) < (agent1.size + agent2.size)

    def handle_collisions(self, agents):
        humans, zombies = agents
        new_agent_dicts = []
        for human_id, human in humans.copy().items():
            for other_agents in humans, zombies:
                for other_agent_id, other_agent in other_agents.copy().items():
                    if human == other_agent:
                        pass
                    else:
                        if self.is_touching(human, other_agent):
                            # We have a collission
                            pass
        return humans, zombies
                            
    def draw_environment(self, agents):
        self.game_display.fill((255, 255, 255))
        humans, zombies = self.handle_collisions(agents)
        for agent_dict in agents:
            for agent_id in agent_dict:
                agent = agent_dict[agent_id]
                pygame.draw.circle(self.game_display, agent.color, agent.position, agent.size)
                # agent.move()
                agent.check_bounds()

        pygame.display.update()
        return humans, zombies

    def generate(self):
        humans = dict(enumerate([self._Human(self._width, self._height) for i in range(self._n_humans)]))
        zombies = dict(enumerate([self._Zombie(self._width, self._height) for i in range(self._n_zombies)]))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            humans, zombies = self.draw_environment([humans, zombies])
            self.clock.tick(60)


if __name__ == "__main__":
    pass