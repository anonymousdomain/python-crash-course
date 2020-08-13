sqaures = []
cubes=[]
for value in range(1, 13):
    sqaure = value ** 2  # sqaure
    cube=value**3
    sqaures.append(sqaure)
    cubes.append(cube)
print(f"sqaures:{sqaures}")
print(f"cubes:{cubes}")
#min max sum   built in functions

print(min(cubes))
print(max(cubes))
print(sum(sqaures))
print(sum(cubes))
print(sum(cubes)-sum(sqaures))
print("try somthing new & efficent")
#another altarnative
sq=[value**2 for value in range(1,13)]
print(sq)