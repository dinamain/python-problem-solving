f=open("sample.txt","w")
# data1=f.readline()
# print(data1)
# data2=f.readline()
# print(data2) 
# f.write("hai hello\nhow are you")
# f.close()
# f=open("sample.txt","a")
# f.write("\ndina")
# f.close()

# with open("sample.txt","r") as f:
#     data=f.read()
#     print(data)
# fclose not compulsory since closes auto with with

# import os
# os.remove("sample.txt")

f=open("practice.txt",'w')
f.write("hi everyone\n we are learning file io\nusing java\ni like progra mming in java")
f.close()
f=open("practice.txt",'r')
data=f.read()
newdata=data.replace('java','python')
print(newdata)
f=open("practice.txt",'w')
f.write(newdata)
f.close()