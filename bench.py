import random
import constants
import engine
import time


def persons_stats(persons):
    '''
    Affiche les statistiques sur une population de personnes dans la scène
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
    
    return healthy, infected, immune
            

            
if __name__ == '__main__':
    # Initialisation du programme
    random.seed(constants.SEED)
    persons = engine.createPopulation()
    endSimulation = False
    frameNumber = 0
    startTime = time.time()

        

    # boucle principale
    while not endSimulation:
                     
        for j in range (0, len(persons)):
            # Mise à jour de la personne: direction et état de santé
            engine.update(persons[j])
            
            # Trouver des collisions entre personnes
            colls = engine.computeCollisions(persons,j)

            # Les personnes contaminées infectent des personnes en bonne santé
            engine.processCollisions(persons, colls)

        frameNumber += 1
                

        endSimulation = engine.endSimulation(persons)


    endTime = time.time()
    fps =  frameNumber / (endTime - startTime)
    healthy, infected, immune = persons_stats(persons)
    print("healthy;infected;immune;FPS")
    print("{0};{1};{2};{3}".format(healthy, infected, immune, fps))
    
