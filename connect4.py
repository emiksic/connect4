import pygame
import time
pygame.init()
size = [1100, 1000]
screen = pygame.display.set_mode(size)
bg_img = pygame.image.load('bg2.png')

pygame.display.flip()
screen.blit(bg_img, (0, 0))
pygame.display.update()

zut = pygame.image.load('z.png')
crv = pygame.image.load('c.png')
pra = pygame.image.load('prazno.png')


mat = []
for i in range(6):
    aaa = []
    for j in range(7):
        aaa.append(0)
    mat.append(aaa)

s = [6, 6, 6, 6, 6, 6, 6]
xstart = 120
ystart = 25
xc = xstart
yc = ystart

px = 0

red = 1

def updateq():
    pygame.display.flip()
    screen.blit(pra, (0, 0))
    for i in range(7):
        if l[i] == 1:
            screen.blit(crv, (matq[i], 25))
        if l[i] == 2:
            screen.blit(zut, (matq[i], 25))
            
    pygame.display.update()
            
def update():
    pygame.display.flip()
    screen.blit(bg_img, (0, 0))
    for i in range(6):
        for j in range(7):
            if mat[i][j] == 1:
                screen.blit(crv, (matcord[i][j][0], matcord[i][j][1]))
            if mat[i][j] == 2:
                screen.blit(zut, (matcord[i][j][0], matcord[i][j][1]))

    time.sleep(0.4)
    ###screen.blit(crv, (xc, yc))
    ###screen.blit(zut, (850, 180))
screen.blit(crv, (120, 25))
matq = [120, 241, 362, 483, 604, 725, 846]

matcord = [[[120, 180],[245, 180],[365, 180],[490, 180],[610, 180],[730, 180],[850, 180]],
           [[120, 280],[245, 280],[365, 280],[490, 280],[610, 280],[730, 280],[850, 280]],
           [[120, 380],[245, 380],[365, 380],[490, 380],[610, 380],[730, 380],[850, 380]],
           [[120, 480],[245, 480],[365, 480],[490, 480],[610, 480],[730, 480],[850, 480]],
           [[120, 580],[245, 580],[365, 580],[490, 580],[610, 580],[730, 580],[850, 580]],
           [[125, 675],[245, 675],[365, 675],[490, 675],[610, 675],[730, 675],[850, 675]]]

l = [1, 0, 0, 0, 0, 0, 0]
updateq()
l = [0, 0, 0, 0, 0, 0, 0]

running = True
while running:

    ## provjera pobjede
    # u stupcu
    for i in range(6):
        for j in range(3):
            if mat[i][j] == 1 and mat[i][j+1] == 1 and mat[i][j+2] == 1 and mat[i][j+3] == 1:
                pygame.quit()
            if mat[i][j] == 2 and mat[i][j+1] == 2 and mat[i][j+2] == 2 and mat[i][j+3] == 2:
                pygame.quit()

    # u redu
    for i in range(7):
        for j in range(3):
            if mat[j][i] == 1 and mat[j+1][i] == 1 and mat[j+2][i] == 1 and mat[j+3][i] == 1:
                pygame.quit()
            if mat[j][i] == 2 and mat[j+1][i] == 2 and mat[j+2][i] == 2 and mat[j+3][i] == 2:
                pygame.quit()

    # dijagonalno   
    for i in range(3):
        for j in range(4):
            if mat[i][j] == 1 and mat[i+1][j+1] == 1 and mat[i+2][j+2] == 1 and mat[i+3][j+3] == 1:
                pygame.quit()
            if mat[i][j] == 2 and mat[i+1][j+1] == 2 and mat[i+2][j+2] == 2 and mat[i+3][j+3] == 2:
                pygame.quit()

                
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            l[px] = 0
            if event.key == pygame.K_LEFT and px > 0:
                px -= 1
            if event.key == pygame.K_RIGHT and px < 6:
                px += 1
            l[px] = red
            updateq()
            
            '''
            print('list', l, 's[px] = ', s[px])
            '''
            
            if event.key == pygame.K_DOWN and s[px] > 0:
                if s[px] > 1:
                    mat[0][px] = red
                    update()
                    for i in range(1, s[px]):
                        mat[i][px] = red
                        mat[i-1][px] = 0

                        update()
                        
                        '''
                        for j in range(6):
                            print(mat[j])
                        print(s[px])
                        print('\n ---------- \n')
                        '''
                
                else:
                    s[px] = 0
                    mat[0][px] = red
                    
                    update()
                    
                    '''
                    for j in range(6):
                        print(mat[j])
                    print(s[px])
                    print('\n ---------- \n')

                print('------------------------------------------')
                '''
                    
                s[px] -= 1 
                    
                
                if red == 2:
                    red = 1
                    l = [1, 0, 0, 0, 0, 0, 0]
                    updateq()
                    l = [0, 0, 0, 0, 0, 0, 0]
                    px = 0
                else:
                    red = 2
                    l = [2, 0, 0, 0, 0, 0, 0]
                    updateq()
                    l = [0, 0, 0, 0, 0, 0, 0]
                    px = 0
                update()

                
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
    
