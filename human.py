from agent import Agent


class Human(Agent):
    """
    A subclass  of agent, specifying a "Human" agent and it's behaviour.
    """

    color = (150,150,255) 

    def __init__(self, x_boundary, y_boundary, p_kill, speed=7):
        Agent.__init__(self, x_boundary, y_boundary, speed)
        self.agent_type = 'h'
        self.p_kill = p_kill

    # @property
    # def p_kill(self):
    #     return self._p_kill

    # @p_kill.setter
    # def p_kill(self, value):
    #     self._p_kill = value