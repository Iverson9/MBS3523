import pygame, time, cv2

pygame.init()

width = 800
height = 600
bgcolor = 255, 255, 255
window = pygame.display.set_mode((width, height))
logo = pygame.image.load("Resources/logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (256, 130))
logoblock = logo.get_rect()
logospeed = [1, 1]
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
    window.fill(bgcolor)
    window.blit(logo, logoblock)
    logoblock = logoblock.move(logospeed)
    pygame.display.flip()
    time.sleep(0.005)
    if logoblock.left < 0 or logoblock.right > width:
        logospeed[0] = -logospeed[0]
    if logoblock.top < 0 or logoblock.bottom > height:
        logospeed[1] = -logospeed[1]
    if running == False:
        break
