import pygame, sys
from random import randint, uniform

def laser_update(laser_list, speed=500):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

def display_score():
    score_text = f"Score: {pygame.time.get_ticks()//1000}"
    text_surf = font.render(score_text, True, (255,255,255))
    text_rect = text_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-80))
    display_surface.blit(text_surf, text_rect)
     # rect drwaing
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30,40), width=10, border_radius=5)

def laser_timer(can_shoot, duration=500):
    if not can_shoot:
        current_time= pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot=True

    return can_shoot


def meteor_update(meteor_list, speed=500):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction  * speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)



# game init 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Asteroid")


# ship import  
ship_surf = pygame.image.load('.\graphics\ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# laser import
laser_surf = pygame.image.load('.\graphics\laser.png').convert_alpha()
# laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
laser_list = []

# laser time
can_shoot = True
shoot_time = None 

# meteor 
meteor_surf = pygame.image.load('.\graphics\\meteor.png')
meteor_list = []




# background
bg_surf = pygame.image.load('.\graphics\\background.png').convert()

# import text
font = pygame.font.Font('.\graphics\\subatomic.ttf', 50)

# meteror timer
meteror_timer = pygame.event.custom_type()
pygame.time.set_timer(meteror_timer, 500)


# import sound
laser_sound = pygame.mixer.Sound('.\graphics\\laser.ogg')
explosion_sound = pygame.mixer.Sound('.\graphics\\explosion.wav')
background_music = pygame.mixer.Sound('.\graphics\\music.wav')
background_music.play(loops = -1)


while True: #keeps game running
    # input --> events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            # laser
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

            # timer
            can_shoot=False
            shoot_time = pygame.time.get_ticks()
            laser_sound.play()
        if event.type == meteror_timer:

            # random positions
            rand_x_pos = randint(-100, WINDOW_WIDTH+100) 
            rand_y_pos = randint(-100, -50)

            # creating a rect 
            meteor_rect = meteor_surf.get_rect(center=(rand_x_pos, rand_y_pos))

            # create a random direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)

            meteor_list.append((meteor_rect, direction)) 

            


    dt = clock.tick(120) / 1000
    # framerate limit
    clock.tick(100)
    ship_rect.center = pygame.mouse.get_pos()
    # laser_rect.y -= round(300 * dt)
    laser_update(laser_list)
    can_shoot = laser_timer(can_shoot, 400)
    meteor_update(meteor_list)
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()

    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                meteor_list.remove(meteor_tuple)
                laser_list.remove(laser_rect)
                explosion_sound.play()




    # update
    display_surface.fill((200,200,200))
    display_surface.blit(bg_surf, (0,0))

    # if ship_rect.top > 0:
    #     ship_rect.bottom -= 2
    
    
    #display_surface.blit(laser_surf, laser_rect)
    display_score()
    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf, meteor_tuple[0])
    for rect in laser_list:
        display_surface.blit(laser_surf, rect)
   
    display_surface.blit(ship_surf, ship_rect)
    


    # show and update the frames on screen
    pygame.display.update()


    