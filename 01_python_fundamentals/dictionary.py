# info = {"name":"Dina",
#         "class":"S8",
#         "rno":22,
#         "marks":[98,90,99],
#         "cgpa":9,
#         }

# print(info)
# print(type(info))

# print(info["surname"])
# info["surname"]="usman" #add
# info["cgpa"]=9.2 #overwrite
# print(info)



# nested dictionary
# infoo={}
# print(infoo)
# infoo["name"]="dina"
# infoo["marks"]={"phy":90,
#                    "geo":56,}
# print(infoo)
# print(infoo["marks"]["geo"])
# print(infoo.keys())
# print(list(infoo.keys()))
# print(len(infoo.keys()))
# print(len(list(infoo.keys())))



# info = {"name":"Dina",
#         "class":"S8",
#         "rno":22,
#         "marks":[98,90,99],
#         "cgpa":9,
#         }
# print(list(info.values()))
# print(info.items())
# print(list(info.items()))

# print(info.get("name"))
# info.update({"city":"hyderabad",})
# print(info)

marks={}
x=input("enter the phy marks")
marks.update({"phy":x})
print(marks)