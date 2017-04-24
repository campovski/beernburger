fout = open("beers.sql", "w")
with open("tmp/beers.txt", "r") as fin:
    for line in fin:
        if line[0] == "=":
            fout.write("INSERT INTO beer (name, review, grade_taste, grade_color, grade_smell, grade_smoothness, grade_foam, grade_total, alc, image, manufacturer) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', (SELECT id FROM manufacturer WHERE name = '{10}'));\n".format(review["name"], review["review"], review["gt"], review["gc"], review["gs"], review["gss"], review["gf"], review["gt"], review["alc"], review["image"], review["manufacturer"]))
        if line[0] == "#" and line[1] == "#":
            review["name"] = line.strip()[2:]
        elif line[0] == "#":
            review["manufacturer"] = line.strip()[1:]
        elif line[0] == "*":
            review["review"] = line[1:]
        elif line[0] == "-":
            review["image"] = line[1:]
        elif line.strip() != "":
            what, number = line.strip().split("=")
            review[what] = number

f.close()
