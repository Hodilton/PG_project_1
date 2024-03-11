import abc

class Simulation(abc.ABC):
    def __init__(self):
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    @abc.abstractmethod
    def add_element(self):
        pass

    @abc.abstractmethod
    def update_elements(self):
        pass

    @abc.abstractmethod
    def draw_elements(self, screen):
        pass

    @abc.abstractmethod
    def draw_info(self, screen):
        pass
