def sum(list):
    if(len(list)==0):
        return 0
    else:
        return list[0] + sum(list[1:])
#print(sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

def count(list):
    if(len(list)==0):
        return 0
    else:
        return 1 + count(list[1:])
#print(count([1,2,3,4]))

        
def max(list):
    if(len(list)==2):
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max
print(max([1,2,3,4,5]))
