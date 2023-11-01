from flask import Flask, render_template
import pygame
import transperent_img as ti
import mp3_player as mp3
import cv2
import time
import x_y_random
from _datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    # Initialize pygame here
    pygame.init()

    win_width = 1000
    win_height = 700

    windows = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Love")

    is_running = True

    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    gun_img = ti.white_to_transparent('image/gun.png', 'image/gun_no_white.png')
    gun_img = pygame.image.load('image/gun_no_white.png')
    gun_width, gun_height = gun_img.get_size()

    gaza_img = pygame.image.load('image/gaza.jpg')
    background_image = pygame.transform.scale(gaza_img, (screen_width, screen_height))

    militery_sight = ti.white_to_transparent('image/militery.png', 'image/militery_no_white.png')
    militery_sight = pygame.image.load('image/militery_no_white.png')
    militery_sight_w, militery_sight_h = militery_sight.get_size()
    militery_sight = pygame.transform.scale(militery_sight, (militery_sight_w // 2, militery_sight_h // 2))

    biden = ti.white_to_transparent('image/biden.png', 'image/biden_no_w.png')
    biden = pygame.image.load('image/biden_no_w.png')
    biden_w, biden_h = biden.get_size()
    biden = pygame.transform.scale(biden, (biden_w, biden_h))

    sara = ti.white_to_transparent('image/sara.png', 'image/sara_no_w.png')
    sara = pygame.image.load('image/sara_no_w.png')
    sara_w, sara_h = sara.get_size()
    sara = pygame.transform.scale(sara, (sara_w - 50, sara_h - 50))

    tank = ti.white_to_transparent('image/tank.png', 'image/tank_no_w.png')
    tank = pygame.image.load('image/tank_no_w.png')
    tank_w, tank_h = tank.get_size()
    tank_w = tank_w + 100
    tank_h = tank_h + 100
    tank = pygame.transform.scale(tank, (tank_w, tank_h))

    bullet = ti.white_to_transparent('image/bullet.png', 'image/bullet_no_w.png')
    bullet = pygame.image.load('image/bullet_no_w.png')
    bullet_w, bullet_h = bullet.get_size()
    bullet = pygame.transform.scale(bullet, (bullet_w - 950, bullet_h - 951))

    cokie = ti.white_to_transparent('image/cokie.png', 'image/cokie_no_w.png')
    cokie = pygame.image.load('image/cokie_no_w.png')

    hamas = ti.white_to_transparent('image/hamas.png', 'image/hamas_no_w.png')
    hamas = pygame.image.load('image/hamas_no_w.png')
    hamas_w, hamas_h = hamas.get_size()
    hamas = pygame.transform.scale(hamas, (hamas_w - 60, hamas_h - 60))

    list_h = [gun_height, tank_h, biden_h, (sara_h - 50)]
    list_w = [gun_width, tank_w, biden_w, (sara_w - 50)]

    atom = ti.white_to_transparent('image/atom.png', 'image/atom_no_w.png')
    atom = pygame.image.load('image/atom_no_w.png')
    atom_w, atom_h = atom.get_size()
    atom = pygame.transform.scale(atom, (atom_w + 600, atom_h + 600))

    rachel = ti.white_to_transparent('image/rachel.png', 'image/rachel_no_w.png')
    rachel = pygame.image.load('image/rachel_no_w.png')
    rachel_w, rachel_h = rachel.get_size()
    rachel = pygame.transform.scale(rachel, (rachel_w + 100, rachel_h + 100))

    trump = ti.white_to_transparent('image/trump.png', 'image/trump_no_w.png')
    trump = pygame.image.load('image/trump_no_w.png')
    trump_w, trump_y = trump.get_size()
    trump = pygame.transform.scale(trump, (trump_w + 50, trump_y + 50))

    carret = ti.white_to_transparent('image/carret.png', 'image/carret_no_w.png')
    carret = pygame.image.load('image/carret_no_w.png')
    carret_w, carret_y = carret.get_size()
    carret = pygame.transform.scale(carret, (carret_w + 50, carret_y + 50))

    shampan = ti.white_to_transparent('image/shampan.png', 'image/shampan_no_w.png')
    shampan = pygame.image.load('image/shampan_no_w.png')
    shampan_w, shampan_y = carret.get_size()
    shampan = pygame.transform.scale(shampan, (shampan_w - 50, shampan_y - 50))

    font_score = pygame.font.Font('font/font_score.ttf', 80)
    font_game_over = pygame.font.Font('font/font_score.ttf', 180)
    font_stage = pygame.font.Font('font/font_stage.ttf', 50)

    list_h = [gun_height, tank_h, biden_h, rachel_w, trump_w, (sara_h - 50)]
    list_w = [gun_width, tank_w, biden_w, rachel_h + 50, trump_y, (sara_w - 50)]

    left_press = False

    counter_gun = 0
    counter_tank = 0
    counter_biden = 0

    max_gun = 15
    max_tank = 5
    max_biden = 1

    x_b, y_b = 0, 0
    x_count, y_count = 0, 0

    count_b = 0
    current_time = 0

    count_ki = 0

    count_time_run = 0
    x_r = 520
    y_r = 80

    list_shot = [bullet, bullet, carret, cokie, bullet, shampan]

    atom_t = 0
    list_img = [gun_img, tank, biden, rachel, trump, sara]
    current_image = 0

    start_timer = datetime.now().second

    stage_sec = 60

    list_stages = [1, 2, 3]
    list_stages_timer = [20, 18, 16]
    list_stages_count_ki = [10, 15, 20]
    stage = 0

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    current_image = (current_image + 1) % len(list_img)
                elif event.button == 5:
                    current_image = (current_image - 1) % len(list_img)

        windows.blit(background_image, (0, 0))

        x, y = pygame.mouse.get_pos()

        left_m_p = pygame.mouse.get_pressed()[0]

        if current_image == 2:
            mp3.mp3_p('mp3/koch rachel.mp3')

        if left_m_p and not left_press:
            x_b, y_b = pygame.mouse.get_pos()

            x_k = x_r + hamas_w
            y_k = y_r + hamas_h
            x_k_b = image_x + (x_count * 4)
            y_k_b = image_y + (y_count * 4)

            if x < x_k - 90 and x > x_r + 50:
                if y > y_r + 50 and y < y_k - 70:
                    count_ki += 1
                    # print('#kill#')

            # print(x_b,y_b)
            if list_img[current_image] == list_img[0]:
                counter_gun += 1
                if max_gun - counter_gun > 0:
                    mp3.mp3_p('mp3/gunfire.mp3')


            elif list_img[current_image] == list_img[1]:

                counter_tank += 1
                if max_tank - counter_tank > 0:
                    mp3.mp3_p('mp3/rocket.mp3')

            elif list_img[current_image] == list_img[2]:
                if max_biden - counter_biden > 0:
                    mp3.mp3_p('mp3/biden-dont.mp3')


            elif list_img[current_image] == list_img[3]:

                mp3.mp3_p('mp3/rachel.mp3')

            elif list_img[current_image] == list_img[4]:
                if max_biden - counter_biden > 0:
                    atom_t = time.time()

                counter_biden += 1

            elif list_img[current_image] == list_img[5]:
                mp3.mp3_p('mp3/sara.mp3')

        left_press = True

        if left_m_p:
            current_time = time.time()
            count_b += 1
            # if count_b<60:

            # elif count_b==60:
            #
            # count_b=0

        if not left_m_p:
            left_press = False

        timer_current = datetime.now().second
        if stage < 3 and count_ki == list_stages_count_ki[stage]:
            print(stage)
            stage_sec -= 10
            stage += 1
            count_ki = 0
            counter_gun, counter_tank, counter_biden = 0, 0, 0
            start_timer = datetime.now().second
        if stage == 3:
            text = font_game_over.render("Israel win", True, (255, 0, 0))
            text_width = text.get_width()

        elif (list_stages_timer[stage] - (
                timer_current - start_timer)) < 0 or max_gun - counter_gun <= 0 and max_tank - counter_tank <= 0 and max_biden - counter_biden < 0 and count_ki < \
                list_stages_count_ki[stage]:
            mp3.mp3_p('mp3/game_over.mp3')
            text = font_game_over.render("Game Over ", True, (255, 0, 0))
            text_width = text.get_width()

            windows.blit(text, ((screen_width // 2) - (text_width // 2) + 30, (screen_height // 2) - 70))
        else:

            text = font_stage.render("Stage " + str(stage + 1), True, (255, 255, 0))
            windows.blit(text, (400, 20))

            if count_time_run == stage_sec:
                x_r = x_y_random.rand('x', screen_width - hamas_w)
                y_r = x_y_random.rand('y', 1)
                count_time_run = 0

            windows.blit(hamas, (x_r, y_r))
            text = font_score.render("Gaza ", True, (255, 0, 0))
            windows.blit(text, (540, 239))
            windows.blit(militery_sight, (x - militery_sight_w // 4, y - militery_sight_h // 4))

            text = font_score.render("Score: " + str(count_ki) + "/" + str(list_stages_count_ki[stage]), True,
                                     (0, 40, 150))
            windows.blit(text, (18, 74))

            text = font_score.render("Timer: 0 : " + str(list_stages_timer[stage] - (timer_current - start_timer)),
                                     True, (0, 200, 0))
            windows.blit(text, (18, 140))

            if current_image == 0:
                if max_gun - counter_gun > 0:
                    text = font_score.render("Fire: " + str(max_gun - counter_gun), True, (255, 50, 0))
                    windows.blit(text, (20, 10))

            elif current_image == 1:
                if max_tank - counter_tank > 0:
                    text = font_score.render("Fire: " + str(max_tank - counter_tank), True, (0, 50, 255))
                    windows.blit(text, (20, 10))

            elif current_image == 2:
                if max_biden - counter_biden > 0:
                    text = font_score.render("Fire: " + str(max_biden - counter_biden), True, (50, 255, 0))
                    windows.blit(text, (20, 10))

            image_x = x - ((list_w[current_image]) // 2)
            image_y = (win_height - (list_h[current_image]))

            windows.blit(list_img[current_image], (image_x, image_y))
            if time.time() - current_time < 0.1:
                x_count = x_dis + x_count
                y_count = y_count + y_dis

                windows.blit(list_shot[current_image], (image_x + (x_count * 10), image_y + (y_count * 10)))



            # print(image_x + x_count, image_y + y_count)
            # print(image_x, image_y)
            else:
                x_count = 0
                y_count = 0

            x_dis = x_b - image_x
            y_dis = y_b - image_y
            x_dis = x_dis // 60
            y_dis = y_dis // 60

            if time.time() - atom_t < 10:
                windows.blit(atom, (150, 20))

        pygame.display.update()

        windows.fill((50, 70, 255))
        # Limit frames per second (FPS)
        count_time_run += 1
        pygame.time.Clock().tick(60)

    pygame.quit()
    # Your pygame code goes here
    # ...

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
