# Program to find cube of any number
def cube(n):
  return n*n*n
print(cube(4))

# Program to find factorial
num = int(input("enter num to find its factorial "))
def factorial(n):
  if n==0:
    return 1
  else:  
    return n*factorial(n-1)
print("factorial for",num, "is", factorial(num)) 

# Program to find pattern
def count_pattern(pattern,string):
  count=0
  len_seq=len(pattern)
  upper_bound=len(string)-len_seq+1
  for i in range(upper_bound):
      if string[i:i+len_seq] == pattern:
        count += 1
  return count
print(count_pattern(('a','b'),('a','b','c','e','b','a','b','f'))) 

# Program for maze manual 
r = int(input("enter number of rows: "))
c = int(input("enter number of columns: "))
matrix = []
for i in range(0,r):
  matrix.append([])
for i in range(0,r):
  for j in range(0,c):
    matrix[i].append(j)
    matrix[i][j]=0
for i in range(0,r):
  for j in range(0,c):
    print("entry in row:",i+1,"column:",j+1)
    matrix[i][j]=int(input())
print(matrix)

def mazeGameAuto(maze):
    curr = [0, 0]
    path = "00"
    while curr != [4, 6]:
        if curr[0] + 1 < maze.__len__() and maze[curr[0] + 1][curr[1]] == 0 and str(curr[0] + 1) + str(
                curr[1]) not in path:
            curr[0] += 1
            path = path + "->" + str(curr[0]) + str(curr[1])
        elif curr[0] - 1 >= 0 and maze[curr[0] - 1][curr[1]] == 0 and str(curr[0] - 1) + str(curr[1]) not in path:
            curr[0] -= 1
            path = path + "->" + str(curr[0]) + str(curr[1])
        elif curr[1] + 1 < maze[0].__len__() and maze[curr[0]][curr[1] + 1] == 0 and str(curr[0]) + str(
                curr[1] + 1) not in path:
            curr[1] += 1
            path = path + "->" + str(curr[0]) + str(curr[1])
        elif curr[1] - 1 >= 0 and maze[curr[0]][curr[1] - 1] == 0 and str(curr[0]) + str(curr[1] - 1) not in path:
            curr[1] -= 1
            path = path + "->" + str(curr[0]) + str(curr[1])
    path = "The path to the end of the maze is " + path
    return path

mylist = ["ab", "ba", "ab", "tab", "ab", "ab"]
a = 4
maze = [[2, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0]]
print(mazeGameAuto(maze))    