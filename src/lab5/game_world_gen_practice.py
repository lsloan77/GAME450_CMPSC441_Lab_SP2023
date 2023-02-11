'''
Lab 5: PCG and Project Lab

This a combined procedural content generation and project lab. 
You will be creating the static components of the game that will be used in the project.
Use the landscape.py file to generate a landscape for the game using perlin noise.
Use the lab 2 cities_n_routes.py file to generate cities and routes for the game.
Draw the landscape, cities and routes on the screen using pygame.draw functions.
Look for triple quotes for instructions on what to do where.
The intention of this lab is to get you familiar with the pygame.draw functions, 
use perlin noise to generate a landscape and more importantly,
build a mindset of writing modular code.
This is the first time you will be creating code that you may use later in the project.
So, please try to write good modular code that you can reuse later.
You can always write non-modular code for the first time and then refactor it later.
'''

import sys
import pygame
import random
import numpy as np
from landscape import get_landscape

from pathlib import Path
sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes


# TODO: Demo blittable surface helper function

''' Create helper functions here '''


#First you must draw the city
#Pygame has a draw function that is used
#you have to iterate till the amount of citynames
#you must provide a starting location and end location
#finally it draws black dots utilzing the RGB: 000
def CityDraw(city_names,city_locations_dict):
    for i in city_names:
         pygame.draw.circle(screen, (0,0,0), city_locations_dict[i], 10)
#Next you can draw the corresponding routes
#You need to define a starting point and end point
#Then a you can draw corresponding lines based on populated points
#It will appear as if all dots are connected through line segments
def RouteDraw(city_locations_dict,routes):
    for (C_Start, C_End) in routes:
        S_Locate = city_locations_dict[C_Start]
        E_Locate = city_locations_dict[C_End]
        pygame.draw.line(screen, (0,0,0), S_Locate, E_Locate,3)

#pygame surface was changed to be refactored
def get_landscape_surface(size):
    landscape = get_landscape(size)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface

if __name__ == "__main__":
    pygame.init()
    size = width, height = 640, 480
    black = 1, 1, 1

    screen = pygame.display.set_mode(size)
    pygame_surface = get_landscape_surface(size)

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta',
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    city_locations = [] 
    routes = []

    ''' Setup cities and routes in here'''
    #below mimick the functions we did in lab 2 previously
    #you can think of these as refactored since 
    #they're essentially pulling it as a library
    city_locations = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(city_names)
    
    
    city_locations_dict = {name: location for name, location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10] 

    print(routes)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))

        ''' draw cities '''
        #both functions are refactored from their original logic
        CityDraw(city_names,city_locations_dict)

        ''' draw first 10 routes '''
        RouteDraw(city_locations_dict,routes)

        pygame.display.flip()

