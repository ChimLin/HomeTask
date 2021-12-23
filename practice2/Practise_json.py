import json
import pprint

# # Opening JSON file
# f = open('C:/Users/Geda Barnaloe/Downloads/json_doc.json')
#
# # returns JSON object as
# # a dictionary
# data = json.load(f)
#
# # Iterating through the json
# # list
# pp = pprint.PrettyPrinter(indent=4)
# # pp.pprint(data.values())
# d = data.values()
# pp.pprint(len(data.values()))
#
# i = 0
# for x in data.values():
#     pp.pprint(x)
#     i += 1
#     if x == 3:
#         break
#
# f.close()

with open('C:/Users/Geda Barnaloe/Downloads/json_doc.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

print(type(obj))
e = 0
h = 0
for x in obj["root"]:
    if x["id"] == 'user09':
        try:
            print(type(x["codes"]))
            print(x["codes"])
            lst = x["codes"]
            if "E" in lst or "H" in lst:
                if "E" in lst and "H" in lst:
                    e += lst.count("E")
                    h += lst.count("H")
                elif "E" in lst:
                    e += lst.count("E")
                elif "H" in lst:
                    h += lst.count("H")
        except:
            continue


print(e, h, sep=" ")


def holiday(input_list = ['dream', 'party']):
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return  input_list

panda = ['bamboo', 'python']
print(panda)
student = panda
panda[0] = 'leaf'
print(student, "studet")
student[1] = 'algorithm'
student = holiday()
print(panda, "panda")
print(student, "studet")
student.append(panda[1])
print(student, "studet")
panda = holiday()
print(panda)
