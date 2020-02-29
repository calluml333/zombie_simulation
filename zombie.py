from agent import Agent


class Zombie(Agent):
    """
    A subclass  of agent, specifying a "Zombie" agent and it's behaviour.
    """
    
    color = (255,0,0)

    def __init__(self, x_boundary, y_boundary, speed=1, was_human=False):
        Agent.__init__(self, x_boundary, y_boundary, speed)
        self.agent_type = 'z'
        self.was_human = was_human

    def hunt_human(self, human_dict):
        nearest_human = self.find_nearest_human(human_dict)
        if nearest_human:
            self.move_towards_agent(nearest_human)