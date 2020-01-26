#Author : JARACH_2.0.9 (ACHAL DIXIT)
#This query maker works only on csv text in a .txt file
#use at your own risk
def sqlquery():
    name = input("Enter the file name \n")
    file = open(name,'r')
    fout = open("OUT_"+name,'w')
    query = ""
    value = ""
    x = False
    alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for line in file:
        line = line[0:len(line)-1]
        tokens = line.split(',')
        value: str
        query = "("
        for value in tokens:
            for each in value:
                if each in alph:
                    x = True
                    break
            else:
                x = False
            if x:
                query += "\'{0}\',".format(value)
            else:
                query += "{0},".format(value)
        query = query[0:len(query)-1] + "),\n"
        fout.write(query)
    query = ""
sqlquery()