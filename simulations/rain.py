from components.raindrops import Raindrops
from .simulation import Simulation

class Rain(Simulation):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.colors = [(255, 100, 10), (0, 150, 255), (135, 200, 255)]
        self.shapes = ["circle", "square", "triangle"]

        self.parameters = {'speed': 7, # скорость капель
                           'drops_per_second': 10, # кол-во капель за единицу времени

                           'drop_per_touch': 1, # сколько даёт капля за касание
                           'drops_per_pixel': 1000, # кол-во капель для набора 1 уровня
                           'levels_per_increment': 6, # кол-во добавочных уровней за drops_per_pixel

                           'level_height': 0, # начальное кол-во уровней
                           'landed_count': 0, # не работает :/

                           'max_distance_factor': 1000,
                           'slowdown_factor': 1
                           }


        self.raindrop_simulation = Raindrops(screen_width, screen_height, self.shapes, self.colors, self.parameters)

    def add_element(self):
        if self.paused:
            return

        for _ in range(self.parameters['drops_per_second']):
            self.raindrop_simulation.add_drop()

    def update_elements(self):
        if self.paused:
            return

        self.raindrop_simulation.update_drops()

    def draw_elements(self, screen):
        self.raindrop_simulation.draw_drops(screen)

    def draw_info(self, screen):
        #self.raindrop_simulation.draw_level(screen)
        #self.raindrop_simulation.draw_score(screen)
        pass

    def set_wind_direction(self, mouse_position):
        self.raindrop_simulation.set_wind_direction(mouse_position)
