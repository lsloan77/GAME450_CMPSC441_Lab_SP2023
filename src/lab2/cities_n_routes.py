''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of cities and all possible routes between them.
'''
import random
from itertools import combinations

def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of cities to be generated 
    and returns a list of cities with their x and y coordinates. The cities are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of cities to generate
    :return: A list of cities with random x and y coordinates.
    """
    size1 = size[0]  #For these lines I wanted to take each index's value so we can dynamically allocate a size change in the range of the random number
    size2 = size[1]  #hence 0 - 100(var) and 0 - 200(var)
    coord = [] #Array initialization of a coordinate system tuple
    for i in range(n_cities): 
        rand1 = random.randint(0, size1)
        rand2 = random.randint(0, size2)
        coord.append((rand1,rand2)) #Adds each coord as a tuple to a list

    return coord 
        
     # Consider the condition where x size and y size are different
    

def get_routes(city_names):
    """
    It takes a list of cities and returns a list of all possible routes between those cities. 
    Equivalently, all possible routes is just all the possible pairs of the cities. 
    
    :param cities: a list of city names
    :return: A list of tuples representing all possible links between cities/ pairs of cities, 
            each item in the list (a link) represents a route between two cities.
    """
    citylen = len(city_names) #Had to contain the for loop to the amount of cities their are
    combination = [] #initalization of an array
    for i in range (citylen):
        combination = list(combinations(city_names, 2)) #combination function that gives us unique possibilities (with no repeated cities)

    return combination
    


# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the cities and routes'''
    coordinates = get_randomly_spread_cities((100, 200), len(city_names))
    unique_paths = get_routes(city_names)
    print('Cities:')
    for i, city in enumerate(coordinates):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(unique_paths):
        print(f'{i}: {route[0]} to {route[1]}')
