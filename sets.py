s1 = [1,2,3,4]
s2 = [2,3,4,5,6]

print "s1: ",s1
print "s2: ",s2

def union(s1, s2):
    union = [x for x in s1] + [x for x in s2 if x not in s1]
    print "UNION: ",union
    return union
union(s1, s2)

def intersect(s1, s2):
    intersect = [x for x in s1 if x in s2]
    print "INTERSECTION: ",intersect
    return intersect
intersect(s1, s2)
 
def set_diff(s1, s2):
    diff = [x for x in s1 if x not in s2]
    print "SET DIFFERENCE: ", diff
    return diff
set_diff(s1, s2)

def sym_diff(s1, s2):
    u = union(s1, s2)
    i = intersect(s1, s2)
    diff = set_diff(u, i)
    print "SYMMETRIC DIFFERENCE: ", diff
    return diff
sym_diff(s1, s2)

def cartesian(s1, s2):
    cart = [[x,y] for x in s1 for y in s2]
    print "CARTESIAN: ", cart
    return cart
cartesian(s1, s2)
