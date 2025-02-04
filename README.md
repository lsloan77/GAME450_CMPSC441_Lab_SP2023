Abstract:

Our project follows game using the Pygame library. We were given a general skeleton. As it is, a user can traverse through a map using the 0-9 keypad. A user could encounter a fight against a computer and is forced to fight in a turn-based manner. The game utilizes multiple AI agents for many aspects of functionality. This could include, core functionality of gameplay, map generation, and even our own unique AI agent. The project is based on the culmination of many labs that were done before it. This was done to aid in contribution for the skeleton implementation, and for understanding how certain AI agents can function to a cohesive design. In addition, we included a UML structure to our game given the scope. Certain aspects of the game require using assets that are best used through inheritance. Overall, it helps with organizing the purpose of how certain files and classes function to eventually get the main game loop running. This includes consideration of sprite generation, how we perform combat, generating the landscape, etc. It was important to assess measures to fix the game. We can make the game more involved by incorporating our GA lab to spread out cities in a realistic way, implementing a cost for travel and restricting movement. Overall, the main goal is to implement and understand how an AI agent can aid in the development of a game. More importantly, how can we use an agent that is thoughtful and purposeful to a goal that is desired to fix overall design.

List of AI components in the project:

The algorithm marked with a _ is the one I integrated
A_ Algorithm\* – Used for general pathfinding
Reflex Agent – Rounds of combat (i.e similar to Rock-Paper scissors agent)
Reinforcement Learning – Choose your weapon
Fitness Function – Set location for cities
AI_Player – looped instance of a computer running through the map

Problem Solved:

I included the A* algorithm to improve the paths in which the code was originally made. Before, there were routes that point to each other via the bressenham functionality. This is the best fit way we can reach between two points. However, I wanted to address the possibility with most OPTIMAL path. So, in addition to making the path the best possible fit, I want to make sure we can get there by the safest route. In addition to the parameters needed to get from start_city to end_city, we need to consider elevation as we are traversing the map. This is because a negative evaluation value can be associated with below sea level, or a higher elevation can be associate with a mountain. Therefore, the you will notice as the game plays now, there is an emphasis on staying on the dark green path. This is the path that is determined as the best fit line by A*. It is safe to assume this line as the path necessary to avoid treacherous environments. But why use A* compared to Dijkstra’s? Mainly due to how A* can handle how we view objects on are way to the destination. The heuristic function actually prioritize the nodes that are likely to lead to the goal. Dijkstra explores nodes in order of their node distance. If we consider additional obstacle for our game’s use case then add ones could be easily integrated for future use. I wanted to mention that I tried to use the floodfill algorithm at first to fulfill this issue. Flood fill is an algorithm that can be used for image processing and graphics. It can determine a continuous region of the same color of a 2D array. My purpose would be to use it for connectivity in a graph. I included the idea of the implementation in a commented portion of my code if interested.

Notice the curved line, This is an example of A\* implementation as it directs as best as it can to the path without being a high or low elevation.
The main implementation method for our combat was via the Reflex based agent. This agent is similar based on the rock paper scissors lab. This agent is reactive based on the accounts of past moves for future considerations. This is to make combat more complex for the player. As opposed to a universal weakness, we can designate combat to by dynamic over the course of a player’s/computer’s health. The concept that is important to highlight is the condition-action rule. It states if player X did action 1, I will therefore choose 2. The fitness function was originally implored in lab 7 (known as the Genetic Algorithm). We wanted to determine the best outcome for our map. This outcome was based on the constraints set by certain environments in the map. For example, we had water and mountains. These had an elevation fitness and we had to determine the best way to draw the map. We can’t just have underwater cities. Instead, we need everyone on the map of play. Now we could use the environment to our advantage… or even disadvantage. For example, a player could suffer penalties by the terrain they’re moving in. As the elevation rises, the player may lose monetary incentives to persevere through this path. That is why it was required to merge into our final project.
We had an AI player and reinforcement learning aspect for our final model. The idea of the AI computer class was a way could loop constantly with traversal of the map. This could be a good testing model as it demonstrates an instance of an AI taking advantage of certain stages of the game. This leads into the next idea of reinforcement learning. If we picked an agent that could handle the best weapon to use in a given situation this could beat the enemy AI. One, this was a good way to handle testing/debugging with an automated agent. Another, it gives a way to use reinforcement learning for an applicable use case.

Additional Points:

