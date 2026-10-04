import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Sprite Adventure")
clock = pygame.time.Clock()

sprite = pygame.Rect(375, 275, 50, 50)
color = "green"
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Arrow key movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite.x += speed
    if keys[pygame.K_UP]:
        sprite.y -= speed
    if keys[pygame.K_DOWN]:
        sprite.y += speed

    # Keep inside screen and change color on each edge
    if sprite.left <= 0:
        sprite.left = 0
        color = "red"
    if sprite.right >= 800:
        sprite.right = 800
        color = "blue"
    if sprite.top <= 0:
        sprite.top = 0
        color = "yellow"
    if sprite.bottom >= 600:
        sprite.bottom = 600
        color = "purple"

    screen.fill("black")
    pygame.draw.rect(screen, color, sprite)              # solid
    pygame.draw.rect(screen, "white", (50, 50, 80, 80), 3)  # outlined
    pygame.draw.rect(screen, "white", (150, 50, 80, 80))    # solid for comparison

    pygame.display.flip()
    clock.tick(60)

pygame.quit()