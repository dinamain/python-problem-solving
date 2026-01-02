# myset={6,1,2,2,3,4,"hello","world"}
# print(myset)
# print(len(myset))

# myset.add(9)
# print(myset)
# myset.remove(7) 
# error because no element present.


# sett=set()
# sett.add(("dina",22,))
# # print(sett)

# sett.update([("chnj",45),("shana",21)])
# print(sett)

# sett={9,9.0,8,8.25,8.0}/ #9 and 9.0 same value in set
# print(sett)
# solution is storing one as string
# sett={9,'9.0',8,8.25,'8.0'}
# print(sett)
#solution 2
sett={
    ('int',9),
    ('float',9.0)
}
print(sett)