ChatGPT was mainly used a means to convey what tools exist that can help me do A*. At first I asked for a generic A* algorithm but later found it necessary to use a module containing pathfinding algorithms. This had what was necessary to get started as opposed to a buggy ground up implementation of A\*. What I could do from there is to set my bounds and parameters. For example, I made a global variable for Elevation to determine my path. This is to highlight the point that chatGPT could not just do my project for me, somewhere along the way I had to understand the interaction of various classes and methods to get the desired outcome that I wanted.
To run the program properly, you need to use run.py at the bottom of the file. You cannot just run it from agent_environment (you will get an error).
I was able to get the GA integrated within my system. I explored mainly with the AI functionality part. I have commented out code to demonstrate that I had tested certain portions of the project in order to deliver a workable product. One thing I had to try to fixe was to consider a player’s inability to travel along a directed graph vs. a graph with no verticies.

Appendix:

ChatGPT Logs (Will also be contained in another file):
User
how can use floodfill on an elevation map to find the shortest path from one point to another in python.

ChatGPT
Floodfill is a common algorithm used to find connected regions in an image. In the context of an elevation map, floodfill can be used to find the shortest path from one point to another by treating the elevation map as an image where each pixel represents an elevation value.

Here's an example of how you can use floodfill to find the shortest path from one point to another in Python:

First, import the necessary libraries:
javascript
Copy code
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label, generate_binary_structure
Load the elevation map as a 2D numpy array:
arduino
Copy code
elevation_map = np.loadtxt('elevation_map.txt')
Define a function to perform floodfill on the elevation map:
scss
Copy code
def floodfill(x, y, target_val, fill_val, map_array):
if map_array[x][y] != target_val:
return
map_array[x][y] = fill_val
if x > 0:
floodfill(x-1, y, target_val, fill_val, map_array)
if y > 0:
floodfill(x, y-1, target_val, fill_val, map_array)
if x < len(map_array)-1:
floodfill(x+1, y, target_val, fill_val, map_array)
if y < len(map_array[0])-1:
floodfill(x, y+1, target_val, fill_val, map_array)
This function recursively fills all connected pixels with a given value, starting from a given point (x, y) and using a target value and fill value.

Define a function to find the shortest path between two points:
python
Copy code
def find_shortest_path(start_x, start_y, end_x, end_y, elevation_map): # Create a binary structure to define the neighborhood
struct = generate_binary_structure(2,2)

    # Perform floodfill to label all connected regions
    labeled_array, num_features = label(elevation_map <= elevation_map[start_x][start_y], structure=struct)

    # Get the label of the end point
    end_label = labeled_array[end_x][end_y]

    # Fill all other regions with a high value
    for i in range(len(labeled_array)):
        for j in range(len(labeled_array[0])):
            if labeled_array[i][j] != end_label:
                elevation_map[i][j] = 99999

    # Fill the start point with a low value
    elevation_map[start_x][start_y] = 0

    # Fill all connected pixels with their distance from the start point
    floodfill(start_x, start_y, 0, -1, elevation_map)

    # Fill the end point with a high value
    elevation_map[end_x][end_y] = 99999

    # Fill all connected pixels with their distance from the end point
    floodfill(end_x, end_y, 99999, -2, elevation_map)

    # Find the shortest path by finding the minimum value of the sum of the distance from the start point and the distance from the end point
    min_dist = float('inf')
    for i in range(len(labeled_array)):
        for j in range(len(labeled_array[0])):
            if labeled_array[i][j] == end_label:
                dist = elevation_map[i][j]
                if dist < min_dist:
                    min_dist = dist

    # Return the minimum distance
    return min_dist

This function first labels all connected regions using floodfill and then fills all other regions with a high value except for the end point which is filled with a low

User
rewrite that function to return a list of coordinants that represent the shortest path
ChatGPT
Sure! Here's a modified version of the find_shortest_path function that returns a list of coordinates that represent the shortest path between the start and end points:

python
Copy code
def find_shortest_path(start_x, start_y, end_x, end_y, elevation_map): # Create a binary structure to define the neighborhood
struct = generate_binary_structure(2,2)

    # Perform floodfill to label all connected regions
    labeled_array, num_features = label(elevation_map <= elevation_map[start_x][start_y], structure=struct)

    # Get the label of the end point
    end_label = labeled_array[end_x][end_y]

    # Fill all other regions with a high value
    for i in range(len(labeled_array)):
        for j in range(len(labeled_array[0])):
            if labeled_array[i][j] != end_label:
                elevation_map[i][j] = 99999

    # Fill the start point with a low value
    elevation_map[start_x][start_y] = 0

    # Fill all connected pixels with their distance from the start point
    floodfill(start_x, start_y, 0, -1, elevation_map)

    # Fill the end point with a high value
    elevation_map[end_x][end_y] = 99999

    # Fill all connected pixels with their distance from the end point
    floodfill(end_x, end_y, 99999, -2, elevation_map)

    # Find the shortest path by backtracking from the end point to the start point
    path = []
    x, y = end_x, end_y
    while labeled_array[x][y] != 0:
        path.append((x, y))
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if x < len(labeled_array)-1:
            neighbors.append((x+1, y))
        if y < len(labeled_array[0])-1:
            neighbors.append((x, y+1))
        dists = []
        for i, j in neighbors:
            dists.append(elevation_map[i][j])
        index = np.argmin(dists)
        x, y = neighbors[index]

    # Add the start point to the path
    path.append((start_x, start_y))

    # Reverse the path so that it goes from start to end
    path.reverse()

    # Return the path
    return path

