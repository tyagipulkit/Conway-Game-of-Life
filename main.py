import time
import pygame
import numpy as np


BG_COLOR = (10,10,10)
GIRD_COLOR = (40,40,40)
DIE_COLOR = (170,170,170)
ALIVE_COLOR = (255,255,255)
SIZE_HORI = 150
SIZE_VERT = 75

def fill_random(cells):
    cells = np.zeros((cells.shape[0], cells.shape[1]))
    for i in range(cells.shape[0]):
        for j in range(cells.shape[1]):
            cells[i,j] = np.random.randint(2)

    return cells
    


def update(screen, cells, size, with_progress = False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2,col-1:col+2]) - cells[row, col]
        color = BG_COLOR if cells[row, col] == 0 else ALIVE_COLOR

        if cells[row, col] == 1 :
            if alive < 2 or alive > 3:
                if with_progress:
                    color = DIE_COLOR
            
            elif 2 <= alive <=3:
                updated_cells[row, col] = 1
                
                if with_progress:
                    color = ALIVE_COLOR

        else:
            if alive == 3:
                updated_cells [row, col] = 1
                if with_progress:
                    color = ALIVE_COLOR

        pygame.draw.rect(screen, color , (col*size, row*size, size-1, size-1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((SIZE_HORI*10, SIZE_VERT*10))
    
    cells = np.zeros((SIZE_VERT,SIZE_HORI))

    screen.fill(GIRD_COLOR)

    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen,cells,10)
                    pygame.display.update()

                elif event.key == pygame.K_LALT:
                    cells = fill_random(cells)
                    update(screen,cells,10)
                    pygame.display.update()

                elif event.key == pygame.K_x:
                    pygame.quit()  

            if pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                cells[pos[1]//10 , pos[0]//10] = 1
                update(screen,cells,10)
                pygame.display.update()

        screen.fill(GIRD_COLOR)

        if running:
            cells= update(screen, cells, 10, with_progress= True)
            pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()