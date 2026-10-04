import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wildlife Information Display")
clock = pygame.time.Clock()

# Load, scale and position images
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))

animal = pygame.image.load("wildlife.png")
animal = pygame.transform.scale(animal, (300, 300))

# Heading and fact text
heading_font = pygame.font.SysFont("arial", 50)
fact_font = pygame.font.SysFont("arial", 28)
heading = heading_font.render("Red Fox", True, "white")
fact = fact_font.render("Foxes use their tails for balance and warmth.", True, "white")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(heading, heading.get_rect(center=(400, 50)))
    screen.blit(animal, (250, 120))
    screen.blit(fact, fact.get_rect(center=(400, 500)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()