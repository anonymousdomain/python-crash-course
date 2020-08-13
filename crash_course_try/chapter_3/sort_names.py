names = ['dawit', 'nahom', 'eyuel', 'selam', 'mitu', 'tinu', 'birukty', 'ahmod']
print(f"orginal list:{names}")
#sorted() used to a list temporarly
print(f"temporarly_sorted_list:{sorted(names)}")
print(f"orginal_list:{names}")

print()
#sort used to sort a list permantly
names.sort()
print(names)
print()
#revers sort
names.sort(reverse=True)
print(names)
print()
#other alternative to sort a list reverse
names.reverse()
print(names)

