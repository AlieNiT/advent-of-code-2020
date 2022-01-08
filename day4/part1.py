res = 0
fields = []
while True:
    inp = input()
    if inp == "" or inp == "end":
        if len(fields) == 8 or (len(fields) == 7 and "cid" not in fields):
            res += 1
        count = 0
        fields = []
        if inp == "end":
            break
        continue
    inp = inp.split()
    fields += [field.split(":")[0] for field in inp]
print(res)