import pygame
import transperent_img as ti


def image_change():
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    gun_img = ti.white_to_transparent('gun.png', 'gun_no_white.png')
    gun_img = pygame.image.load('gun_no_white.png')
    gun_width, gun_height = gun_img.get_size()

    gaza_img = pygame.image.load('gaza.jpg').convert()
    background_image = pygame.transform.scale(gaza_img, (screen_width, screen_height))

    militery_sight = ti.white_to_transparent('militery.png', 'militery_no_white.png')
    militery_sight = pygame.image.load('militery_no_white.png')
    militery_sight_w, militery_sight_h = militery_sight.get_size()
    militery_sight = pygame.transform.scale(militery_sight, (militery_sight_w // 2, militery_sight_h // 2))

    biden = ti.white_to_transparent('biden.png', 'biden_no_w.png')
    biden = pygame.image.load('biden_no_w.png')
    biden_w, biden_h = biden.get_size()
    biden = pygame.transform.scale(biden, (biden_w, biden_h))

    sara = ti.white_to_transparent('sara.png', 'sara_no_w.png')
    sara = pygame.image.load('sara_no_w.png')
    sara_w, sara_h = sara.get_size()
    sara = pygame.transform.scale(sara, (sara_w - 50, sara_h - 50))

    tank = ti.white_to_transparent('tank.png', 'tank_no_w.png')
    tank = pygame.image.load('tank_no_w.png')
    tank_w, tank_h = tank.get_size()
    tank = pygame.transform.scale(tank, (tank_w + 50, tank_h + 50))

    bullet = ti.white_to_transparent('bullet.png', 'bullet_no_w.png')
    bullet = pygame.image.load('bullet_no_w.png')
    bullet_w, bullet_h = bullet.get_size()
    bullet = pygame.transform.scale(bullet, (bullet_w - 950, bullet_h - 951))

    hamas = ti.white_to_transparent('hamas.png', 'hamas_no_w.png')
    hamas = pygame.image.load('hamas_no_w.png')
    hamas_w, hamas_h = hamas.get_size()
    hamas = pygame.transform.scale(hamas, (hamas_w - 60, hamas_h - 60))

    return screen_width,screen_height,gun_img,gun_width,gun_height,background_image,militery_sight,militery_sight_w, militery_sight_h,biden_w, biden_h,biden,sara_w, sara_h,sara,tank_w, tank_h,tank,bullet_w, bullet_h,bullet,hamas_w, hamas_h,hamas
