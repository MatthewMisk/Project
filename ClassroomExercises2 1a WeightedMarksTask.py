mark1 = int(input("how many marks did you get? "))
weight1 = int(input("input the weight of the first mark: "))

mark2 = int(input("how many marks did you get: "))
weight2 = int(input("input the weight of the second mark mark: "))

mark3 = int(input("how many marks did you get: "))
weight3 = int(input("input the weight of the third mark mark: "))


print("Mark of first paper = "+ str(mark1),"Weight of first mark = " + str(weight1))
percentage1 = weight1 * mark1
totalpercentage1 = percentage1/100
print(totalpercentage1)

print("Mark of second paper = "+ str(mark2),"Weight of second mark = " + str(weight2))
percentage2 = weight2 * mark2
totalpercentage2 = percentage2/100
print(totalpercentage2)

print("Mark of second paper = "+ str(mark3),"Weight of second mark = " + str(weight3))
percentage3 = weight3 * mark3
totalpercentage3 = percentage3/100
print(totalpercentage3)

totalmark = totalpercentage1 + totalpercentage2 + totalpercentage3
print("Total mark: " + str(totalmark) + "%")