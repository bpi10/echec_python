# Taille de l'application
SCENE_WIDTH = 1000
SCENE_HEIGHT = 800

# Couleurs de cercles
PALETTE = [(50, 50, 50), (220, 25, 0), (10, 200, 35)]
# couleur DeL'arrièrePlan
BACKGROUND_COLOR = (220, 220, 220)

# Rayon du cercle représentant une personne
PERSON_RADIUS = 8

#Seed - Choisissez une valeur fixe pour toujours avoir la même simulation
SEED = None

# Constantes d'état de santé
HEALTHY = 0
INFECTED = 1
IMMUNE = 2

# Vitesse minimale et maximale d'une personne
PERSON_MIN_SPEED = 1.0
PERSON_MAX_SPEED = 2.5

# Number of persons infected at the beginning of the simulation
INITIAL_INFECTED_POPULATION_SIZE = 1

# nombre de cadres rendus avant qu'une personne ne récupère d'une infection
INFECTION_TTL = 600

# Nombre de personnes dans la scène et le ratio de population en mouvement
POPULATION_SIZE = 100
MOVABLE_POPULATION_RATE = 1
