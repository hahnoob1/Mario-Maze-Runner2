from pygame import *
from datetime import datetime
from math import *



#define story
def story():
    running = True
    #Load image
    story = image.load("story1.png")
    #scale it to the size of the screen
    story = transform.smoothscale(story, screen.get_size())
    #blit to the screen
    screen.blit(story,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                #if you press the X then story will stop running 
        if key.get_pressed()[27]: running = False

        display.flip()
        #returns to menu
    return "menu"

#the same as story
def credit():
    running = True
    cred = image.load("credits.png")
    cred = transform.smoothscale(cred, screen.get_size())
    screen.blit(cred,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"
#the same as the ones above
def instructions():
    running = True
    inst = image.load("instructions.png")
    inst = transform.smoothscale(inst, screen.get_size())
    screen.blit(inst,(0,0))
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"

def menu():
    running = True
    #Define the positions of the rectangles
    buttons = [Rect(280,y*90+160,200,60) for y in range(3)]
    #Define what each box is 
    vals = ["Start","instructions","credits"]
    #Puts in music
    mixer.music.load("01 - Super Mario Bros.mp3")
    mixer.music.play()
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "exit"

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        #Putting in the images
        ground = image.load("back.jpg")
        screen.blit(ground,(0,0))
        title = image.load("Title.png")
        screen.blit(title,(200,30,100,40))
        start = image.load("start.png")
        screen.blit(start,(280,y*100+150,200,60))
        ints = image.load("int.png")
        screen.blit(ints,(280,y*100+250,200,60))
        credit = image.load("credit.png")
        screen.blit(credit,(265,y*100+330,200,60))
        exit = image.load("exit.png")
        screen.blit(exit,(600,y*100+100,200,60))
        #For the range of the rectangels and vals the rectangles will be drawn
        for r,v in zip(buttons,vals):
            draw.rect(screen,(0,0,0),r,1)
            #if the mosue collides with the rectangles then it will change colour
            if r.collidepoint(mpos):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    return v
            else:
                draw.rect(screen,(255,255,0),r,2)
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False


        display.flip()
    
#to set the values to their values in the beggining/ starting position
init()
#sets screen
screen = display.set_mode((800, 500))
running = True
x,y= 0,0
page = "menu"
#If page is not exit
while page != "exit":
    if page == "menu":
        page = menu()
    #If page is instructions then page will turn from menu to instructions
    if page == "instructions":
        page =instructions()
    if page == "credits":
        page =credit()
        
    if page == "Start":
        page = story()


