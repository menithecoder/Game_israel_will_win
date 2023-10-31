import pygame
import transperent_img as ti

pygame.init()

win_width = 1000
win_height = 700
windows = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Love")

gun_img = ti.white_to_transparent('gun.png', 'gun_no_white.png')
gun_img = pygame.image.load('gun_no_white.png')
gun_width, gun_height = gun_img.get_size()

is_running = True
display_gun = False
start_time = pygame.time.get_ticks()  # Get the current time in milliseconds

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
    elapsed_time = current_time - start_time

    if elapsed_time < 1000:  # Display the gun image for 1 second (1000 milliseconds)
        display_gun = True
    else:
        display_gun = False

    windows.fill((0, 0, 0))  # Clear the screen
    if display_gun:
        x, _ = pygame.mouse.get_pos()
        image_x = x
        image_y = (win_height - gun_height)
        windows.blit(gun_img, (image_x, image_y))

    pygame.display.update()

pygame.quit()
