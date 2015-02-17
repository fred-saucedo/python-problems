
import functools 
import math 
import point 
"""
* Using the fold pattern to applie an operation to each member of 
* an input list an returns a value, in this case the sum of all numbers
"""
def sum(input_list):
    return functools.reduce(lambda x, y: x + y, input_list)
"""
* find the smallest, and then return the index of the smallest
"""
def index_of_smallest(input_list):
   if(len(input_list)>0):
      return input_list.index(functools.reduce(lambda x, y: x if (x < y) else y, input_list))
   else: 
      return -1 
"""
* Find the point nearest the origin
* Todo, calculate distance from oirigin
* Find smallest distance
* If point_list is empty, return -1
"""
def nearest_origin(point_list):
   # find distances
   distance_list = [math.sqrt(point.x*point.x + point.y*point.y) for point in point_list if len(point_list)>0]
   if(len(point_list) > 0):
      return point_list[index_of_smallest(distance_list)] 
   else: 
      return -1
