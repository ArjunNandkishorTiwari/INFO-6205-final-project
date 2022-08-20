import pygame
import random
pygame.init()


#dimensions

w = 16
h = 16
window = pygame.display.set_mode((850,850))

pygame.display.set_caption('Random Maze Generation')


class Block(): #class for each block cell on the window

    def __init__(self, xCoordinate: int, yCoordinate: int) -> None:
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.traversed = False
        self.partition = [True, True, True, True] # L, R, U, D


    def fetchDescendants(self, matrix: list) -> list:
        
        #Whether the Block has any  untraversed Blocks that can be traced
        directions = [(1, 0), (-1,0), (0, 1), (0, -1)] # neighbour nodes
        descendants = []

        for xCoordinate, yCoordinate in directions:
            if self.xCoordinate+xCoordinate in [len(matrix), -1] or self.yCoordinate+yCoordinate in [-1, len(matrix)]: # Check whether the neighbouring nodes is within the range
                continue
        
            descendant = matrix[self.yCoordinate+yCoordinate][self.xCoordinate+xCoordinate] # he descendant Block

            if descendant.traversed: # Check whether the descendant have previously been traversed
                continue

            descendants.append(descendant)
        return descendants


    def display(self, w: int, h: int, a: int, b: int)-> None:
        #Draw a Block partition
        xCoordinate = self.xCoordinate
        yCoordinate = self.yCoordinate

        if self.partition[0]:
            pygame.draw.rect(window, (25,25,25), (w*xCoordinate+a-w, h*yCoordinate+b, w, h))
        if self.partition[1]:
            pygame.draw.rect(window, (25,25,25), (w*xCoordinate+a+w, h*yCoordinate+b, w, h))
        if self.partition[2]:
            pygame.draw.rect(window, (25,25,25), (w*xCoordinate+a, h*yCoordinate+b-h, w, h))    
        if self.partition[3]:
            pygame.draw.rect(window, (25,25,25), (w*xCoordinate+a, h*yCoordinate+b+h, w, h))  
    

    def trace(self, w: int, h: int)-> None:
        #trace the current Block
        xCoordinate = self.xCoordinate*w
        yCoordinate = self.yCoordinate*h
        pygame.draw.rect(window, (150, 50, 250), (xCoordinate*2+w,yCoordinate*2+h, w, h))


def removepartition(present: Block, next: Block)-> None:
    # Removeing the partition between two Blocks"""
    if next.xCoordinate > present.xCoordinate:     
        present.partition[1] = False
        next.partition[0] = False
    elif next.xCoordinate < present.xCoordinate:
        present.partition[0] = False
        next.partition[1] = False
    elif next.yCoordinate > present.yCoordinate:
        present.partition[3] = False
        next.partition[2] = False
    elif next.yCoordinate < present.yCoordinate:
        present.partition[2] = False
        next.partition[3] = False


def fill()-> None:
    
    for xCoordinate in range(len(matrix)+1):
        for yCoordinate in range(len(matrix)+1):
            pygame.draw.rect(window, (20,20,20), (xCoordinate*w*2, yCoordinate*h*2, w, h))


#matrix to set the current Block and initialise the array
matrix = [[Block(xCoordinate, yCoordinate) for xCoordinate in range(24)] for yCoordinate in range(24)]
present = matrix[0][0]
array = []

window.fill((219, 219 ,219))

entry = False
while not entry:
    for xCoordinate in range(len(matrix)):
        
        for yCoordinate in range(len(matrix)):
            
            matrix[xCoordinate][yCoordinate].display(w, h, (yCoordinate+1)*w, (xCoordinate+1)*h) # Draw partition
    
    fill()

    present.traversed = True
    
    present.trace(w, h) # Highlight the present Block being traversed for real time effect

  
    descendants = present.fetchDescendants(matrix) 
    if descendants:
        next = random.choice(descendants)
        
        
        next.traversed = True

        array.append(present)

        removepartition(present, next)

        present = next
    

    elif array: # If the present has no neighbours go back to the last Block on the array
        
        present = array.pop()

    for e in pygame.event.get():
        
        if e.type == pygame.QUIT:
            
            entry = True
    
    pygame.display.update()
    
    window.fill((210, 210 ,210))
    
    
pygame.quit()


quit()
