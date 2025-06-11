import turtle
import pygame
import random

class Shape:
    def init(self, shape_type):
        self.shape_type = shape_type
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.size = random.randint(20, 50)
        self.angle_x = random.choice([-1, 1]) * random.uniform(1, 3)
        self.angle_y = random.choice([-1, 1]) * random.uniform(1, 3)

    def move(self):
        self.x += self.angle_x
        self.y += self.angle_y

        
        if self.x <= 0 or self.x >= WIDTH:
            self.angle_x *= -1
        
        if self.y <= 0 or self.y >= HEIGHT:
            self.angle_y *= -1

    def draw(self, screen):
        if self.shape_type == 'triangle':
            points = [(self.x, self.y - self.size), 
                      (self.x - self.size, self.y + self.size), 
                      (self.x + self.size, self.y + self.size)]
            pygame.draw.polygon(screen, WHITE, points)
        
        elif self.shape_type == 'square':
            pygame.draw.rect(screen, WHITE, (self.x - self.size // 2, 
                                               self.y - self.size // 2,
                                               self.size,
                                               self.size))
        
        elif self.shape_type == 'rectangle':
            pygame.draw.rect(screen, WHITE, (self.x - self.size // 2,
                                               self.y - (self.size // 2) // 2,
                                               self.size,
                                               (self.size // 2)))
        
        elif self.shape_type == 'circle':
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), int(self.size))


shapes_list = []
for _ in range(n):
    shapes_list.append(Shape('triangle'))
for _ in range(m):
    shapes_list.append(Shape('square'))
for _ in range(p):
    shapes_list.append(Shape('rectangle'))
for _ in range(q):
    shapes_list.append(Shape('circle'))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for shape in shapes_list:
        shape.move()
        shape.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
