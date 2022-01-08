def validate(table):
    if not (len(table) == 8 or (len(table) == 7 and "cid" not in table)):
        print("length failed")
        return False
    if not (1920 <= int(table["byr"]) <= 2002):
        print("byr failed(" + table["byr"] + ")")
        return False
    if not (2010 <= int(table["iyr"]) <= 2020):
        print("iyr failed(" + table["iyr"] + ")")
        return False
    if not (2020 <= int(table["eyr"]) <= 2030):
        print("eyr failed(" + table["eyr"] + ")")
        return False
    if len(table["hgt"]) < 2:
        print("hgt failed(" + table["hgt"] + ")")
        return False
    elif table["hgt"][-2:] == "cm":
        if not (150 <= int(table["hgt"][:-2]) <= 193):
            print("hgt failed(" + table["hgt"] + ")")
            return False
    elif table["hgt"][-2:] == "in":
        if not (59 <= int(table["hgt"][:-2]) <= 76):
            print("hgt failed(" + table["hgt"] + ")")
            return False
    else:
        print("hgt failed(" + table["hgt"] + ")")
        return False
    if not (len(table["hcl"]) == 7 and table["hcl"][0] == '#'):
        print("hcl failed(" + table["hcl"] + ")")
        return False
    else:
        for ch in table["hcl"][1:]:
            if ch not in "0123456789abcdef":
                print("hcl failed(" + table["hcl"] + ")")
                return False
    eye_colors = "amb blu brn gry grn hzl oth".split()
    if table["ecl"] not in eye_colors:
        print("ecl failed(" + table["ecl"] + ")")
        return False
    for ch in table["pid"]:
        if ch not in "0123456789":
            return False
    if int(table["pid"]) >= 10 ** 9:
        print("pid failed(" + table["pid"] + ")")
        return False
    print("valid:")
    for item in table.items():
        print(item)
    print()
    return True


res = 0
fields = {}
while True:
    inp = input()
    if inp == "" or inp == "end":
        if validate(fields):
            res += 1
        fields = {}
        if inp == "end":
            break
        continue
    inp = inp.split()
    for field in inp:
        field = field.split(":")
        fields[field[0]] = field[1]
print(res)