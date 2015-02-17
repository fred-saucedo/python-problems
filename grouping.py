"""
* The following method takes in a list and a number "n" and returns the list of groupings of 'n'
"""

def groups_of_n(input_list, n): 
   size_of = len(input_list)
   return [input_list[index*n:index*n+1] for index in range(size_of//n + 1) ]
   
