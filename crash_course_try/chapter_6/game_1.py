aline={'color':'red', 'x_coordinate':2 ,'y_coordinate':50 ,'speed':'medium'}
print()
print(f"startimg postion of aline is {aline['x_coordinate']} & its color is {aline['color']}")

if aline['speed'] == 'slow':
    x_increament = 1
elif aline['speed'] == 'medium':
    x_increament = 4
    aline['color'] = 'green'
elif aline['speed'] == 'fast':
    x_increament = 8
    aline['color'] = 'blue'
aline['x_coordinate'] += x_increament

print(f"new postion of aline is {aline['x_coordinate']} & its color changed in to {aline['color']}")
