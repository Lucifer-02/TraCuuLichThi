raw_file = open("raw_data.txt", "r")

datas = raw_file.read().split("\n")

file = open("test.txt", encoding="utf8", mode="w")

for data in datas:

    data = data.split("\\n")

    for i in range(len(data)):
        data[i] = data[i].replace("\\r", "")
        data[i] = data[i].replace("\\t", "")

    # change '</td><td>' to ','
    for i in range(len(data)):
        data[i] = data[i].replace("</td><td>", ", ")

    # remove tag
    for i in range(len(data)):
        tags = []
        for j in range(len(data[i])):
            if data[i][j] == "<":
                begin = j
            if data[i][j] == ">":
                end = j
                tags.append(data[i][begin:end + 1])
        for tag in tags:

            data[i] = data[i].replace(tag, "")

    # remove space
    for i in range(len(data)):
        data[i] = data[i].strip()

    data_without_space = []

    for i in range(len(data)):
        if data[i] != "":
            data_without_space.append(data[i])

    data = data_without_space

    # remove unused lines

    for i in range(len(data)):
        if data[i][0] == "<":
            sign = i

    data = data[12:sign - 1]

    # continue clean
    for i in range(len(data)):
        data[i] = data[i][:11] + "," + data[i][12:]

    # convert special char
    file = open("unicode.txt", encoding="utf8")

    char_table = file.read().split("\n")

    for i in range(len(char_table)):
        char_table[i] = char_table[i].split("\t")

    for i in range(len(data)):
        for j in range(len(char_table)):
            data[i] = data[i].replace(char_table[j][1], char_table[j][0])

# write data is clean to test.txt file
    file = open("test.txt", encoding="utf8", mode="a")

    for i in range(len(data)):
        file.write(data[i] + "\n")
    file.write("**************************************************************************************************************************************************************************\n")
