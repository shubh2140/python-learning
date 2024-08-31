marks = {}

math = int(input("Enter math num : "))
marks.update({
    "math":math
})

chem = int(input("Enter chem num : "))
marks.update({
    "chem": chem
})

phy = int(input("Enter phy num : "))
marks.update({
    "physics": phy
})

print(marks)