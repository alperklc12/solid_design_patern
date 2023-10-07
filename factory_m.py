import pygame
import random
from abc import ABC, abstractmethod
from enum import Enum, auto


class ShapeEnum(Enum):
    CIRCLE = auto()
    RECTANGLE = auto()


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, screen):
        pass


class Circle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius)


class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))


class ShapeFactory:
    @staticmethod
    def create_shape(typ: str, x, y):
        instance = None
        if typ == ShapeEnum.CIRCLE:
            instance = Circle(x, y)
        elif typ == ShapeEnum.RECTANGLE:
            instance = Rectangle(x, y)
        return instance


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Create Shape')
    clock = pygame.time.Clock()

    shapes = []
    for e in list(ShapeEnum):
        print(e)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                shape_type = random.choice(list(ShapeEnum))
                new_shape = ShapeFactory.create_shape(shape_type, mouse_x, mouse_y)
                shapes.append(new_shape)

        screen.fill((255, 255, 255))

        for item in shapes:
            item.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
