marks = {
    "vivan":100,
    "shubham":35,
    "sam":77,
    0: "vivan"
}

print(marks.items())
print(marks.keys())     #name of students left side terms
print(marks.values())   #the marks or the right hand side output

marks.update({"vivan": 99, "jack": 100})
print(marks)

print(marks.get("vivan2"))   # prints none
print(marks["vivan2"])       # prints error
