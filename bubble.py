import pygame
import random

STARTING_BLUE_BUBBLE = 10
STARTING_RED_BUBBLE = 10

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bubbles')
clock = pygame.time.Clock()


class Bubble:

    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4, 8)
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT


def draw_env(bubble_list):
    game_display.fill(WHITE)

    for bubble_dict in bubble_list:
        for bubble_id in bubble_dict:
            bubble = bubble_dict[bubble_id]
            pygame.draw.circle(game_display, bubble.color, [bubble.x, bubble.y], bubble.size)
            bubble.move()
    pygame.display.update()


def main():
    blue_bubbles = dict(enumerate([Bubble(BLUE) for i in range(STARTING_BLUE_BUBBLE)]))
    red_bubbles = dict(enumerate([Bubble(RED) for i in range(STARTING_RED_BUBBLE)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_env([blue_bubbles, red_bubbles])
        clock.tick(60)


if __name__ == '__main__':
    main()



