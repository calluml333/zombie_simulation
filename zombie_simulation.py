import math 
import pygame
import random
from agent import Agent, Human, Zombie
from environment import Environment


n_humans = 1
n_zombies = 1
WIDTH = 500
HEIGHT = 500
p_kill = 0.1

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()   
pygame.display.set_caption("Zombie Outbreak Simulation")


def draw_environment(environment, agents):
    game_display.fill((0, 0, 0))
    humans, zombies = environment.handle_collisions(agents)
    
    for zombie_id in zombies:
        zombie = zombies[zombie_id]
        zombie.hunt_human(humans)
    
    for agent_dict in agents:
        for agent_id in agent_dict:
            agent = agent_dict[agent_id]
            pygame.draw.circle(game_display, agent.color, (agent.x, agent.y), agent.size)
            
            if agent.agent_type != 'z':
                # TODO: Create logic that will move the human agents
                pass
                
            agent.check_bounds()
    pygame.display.update()
    return humans, zombies

def generate(environment):
    humans = dict(enumerate([Human(WIDTH, HEIGHT, p_kill) for i in range(n_humans)]))
    zombies = dict(enumerate([Zombie(WIDTH, HEIGHT) for i in range(n_zombies)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        humans, zombies = draw_environment(environment, [humans, zombies])
        clock.tick(60)

def main():
    env = Environment(HEIGHT, WIDTH, Human, Zombie, n_humans, n_zombies)
    generate(env)


if __name__ == "__main__":
    main()