This function first performs the same floodfill labeling as before, but instead of finding the minimum distance, it backtracks from the end point to the start point to find the shortest path. The path variable is initialized as an empty list, and each step of the backtrack appends the current coordinates to the path. The function then adds the start point to the path and reverses it so that it goes from the start point to the end point. Finally, it returns the path as a list of coordinates.

User
using the pathfinding module in python, traverse a grid from one point to another where each cell in the grid has values 0-1, where 1 is more expensive to traverse
ChatGPT
Sure! Here's an example of how to use the pathfinding module in Python to traverse a grid from one point to another where each cell in the grid has values 0-1, where 1 is more expensive to traverse:

First, install the pathfinding module using pip:
Copy code
pip install pathfinding
Import the necessary modules and define the grid:
python
Copy code
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

# Define the grid

grid = Grid(matrix=[
[0, 0, 1, 0],
[0, 0, 1, 0],
[0, 0, 1, 0],
[0, 0, 0, 0]
])
In this example, the grid is defined as a 4x4 matrix where 0 represents an easy-to-traverse cell and 1 represents a more difficult-to-traverse cell.

Define the start and end points:
python
Copy code
start = grid.node(0, 0)
end = grid.node(3, 3)
In this example, the start point is the top-left cell and the end point is the bottom-right cell.

Define the cost function:
python
Copy code
def cost(node_a, node_b, grid):
return grid.node(\*node_b).weight
In this example, the cost function simply returns the weight of the destination node.

Create an instance of the AStarFinder:
python
Copy code
finder = AStarFinder(diagonal_movement=DiagonalMovement.never, cost_func=cost)
In this example, we're using the A\* algorithm to find the shortest path, and we're specifying that diagonal movement is not allowed.

Find the path:
python
Copy code
path, runs = finder.find_path(start, end, grid)
The find_path method returns the shortest path as a list of (x, y) coordinates and the number of iterations it took to find the path.

Print the path:
python
Copy code
print('path:', path)
This will print the path as a list of (x, y) coordinates.

That's it! Here's the complete code:

python
Copy code
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

# Define the grid

grid = Grid(matrix=[
[0, 0, 1, 0],
[0, 0, 1, 0],
[0, 0, 1, 0],
[0, 0, 0, 0]
])

# Define the start and end points

start = grid.node(0, 0)
end = grid.node(3, 3)

# Define the cost function

def cost(node_a, node_b, grid):
return grid.node(\*node_b).weight

# Create an instance of the AStarFinder

finder = AStarFinder(diagonal_movement=DiagonalMovement.never, cost_func=cost)

# Find the path

path, runs = finder.find_path(start, end, grid)

# Print the path

print('path:', path)
Output:

