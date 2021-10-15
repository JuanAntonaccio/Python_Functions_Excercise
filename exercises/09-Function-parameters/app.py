# Your code goes here:
def render_person(name,born,eye,years,gender):
    param=name+" is a "+str(years)+" years old "+gender+" born in "+born+" with "+eye+" eyes"
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))