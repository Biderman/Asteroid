from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from  logger import log_event
import random

class Asteroid(CircleShape):


    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            velocity_1 = self.velocity.rotate(angle)
            velocity_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_1.velocity = velocity_1 * 1.2
            ast_2.velocity = velocity_2 * 1.2
