info = [
    ["name", "age", "pet"],
    ["Amy", "20", "bird"],
    ["John", "21", "cat"],
    ["Ash", "24", "dog"],
]
# Remove the keys and save them in a variable
keys = info[0]
# print(f"keys {keys}")
info.pop(0)
# Initialise an empty dictionary
class_info = {}

# enumerate
for i in range(len(keys)):
    student_dict = {}
    for j in range(len(info)):
        student_dict[keys[j]] = info[i][j]
    #     keys[0] == "name"
    #     student_dict["name"] = "amy"
    #     {"name": "amy"}
    #     == == j = 1
    #     keys[1] == "age"
    #     student_dict["age"] = "20"
    #     {"name": "amy", "age": "20"}
    #     == == = j = 2
    #     keys[2] == "pet"
    #     student_dict["pet"] = "bird"
    #     {"name": "amy", "age": "20", "pet": "bird"}

    class_info[str(i)] = student_dict
    class_info["0"]
    {"0": {"name": "amy", "age": "20", "pet": "bird"}}

print(class_info)
