import sys
import pygame
import random
import math
from src.Final_Project.sprite import Sprite
from src.Final_Project.pygame_combat import run_pygame_combat
from src.Final_Project.pygame_human_player import PyGameHumanPlayer
from src.Final_Project.landscape import get_landscape, get_combat_bg, make_landscape
from src.Final_Project.pygame_ai_player import PyGameAIPlayer

ELEVATION = None

from pathlib import Path
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab2.cities_n_routes import get_randomly_spread_cities, get_routes
from lab7.ga_cities import Lab7

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)

# A* Algorithm
"""
def heuristic(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def a_star_algorithm(start_city, end_city, cities, routes):
    open_set = set([start_city])
    closed_set = set()
    came_from = dict()
    g_score = {city: float('inf') for city in range(len(cities))}
    f_score = {city: float('inf') for city in range(len(cities))}

    g_score[start_city] = 0
    f_score[start_city] = heuristic(cities[start_city], cities[end_city])

    while open_set:
        current = min(open_set, key=lambda city: f_score[city])

        if current == end_city:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start_city)
            path.reverse()
            return path

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in range(len(cities)):
            if neighbor in closed_set or not routes[current][neighbor]:
                continue

            tentative_g_score = g_score[current] + routes[current][neighbor]

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(cities[neighbor], cities[end_city])

    return None
"""


def get_landscape_surface(size):
    # landscape = get_landscape(size)
    global ELEVATION
    ELEVATION, landscape = make_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window

def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        #text_surface = game_font.render(str(i) + " " + name + str(city_locations[i]), True, (0, 0, 150))
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])

class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes


# import numpy as np
# from scipy.ndimage import label, generate_binary_structure

# def floodfill(x, y, target_val, fill_val, map_array):
#     if map_array[x][y] != target_val:
#         return
#     map_array[x][y] = fill_val
#     if x > 0:
#         floodfill(x-1, y, target_val, fill_val, map_array)
#     if y > 0:
#         floodfill(x, y-1, target_val, fill_val, map_array)
#     if x < len(map_array)-1:
#         floodfill(x+1, y, target_val, fill_val, map_array)
#     if y < len(map_array[0])-1:
#         floodfill(x, y+1, target_val, fill_val, map_array)


# def find_shortest_path(start_x, start_y, end_x, end_y, elevation_map):
#     print(f"FINDING SHORTEST PATH: {start_x}, {start_y} | {end_x}, {end_y}")

#     # Create a binary structure to define the neighborhood
#     struct = generate_binary_structure(2,2)

#     # Perform floodfill to label all connected regions
#     labeled_array, num_features = label(elevation_map <= elevation_map[start_x][start_y], structure=struct)

#     # Get the label of the end point
#     end_label = labeled_array[end_x][end_y]

#     # Fill all other regions with a high value
#     for i in range(len(labeled_array)):
#         for j in range(len(labeled_array[0])):
#             if labeled_array[i][j] != end_label:
#                 elevation_map[i][j] = 99999

#     # Fill the start point with a low value
#     elevation_map[start_x][start_y] = 0

#     # Fill all connected pixels with their distance from the start point
#     floodfill(start_x, start_y, 0, -1, elevation_map)

#     # Fill the end point with a high value
#     elevation_map[end_x][end_y] = 99999

#     # Fill all connected pixels with their distance from the end point
#     floodfill(end_x, end_y, 99999, -2, elevation_map)

#     # Find the shortest path by backtracking from the end point to the start point
#     path = []
#     x, y = end_x, end_y
#     while labeled_array[x][y] != 0:
#         path.append((x, y))
#         neighbors = []
#         if x > 0:
#             neighbors.append((x-1, y))
#         if y > 0:
#             neighbors.append((x, y-1))
#         if x < len(labeled_array)-1:
#             neighbors.append((x+1, y))
#         if y < len(labeled_array[0])-1:
#             neighbors.append((x, y+1))
#         dists = []
#         for i, j in neighbors:
#             dists.append(elevation_map[i][j])
#         index = np.argmin(dists)
#         x, y = neighbors[index]


