import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (36,36,36)
red = (213,50,80)
green = (0,255,0)

display_width = 600
display_height = 500

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

def score(score):
    score_font = pygame.font.SysFont("arial",15)
    value = score_font.render(" Score: " + str(score),True,white)
    display.blit(value,[0,0])

def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(display , green, [x[0],x[1], snake_block, snake_block],border_radius=3)
    

def message(msg,color,size = 12):
    font_style = pygame.font.SysFont("bahnschrift",size)
    mesg = font_style.render(msg,True,color)
    display.blit(mesg, [display_width/8,display_height/5])

def gameloop():
    game_over=False
    game_close=False

    x1 = display_width/2
    y1 = display_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width -snake_block)/10.0)*10.0
    foody = round(random.randrange(0, display_height -snake_block)/10.0)*10.0

    while not game_over:
        while game_close == True:
            display.fill(black)
            message("You Lost ! Press space or Q to quit !",red,35)

            score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    
                    if event.key == pygame.K_SPACE:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                    print("Left") #for debugging purposes

                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                    print("Right")
                
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                    print("Down")
                
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                    print("Up")
        
        if x1 >= display_width or x1<0 or y1>= display_height or y1<0:
            game_close = True
        
        x1+=x1_change
        y1+=y1_change

        display.fill(black)
        pygame.draw.rect(display,red,[foodx,foody,snake_block,snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True
        
        snake(snake_block,snake_list)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,display_width-snake_block)/10.0)*10.0
            foody = round(random.randrange(0,display_height-snake_block)/10.0)*10.0

            Length_of_snake += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameloop()