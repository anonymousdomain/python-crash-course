aline_1={'color':'green','speed':'slow','name':'cyborg'}
aline_2={'color':'blue','speed':'medium','name':'crikox'}
aline_3={'color':'red','speed':'fast','name':'maxidux'}
#list of dictinaries
list=[aline_1,aline_2,aline_3]


alines=[]
for No_alines in range(20):
     new_aline={'color':'green','speed':'slow','name':'cyborg'}
     alines.append(new_aline)

for aline in alines[:5]:
    print(aline)
    print("........................")

print(len(alines))
 