lua
Copy code
path: [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

User
how to make numpy array absolute value
ChatGPT
To take the absolute value of a NumPy array, you can use the numpy.abs() function. Here's an example:

python
Copy code
import numpy as np

# Define a numpy array with some negative values

arr = np.array([-1, 2, -3, 4, -5])

# Take the absolute value of the array

abs_arr = np.abs(arr)

# Print the result

print(abs_arr)
Output:

csharp
Copy code
[1 2 3 4 5]
In this example, the np.abs() function is used to take the absolute value of the arr NumPy array, resulting in a new array abs_arr where all values are positive. The print() function is used to display the resulting array. Note that the original array arr is not modified.

User
convert np array to array
ChatGPT
To convert a NumPy array to a regular Python array, you can use the tolist() method of the NumPy array. Here's an example:

python
Copy code
import numpy as np

# Define a NumPy array

np_arr = np.array([1, 2, 3, 4, 5])

# Convert the NumPy array to a regular Python array

py_arr = np_arr.tolist()

# Print the result

print(py_arr)
Output:

csharp
Copy code
[1, 2, 3, 4, 5]
In this example, the tolist() method is used to convert the NumPy array np_arr to a regular Python array py_arr. The print() function is used to display the resulting array. Note that the resulting array is a regular Python list, not a NumPy array.

User
get me a list of all the coordinants from a numpy array that are greater than 0
ChatGPT
To get a list of all the coordinates (indices) from a NumPy array that are greater than 0, you can use the numpy.where() function. Here's an example:

python
Copy code
import numpy as np

# Define a NumPy array

arr = np.array([[0, 1, 0], [2, 0, 3], [0, 4, 0]])

# Get the coordinates where the array is greater than 0

coords = np.where(arr > 0)

# Convert the coordinates to a list of tuples

coord_list = list(zip(coords[0], coords[1]))

# Print the result

print(coord_list)
Output:

css
Copy code
[(0, 1), (1, 0), (1, 2), (2, 1)]
In this example, the np.where() function is used to get the indices of all elements in the arr NumPy array that are greater than 0. The resulting coords variable is a tuple of arrays containing the row and column indices, respectively. The zip() function is used to combine the row and column indices into a list of tuples, and the list() function is used to convert this list to a regular Python list. The resulting coord_list variable is a list of tuples containing the coordinates of all elements in the arr NumPy array that are greater than 0. Finally, the print() function is used to display the resulting list of coordinates.

User
get 10 random samples of unique values from a list
ChatGPT
To get 10 random samples of unique values from a list, you can use the random.sample() function from the Python standard library. Here's an example:

python
Copy code
import random

# Define a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get 10 random samples from the list

samples = random.sample(my_list, 10)

# Print the result

print(samples)
Output (example):

csharp
Copy code
[5, 7, 2, 1, 8, 3, 6, 10, 9, 4]
In this example, the random.sample() function is used to get 10 random samples from the my_list list. The resulting samples variable is a list containing 10 unique values randomly selected from the original list. Finally, the print() function is used to display the resulting list of samples. Note that if the original list contains less than 10 unique values, the random.sample() function will raise a ValueError exception.

User
get me a list of all the coordinants from a numpy dataframe array that are greater than 0
ChatGPT
To get a list of all the coordinates (indices) from a NumPy array or a NumPy dataframe array that are greater than 0, you can use the numpy.where() function. Here's an example:

python
Copy code
import numpy as np
import pandas as pd

# Define a NumPy dataframe array

df_arr = pd.DataFrame({'A': [0, 1, 0], 'B': [2, 0, 3], 'C': [0, 4, 0]})

# Get the coordinates where the array is greater than 0

coords = np.where(df_arr > 0)

# Convert the coordinates to a list of tuples

coord_list = list(zip(coords[0], coords[1]))

# Print the result

print(coord_list)
Output:

css
Copy code
[(0, 1), (1, 0), (1, 2), (2, 1)]
In this example, the np.where() function is used to get the indices of all elements in the df_arr NumPy dataframe array that are greater than 0. The resulting coords variable is a tuple of arrays containing the row and column indices, respectively. The zip() function is used to combine the row and column indices into a list of tuples, and the list() function is used to convert this list to a regular Python list. The resulting coord_list variable is a list of tuples containing the coordinates of all elements in the df_arr NumPy dataframe array that are greater than 0. Finally, the print() function is used to display the resulting list of coordinates.

User
convert numpy dataframe to numpy array
ChatGPT
To convert a NumPy dataframe to a NumPy array, you can use the values attribute of the dataframe. Here's an example:

python
Copy code
import pandas as pd
import numpy as np

# Define a NumPy dataframe

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Convert the NumPy dataframe to a NumPy array

arr = df.values

# Print the result

print(arr)
Output:

lua
Copy code
[[1 4 7]
 [2 5 8]
 [3 6 9]]
In this example, the values attribute is used to convert the NumPy dataframe df to a NumPy array arr. The print() function is used to display the resulting array. Note that the resulting array has the same shape as the original dataframe, and the column names are not preserved in the array. If you want to preserve the column names, you can use the to_numpy() method instead of the values attribute, but this method is only available in more recent versions of Pandas:

python
Copy code

# Convert the NumPy dataframe to a NumPy array with column names

arr_with_names = df.to_numpy()

# Print the result

print(arr_with_names)
Output:

lua
Copy code
[[1 4 7]
 [2 5 8]
 [3 6 9]]

User
get coordinantes of list where value is breater than 0
ChatGPT
To get the coordinates (indices) of a list where the value is greater than 0, you can use the enumerate() function to iterate over the list and check each value. Here's an example:

python
Copy code

# Define a list

my_list = [1, 0, 3, 0, 5, 0, 7]

# Get the coordinates where the value is greater than 0

coord_list = [(i, val) for i, val in enumerate(my_list) if val > 0]

# Print the result

print(coord_list)
Output:

css
Copy code
[(0, 1), (2, 3), (4, 5), (6, 7)]
In this example, the enumerate() function is used to iterate over the my_list list and get both the index and value of each element. The resulting (i, val) tuple is added to the coord_list variable if the value is greater than 0. Finally, the print() function is used to display the resulting list of coordinates. Note that the resulting coord_list variable is a list of tuples containing the coordinates of all elements in the my_list list that are greater than 0.

User
get coordinantes of 2d list where value is breater than 0
ChatGPT
To get the coordinates (indices) of a 2D list where the value is greater than 0, you can use a nested loop to iterate over the rows and columns of the list and check each value. Here's an example:

python
Copy code

# Define a 2D list

my_list = [[1, 0, 3], [0, 5, 0], [7, 0, 9]]

# Get the coordinates where the value is greater than 0

coord_list = [(i, j) for i in range(len(my_list)) for j in range(len(my_list[0])) if my_list[i][j] > 0]

# Print the result

print(coord_list)
Output:

css
Copy code
[(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
In this example, a nested loop is used to iterate over the rows and columns of the my_list 2D list. The resulting (i, j) tuple is added to the coord_list variable if the value at the current position is greater than 0. Finally, the print() function is used to display the resulting list of coordinates. Note that the resulting coord_list variable is a list of tuples containing the coordinates of all elements in the my_list 2D list that are greater than 0.

User
multiply entire numpy array
ChatGPT
To multiply an entire NumPy array by a scalar, you can use the numpy.multiply() function or the \* operator. Here's an example:

python
Copy code
import numpy as np

# Define a NumPy array

arr = np.array([[1, 2], [3, 4]])

# Multiply the entire array by a scalar

mult_arr = np.multiply(arr, 2)

# or: mult_arr = arr \* 2

# Print the result

print(mult_arr)
Output:

lua
Copy code
[[2 4]
 [6 8]]
In this example, the np.multiply() function is used to multiply the entire arr NumPy array by the scalar value 2, resulting in a new array mult_arr where every element is multiplied by 2. Alternatively, you can use the \* operator to perform element-wise multiplication between the array and the scalar value. The print() function is used to display the resulting array. Note that the original array arr is not modified.

User
make numpy array int
ChatGPT
To convert a NumPy array to integer type, you can use the astype() method of the array. Here's an example:

python
Copy code
import numpy as np

# Define a NumPy array with floating point values

arr = np.array([1.0, 2.5, 3.9, 4.2, 5.8])

# Convert the array to integer type

int_arr = arr.astype(int)

# Print the result

print(int_arr)
Output:

csharp
Copy code
[1 2 3 4 5]
In this example, the astype() method is used to convert the arr NumPy array from floating point type to integer type, resulting in a new array int_arr where each value is rounded down to the nearest integer. The print() function is used to display the resulting array. Note that the original array arr is not modified.

User
add to entire nparray
ChatGPT
To add a scalar value to every element in a NumPy array, you can use the numpy.add() function or the + operator. Here's an example:

python
Copy code
import numpy as np

# Define a NumPy array

arr = np.array([[1, 2], [3, 4]])

# Add a scalar value to the entire array

add_arr = np.add(arr, 2)

# or: add_arr = arr + 2

# Print the result

print(add_arr)
Output:

lua
Copy code
[[3 4]
 [5 6]]
In this example, the np.add() function is used to add the scalar value 2 to every element in the arr NumPy array, resulting in a new array add_arr where every element is increased by 2. Alternatively, you can use the + operator to perform element-wise addition between the array and the scalar value. The print() function is used to display the resulting array. Note that the original array arr is not modified.

User
get max value in nparray
ChatGPT
To get the maximum value in a NumPy array, you can use the numpy.amax() function or the max() method of the array. Here's an example:

python
Copy code
import numpy as np

# Define a NumPy array

arr = np.array([1, 2, 3, 4, 5])

# Get the maximum value in the array

max_val = np.amax(arr)

# or: max_val = arr.max()

# Print the result

print(max_val)
Output:

Copy code
5
In this example, the np.amax() function is used to get the maximum value in the arr NumPy array, resulting in a new variable max_val that contains the maximum value. Alternatively, you can use the max() method of the array to achieve the same result. The print() function is used to display the resulting maximum value. Note that the original array arr is not modified.
