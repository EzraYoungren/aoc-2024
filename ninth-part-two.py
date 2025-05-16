with open("input.txt") as f:
    actual_file = f.read()

chars = list(actual_file)

result = []

file_id = 0
current_size = 0
for idx, char in enumerate(chars):
    size = int(char)
    if size:
        if idx % 2 == 1:
            result.append({"id": ".", "size": size, "location": current_size})
        else:
            result.append({"id": file_id, "size": size, "location": current_size})
            file_id += 1
        current_size += size

print(result)
actual_result = result.copy()
result.reverse()
size_moved = 0
for file in result:
    file_id = file["id"]
    size = file["size"]
    location = file["location"]
    size_moved += size
    if file_id == ".":
        continue
    else:
        for aidx, afile in enumerate(actual_result):
            afile_id = afile["id"]
            asize = afile["size"]
            alocation = afile["location"]
            if alocation >= location:
                break
            if asize >= size and afile_id == ".":
                print(size)
                difference = asize - size
                finished = True
                actual_result.pop(aidx)
                actual_file_idx = 0
                for bidx, bfile in enumerate(actual_result):
                    bfile_id = bfile["id"]
                    if file_id == bfile_id:
                        actual_file_idx = bidx
                        break
                actual_result[actual_file_idx]["id"] = "."
                actual_result.append(
                    {"id": file_id, "size": size, "location": alocation}
                )
                if difference:
                    actual_result.append(
                        {"id": ".", "size": difference, "location": alocation + size}
                    )
                actual_result.sort(key=lambda x: x["location"])
                actual_result = [file for file in actual_result if file["size"] > 0]
                break


print(actual_result)

# actual_result = [file for file in actual_result if file["id"] != "."]

print(actual_result)
ret = 0

ret_arr = []
for file in actual_result:
    file_id = file["id"]
    for idx in range(file["size"]):
        ret_arr.append(file_id)
    # ret_arr.extend(list(str(file_id) * file["size"]))

print(ret_arr)
for idx, file in enumerate(ret_arr):
    if file != ".":
        ret += idx * int(file)

print(ret)
ret = [
    [
        "0",
        "0",
        "9",
        "9",
        "2",
        "1",
        "1",
        "1",
        "7",
        "7",
        "7",
        "4",
        "4",
        ".",
        "3",
        "3",
        "3",
        ".",
        ".",
        "5",
        "5",
        "5",
        "5",
        ".",
        "6",
        "6",
        "6",
        "6",
        ".",
        ".",
        "8",
        "8",
        "8",
        "8",
    ]
]

# for cidx, cfile in enumerate(actual_result):
#     cfile_id = cfile["id"]
#     csize = cfile["size"]
#     clocation = cfile["location"]

#     if cfile_id == "." and cidx > 0:
#         if actual_result[cidx - 1] == ".":
#             actual_result[cidx]["size"] = (
#                 actual_result[cidx - 1]["size"] + csize
#             )
#             actual_result[cidx - 1]["size"] = 0
#             actual_result[cidx]["location"] = actual_result[cidx - 1][
#                 "location"
#             ]
