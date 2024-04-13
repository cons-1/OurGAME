import pygame

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))

bgpic = pygame.image.load("/Users/blue/OurGAME/TEST/Pic/bg.png")
bgpic = pygame.transform.scale(bgpic, (w, h))

m_pic = pygame.image.load("TEST/Pic/pic.png")

sprite = pygame.sprite.Sprite()
sprite.image = m_pic
sprite.rect = sprite.image.get_rect()
sprite.rect.x, sprite.rect.y = w // 2, h // 2

player_group = pygame.sprite.Group()
player_group.add(sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite.rect.x -= 10
            if event.key == pygame.K_RIGHT:
                sprite.rect.x += 10
            if event.key == pygame.K_UP:
                sprite.rect.y -= 10
            if event.key == pygame.K_DOWN:
                sprite.rect.y += 10

    screen.blit(bgpic, (0, 0))
    player_group.draw(screen)

    pygame.display.update()
