
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        ##self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)
        
    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            asteroid_1_velocity = self.velocity.rotate(random_angle)
            asteroid_2_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y,new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y,new_radius)
            asteroid_1.velocity = 1.2 * asteroid_1_velocity
            asteroid_2.velocity = 1.2 * asteroid_2_velocity
            
    
    def update(self, dt):
        
        
        self.position += self.velocity * dt
        # print("Asteroid update called",self.velocity)