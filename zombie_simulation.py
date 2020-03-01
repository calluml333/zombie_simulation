import math 
import pygame
import random
from Objects import Human, Zombie, Bat
from Objects import Environment as Env


n_humans = 1
n_zombies = 1
n_bats = 1
WIDTH = 500
HEIGHT = 500
p_kill = 0.7

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()   
pygame.display.set_caption("Zombie Outbreak Game")


def draw_environment(environment, population):
    game_display.fill((0, 0, 0))
    population = environment.handle_collisions(population)
    
    for member_id in population:
        member = population[member_id]

        pygame.draw.circle(game_display, member.color, (member.x, member.y), member.size)
        
        if member.is_type == 'Human' and member.is_player:
            Env.move_human(member)
        
        elif member.is_type == 'Zombie':
            member.hunt_human(population)
            Env.random_move_agent(member)

        elif member.is_type == 'Weapon' and member.picked_up:
            owner = member.owner_id
            member.track_agent(population[owner])

        member.check_bounds()
    pygame.display.update()
    return population

def generate(environment):
    population = create_population(Human, Zombie, Bat)
    while True:
        Env.check_for_exit()
        population = draw_environment(environment, population)
        Env.check_empty_populations(population)
        clock.tick(30)

def create_humans():
    humans = dict(enumerate([Human(WIDTH, HEIGHT, p_kill) for i in range(0, n_humans)]))
    humans[0].is_player = True
    return humans

def create_zombies():
    return dict(enumerate([Zombie(WIDTH, HEIGHT) for i in range(n_zombies)]))

def create_bats():
    return dict(enumerate([Bat(WIDTH, HEIGHT) for i in range(n_zombies)]))

def create_population(*args):
    key_count = 0
    population = {}
    for population_class in args:
        if population_class.is_type == 'Human':
            for i in range(n_humans):
                population[key_count] = population_class(WIDTH, HEIGHT, p_kill)
                if i == 0:
                    population[key_count].is_player = True
                key_count += 1
        
        elif population_class.is_type == 'Zombie':
            for i in range(n_zombies):
                population[key_count] = population_class(WIDTH, HEIGHT)
                key_count += 1
        
        elif population_class.is_type == 'Weapon':
            for i in range(n_bats):
                population[key_count] = population_class(WIDTH, HEIGHT)
                key_count += 1
    return population

def main():
    env = Env(HEIGHT, WIDTH, Human, Zombie, Bat)
    generate(env)


if __name__ == "__main__":
    main()