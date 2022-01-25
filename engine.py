import constants
import math
import random



def createPopulation():
    '''
    Initialise les attributs de chaque personne dans la simulation    
    '''

    # Liste des personnes
    persons = []
    #Combien de personnes peuvent bouger
    movable = constants.POPULATION_SIZE * constants.MOVABLE_POPULATION_RATE
    
    for i in range(constants.POPULATION_SIZE):
        # Nous calculons maintenant diverses propriétés d'une personne (position initiale, état de santé,
        # Temps avant la récupération et la vitesse de mouvement initiale)
        
        # position
        x = random.uniform(0, constants.SCENE_WIDTH)
        y = random.uniform(0, constants.SCENE_HEIGHT)

        # état de santé
        state = constants.HEALTHY
        # temps avant que la récupération soit 0 si une personne est en bonne santé
        infectionTTL = 0 # Cette personne est saine
        if (i >= constants.POPULATION_SIZE - constants.INITIAL_INFECTED_POPULATION_SIZE):
            # tSa personne est infectée
            state = constants.INFECTED
            # leur temps avant la récupération est positif            
            infectionTTL = constants.INFECTION_TTL

        # la direction de la personne face, comme angle des radians
        angle = random.uniform(0, 2 * math.pi)

        # la vitesse de cette personne se déplace à
        # cette personne ne bouge pas
        speed = 0
        if (i < movable):
            # Cette personne bouge
            speed = random.uniform(constants.PERSON_MIN_SPEED, constants.PERSON_MAX_SPEED)
        
        # xvelocity et Yvelocity sont les composants du vecteur de la vélocité de cette personne 
        xVelocity = speed * math.cos(angle)
        yVelocity = speed * math.sin(angle)

        # Nous stockons les attributs de cette personne dans une liste
        thisPerson = [x, y, state, infectionTTL, xVelocity, yVelocity]

        # Nous avons finalement ajouté aux attributs de cette personne à la liste des personnes
        persons.append(thisPerson)
    return persons



def update(person):
    '''
    Met à jour la position d'une personne et l'état de santé lors d'une tickette de simulation
    '''

    # Nous déplacons chaque coordonnée par une quantité égale à la composante de vitesse correspondante.
    person[0] += person[4]
    person[1] += person[5]
        
    # Si une personne est en dehors de la scène, nous faisons deux choses:
    # 1 / Nous les déplacons dans la scène en corrigeant ses coordonnées
    # 2 / Nous les faisons rebondir sur la limite de la scène, en corrigeant ses composants de vitesse

    # Si la personne est trop loin à gauche
    if person[0] < 0:
        # Nous les remettons dans la scène
        person[0] = 0
        # and make it so they move in the opposite direction with respect to the x axis
        person[4] = -person[4]
    # Si la personne est trop loin
    # Nous faisons quelque chose de similaire
    elif person[0] > constants.SCENE_WIDTH:
        person[0] = constants.SCENE_WIDTH
        person[4] = - person[4]

    # Si la personne est trop nombreuse en haut ou en bas
    if person[1] < 0:
        person[1] = 0
        person[5] = -person[5]
    elif person[1] > constants.SCENE_HEIGHT:
        person[1] = constants.SCENE_HEIGHT
        person[5] = -person[5]

    # Si une personne est infectée, nous réduisons leur temps avant la récupération par un
    if person[2] == constants.INFECTED:
        person[3] -= 1
        #Si le temps avant que la récupération soit zéro,
        # la personne guérit et devient à l'abri de l'infectio supplémentairen
        if person[3] == 0:
            person[2] = constants.IMMUNE



def circleCollision(c1, c2):
    '''
    Détermine si deux cercles se croisent ou non
    '''
    angle = 0
    while(angle<3.1415926*2):
        # Nous choisissons un point sur le premier cercle
        ptx = c1[0] + (math.cos(angle)*constants.PERSON_RADIUS)
        pty = c1[1] + (math.sin(angle)*constants.PERSON_RADIUS)
        #Nous calculons la longueur entre ce point et le centre de C2
        dx = ptx - c2[0]
        dy = pty - c2[1]
        d = math.sqrt(dx ** 2 + dy ** 2)
        # Si cette longueur est inférieure au rayon de C2, ce point est à l'intérieur du cercle
        if d/2 < constants.PERSON_RADIUS:
            return True
        # Nous passons ensuite à un autre point près de la précédente, jusqu'à ce que nous bougeons autour de C1
        angle = angle + 0.1

    # Aucune collision détectée: C1 et C2 ne se croisent pas
    return False


def computeCollisions(persons, personNumber):
    '''
    Computes the collisions between a population of persons and a single person
    among them, identified by their list index
    '''

    collisions = []
    p = persons[personNumber]
    for j in range (len(persons)):
        # Pour éviter d'envisager des collisions avec eux-mêmes
        if ( j != personNumber):
            q = persons[j]
            # Collision de test entre les personnes P et Q
            if circleCollision((p[0],p[1]),(q[0],q[1])):
                collisions.append((personNumber, j))
                    
    return collisions


def processCollisions(persons, colls):
    '''
    Propagates the infection among a list of person,
    given which ones collide as a list of tuples
    '''
    for collision in colls:
        a, b = collision
        p = persons[a]
        q = persons[b]

        # Si une personne en bonne santé collecte avec la personne infectée et infectée,
        # la personne en bonne santé devient infectée
        if p[2] == constants.INFECTED and q[2] == constants.HEALTHY:
            q[2] = constants.INFECTED
            q[3] = constants.INFECTION_TTL
        elif q[2] == constants.INFECTED and p[2] == constants.HEALTHY:
            p[2] = constants.INFECTED
            p[3] = constants.INFECTION_TTL


def endSimulation(persons):
    '''
    Determines if the simulation can be stopped (because nobody is infected anymore)
    '''
    immuned = 0
    for person in persons:
        if person[2] == constants.INFECTED:
            return False
        if person[2] == constants.IMMUNE:
            immuned += 1

    return True
