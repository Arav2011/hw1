import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))
font = pygame.font.SysFont("arial", 50)

pet = pygame.sprite.Sprite()
pet.image = pygame.Surface((50, 50))
pet.image.fill("orange")
pet.rect = pet.image.get_rect(center=(400, 300))

foods = pygame.sprite.Group()
for i in range(10):
    food = pygame.sprite.Sprite()
    food.image = pygame.Surface((30, 30))
    food.image.fill("brown")
    food.rect = food.image.get_rect(topleft=(random.randint(0, 770), random.randint(0, 570)))
    foods.add(food)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pet.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        pet.rect.x += 5
    if keys[pygame.K_UP]:
        pet.rect.y -= 5
    if keys[pygame.K_DOWN]:
        pet.rect.y += 5

    pygame.sprite.spritecollide(pet, foods, True)

    screen.blit(background, (0, 0))
    foods.draw(screen)
    screen.blit(pet.image, pet.rect)

    if len(foods) == 0:
        text = font.render("All food collected!", True, "white")
        screen.blit(text, text.get_rect(center=(400, 300)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()