import pygame


running = True
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Turtle Bot')




turtle_surf = pygame.image.load('Turtle.png')
turtle_rect = turtle_surf.get_rect(center = (250, 250))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if running:
        screen.blit(turtle_surf, turtle_rect)

    pygame.display.update()
    clock.tick(60)