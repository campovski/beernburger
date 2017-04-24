fout = open("countries.sql", "w")
with open("tmp/countries.txt", "r") as fin:
    for line in fin:
        fout.write("INSERT INTO country (name) VALUES (\"{0}\");\n".format(line.strip()))
fout.close()
