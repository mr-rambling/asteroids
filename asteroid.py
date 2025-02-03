import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return (
            pygame.draw.circle(
                screen,
                "grey35",
                self.position,
                self.radius,
                width=2
            )
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Create new split asteroids
        rotation = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split1 = Asteroid(self.position.x, self.position.y, new_radius)
        split1.velocity = self.velocity.rotate(rotation) * 1.2

        split2 = Asteroid(self.position.x, self.position.y, new_radius)
        split2.velocity = self.velocity.rotate(-rotation) * 1.2
