import json

data_num = 0

for i in range(17):
    with open("data" + str(i + 1) + ".json", "r") as read_file:
        data = json.load(read_file)
        for j in range(len(data)):
            data_num = data_num + len(data[j][1])
