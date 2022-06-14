import json
import sys
object_started = False
with open(sys.argv[1]) as file:
    objects = []
    for line in file.readlines():
        if line.startswith("{"):
            object_started = True
            obj = ""
        if object_started:
            obj += line
        if line.startswith("}"):
            object_started = False
            objects.append(obj)
            obj = ""

dict_objects = []           
for i in range(len(objects)):
    dict_objects.append(json.loads(objects[i]))

updates_available = []
for i in range(len(dict_objects)):
    if(bool(dict_objects[i]["kb"])):
    #    print(dict_objects[i]["kb"])
       updates_available.extend(dict_objects[i]["kb"])
    else:
        continue

print(updates_available)