import pygame

from simulations.rain import Rain

class MainApp:
    def __init__(self):
        pygame.init()

        self.screen_width = 1920
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption("Pygame")
        self.text_font = pygame.font.SysFont("Consolas", 20)
        self.background_color = (0, 0, 0)

        self.simulators = [Rain(self.screen_width, self.screen_height)]

        self.space_pressed = False

        self.BUTTONS = {
            'LEFT_MOUSE': 0,
            'RIGHT_MOUSE': 3,
            'SPACE': 32,
        }

        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[self.BUTTONS['LEFT_MOUSE']]:
                    for simulator in self.simulators:
                        if hasattr(simulator, 'set_wind_direction'):
                            simulator.set_wind_direction(event.pos)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif event.type == pygame.MOUSEBUTTONUP:
                pass

            elif event.type == pygame.KEYDOWN:
                if event.key == self.BUTTONS['SPACE']:
                    self.space_pressed = True
                    self.simulator_toggle_pause()

            elif event.type == pygame.KEYUP:
                if event.key == self.BUTTONS['SPACE']:
                    self.space_pressed = False
                    self.simulator_toggle_pause()

        return True

    def simulator_toggle_pause(self):
        for simulator in self.simulators:
            simulator.toggle_pause()

    def run_simulation(self):
        running = True
        while running:
            running = self.handle_events()

            for simulator in self.simulators:
                simulator.add_element()
                simulator.update_elements()

            self.screen.fill(self.background_color)

            for simulator in self.simulators:
                simulator.draw_elements(self.screen)
                simulator.draw_info(self.screen)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