#     # Add the start point to the path
#     path.append((start_x, start_y))

#     # Reverse the path so that it goes from start to end
#     path.reverse()

#     # Return the path
#     return path


from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import numpy as np

def find_shortest_path(start_x, start_y, end_x, end_y, elevation_map):
    print(f"FINDING SHORTEST PATH: {start_x}, {start_y} | {end_x}, {end_y}")
    
    print(ELEVATION.max())
    print(ELEVATION.min())

    # ELEVATION MAP, consider squaring it so that higher elevations are 
    # SUPER scary and mid eleavtion are ok
    elev = np.add(np.abs(np.multiply(ELEVATION,100)),1).astype(int).tolist()

    grid = Grid(matrix=elev)
    start = grid.node(start_y, start_x)
    end = grid.node(end_y, end_x)


    finder = AStarFinder(
        diagonal_movement=DiagonalMovement.never
        #heuristic= lambda city1, city2:
        #   math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    )

    path, runs = finder.find_path(start, end, grid)
    print(path)

    invert = []
    for point in path:
        i,j = point
        invert.append((j,i))

    return invert



def run():
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "assets/lego.png"
    sprite_speed = 1

    global screen
    screen = setup_window(width, height, "Game World Gen Practice")
    landscape_surface = get_landscape_surface(size)
    print("Landscape surface", landscape_surface.get_size())
    combat_surface = get_combat_surface(size)
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]
    
    # cities = get_randomly_spread_cities(size, len(city_names))
    my_list = ELEVATION.tolist()
    #habitable = [(i, j) for i in range(len(my_list)) for j in range(len(my_list[0])) if my_list[i][j] > 0]
    #cities = random.sample(habitable, len(city_names))
    
    #GA Integration
    cities = Lab7(len(city_names), ELEVATION, size)
    routes = get_routes(cities)
    
    
    #routes = get_routes(city_names)

    random.shuffle(routes)
    routes = routes[:10]

    short_path = find_shortest_path(
        cities[0][0], cities[0][1],
        cities[1][0], cities[1][1],
        #cities[0][2],
        #cities[2][0], cities[2][2],
        ELEVATION
    )


    # TODO before passing routes into a_star, change it so that it
    # is a 2d array where routes[i][j] represents the distance between
    # city i and j
    # do that by making a new array using the cities and routes
    #routes = a_star_algorithm(start_city, end_city, cities, routes)


    player_sprite = Sprite(sprite_path, cities[start_city])

    player = PyGameHumanPlayer()

    """ Add a line below that will reset the player variable to 
    a new object of PyGameAIPlayer class."""

    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=cities,
        routes=routes,
    )
    
    print("routes", routes[0], type(routes[0]))

    while True:
        action = player.selectAction(state)
        if 0 <= int(chr(action)) <= 9:
            if int(chr(action)) != state.current_city and not state.travelling:
                start = cities[state.current_city]
                state.destination_city = int(chr(action))
                #if state.destination_city in 
                destination = cities[state.destination_city]
                print((start,destination))
                #if any (tuple([start, destination]) in routes):
                player_sprite.set_location(cities[state.current_city])
                state.travelling = True
                print(
                    "Travelling from", state.current_city, "to", state.destination_city
                    )

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in cities:
            #print(city)
            #pygame.draw.circle(landscape_surface, (255, 0, 0), city, 5)
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        if len(short_path) > 2:
            start_pos = short_path[0]
            for point in short_path[1:]:
                end_pos = point
                pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos)   
                start_pos = end_pos

        displayCityNames(cities, city_names)
        if state.travelling:
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                print('Arrived at', state.destination_city)

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            run_pygame_combat(combat_surface, screen, player_sprite)
            state.encounter_event = False
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.current_city == end_city:
            print('You have reached the end of the game!')
            break