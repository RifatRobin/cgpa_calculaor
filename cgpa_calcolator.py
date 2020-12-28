n = int(input("Enter the number of total semesters: "))
tcl = []
tsg = []

print()

for i in range(1, n+1):
    c = int(input("Enter the "+str(i)+"th semester's credit: "))
    tc = tcl.append(c)
    tcs = sum(tcl)

    sg = float(input("sgpa you get in "+str(i)+"th semester: "))
    sgp = c*sg
    sgpa = tsg.append(sgp)
    tsgpa = sum(tsg)
    print()

print()

# print("Total of credit*cgpa value: "+str(tsgpa))
print("Total credit taken: "+str(tcs))

cgpa = tsgpa/tcs

print("\n\t\t\tYour CGPA is :\t"+str(cgpa)+"\n")
