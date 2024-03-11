import pygame
import random

class Raindrops:
    def __init__(self, screen_width, screen_height, shapes, colors, parameters):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.drops = []

        self.shapes = shapes
        self.colors = colors
        self.parameters = parameters

    def add_drop(self):
        x, y = random.randint(0, self.screen_width), 0
        color = random.choice(self.colors)
        shape = random.choice(self.shapes)

        new_drop = ({'x': x, 'y': y, 'color': color, 'shape': shape})
        self.drops.append(new_drop)

    def draw_drops(self, screen):
        for drop in self.drops:
            x, y = drop['x'], drop['y']
            color = drop['color']
            shape = drop['shape']

            if shape == "circle":
                pygame.draw.circle(screen, color, (int(x), int(y)), 2)
            elif shape == "square":
                pygame.draw.rect(screen, color, (int(x), int(y), 5, 5))
            elif shape == "triangle":
                pygame.draw.polygon(screen, color, [(x, y), (x + 5, y), (x + 2.5, y + 5)])

    def update_drops(self):
        new_drops = []

        for drop in self.drops:
            drop['y'] += self.parameters['speed']

            if drop['y'] < self.screen_height:
                new_drops.append(drop)
            else:
                self.parameters['landed_count'] += self.parameters['drop_per_touch']
                if self.parameters['landed_count'] % self.parameters['drops_per_pixel'] == 0:
                    self.parameters['level_height'] += self.parameters['levels_per_increment']

        self.drops = new_drops

    def draw_score(self, screen):
        font = pygame.font.SysFont("Consolas", 20)
        score_text = font.render(f"Капель дождя: {str(self.parameters['landed_count'])}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def draw_level(self, screen):
        pygame.draw.rect(screen, (173, 216, 230), (0, self.screen_height - self.parameters['level_height'], self.screen_width, self.parameters['level_height']))

    def set_wind_direction(self, mouse_position):
        for drop in self.drops:
            drop_x, drop_y = drop['x'], drop['y']
            direction_vector = pygame.math.Vector2(mouse_position[0] - drop_x, mouse_position[1] - drop_y)

            distance = direction_vector.length()
            max_distance = self.parameters['max_distance_factor']

            influence = max(0, (max_distance - distance) / max_distance)
            influence *= self.parameters['slowdown_factor']

            direction_vector.normalize_ip()
            drop['x'] += influence * direction_vector.x * self.parameters['speed'] * 2
            drop['y'] += influence * direction_vector.y * self.parameters['speed'] * 2
