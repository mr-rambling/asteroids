import pygame
from circleshape import CircleShape


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
