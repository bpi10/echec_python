# Utile pour supprimer des messages inutiles
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import random
import constants
import engine
import time



def draw(scene, font, persons):
    '''
        Dessine une population de personnes sur la scène
    '''
    # Fond
    scene.fill(constants.BACKGROUND_COLOR)
    # Dessiner toutes les personnes
    for p in persons:
        # un disque par personne
        pygame.draw.circle(scene, constants.PALETTE[p[2]], ((int)(p[0]), (int)(p[1])), constants.PERSON_RADIUS)
        # Si la personne est infectée, nous dessinons leur infectionTTL
        if p[2] == constants.INFECTED:
            ttlText = font.render(str(p[3]), True, (255, 255, 255), constants.PALETTE[p[2]])
            ttlRect = ttlText.get_rect()
            ttlRect.center = ((int)(p[0]), (int)(p[1]))
            scene.blit(ttlText, ttlRect)



def display_final_state(persons):
    '''
    Displays various statistics about the simulation
    '''
    healthy=0
    infected=0
    immune=0

    for p in persons:
        if(p[2] == constants.HEALTHY):
            healthy+=1
        if(p[2]== constants.INFECTED):
            infected+=1
        if(p[2]==constants.IMMUNE):
            immune+=1
    
    
    print("A la fin de la simulation, pour une population de", constants.POPULATION_SIZE,"personnes, il y a :")
    print("-",healthy, "personnes en bonne santé, soit",healthy*100/constants.POPULATION_SIZE,"%")
    print("-",infected, "personnes infectées, soit",infected*100/constants.POPULATION_SIZE,"%")
    print("-",immune, "personnes guéries, soit",immune*100/constants.POPULATION_SIZE,"%")
            

            
if __name__ == '__main__':
    # Initialisation du programme
    random.seed(constants.SEED)
    persons = engine.createPopulation()
    endSimulation = False
    frameNumber = 0
    startTime = time.time()
    
    # Initialisation pygame
    pygame.init()
    pygame.display.set_caption('Covid Simulator')
    clock = pygame.time.Clock()
    scene = pygame.display.set_mode((constants.SCENE_WIDTH, constants.SCENE_HEIGHT))
    font = pygame.font.Font(None, 14)

        

    # boucle principale
    while not endSimulation:
                     
        for j in range (0, len(persons)):
            # Mise à jour de la personne: direction et état de santé
            engine.update(persons[j])
            
            # Trouver des collisions entre personnes
            colls = engine.computeCollisions(persons,j)

            # Les personnes contaminées infectent des personnes en bonne santé
            engine.processCollisions(persons, colls)

            # dessiner la scène
            draw(scene,font,persons)

        # Afficher la mise à jour
        deltaTime = clock.tick()
        pygame.display.update()
        frameNumber += 1
        # time.sleep(0.2)
                

        # fin s'il n'y a pas d'une personne infectée
        endSimulation = engine.endSimulation(persons)

        # événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endSimulation = True
        

    endTime = time.time()
    # Impression moyenne des FPS
    print("FPS moyen durant la simulation :", frameNumber / (endTime - startTime))
    print()

    # Statistiques imprimées sur les personnes
    display_final_state(persons)
    
    pygame.quit()
