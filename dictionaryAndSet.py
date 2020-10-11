d1={"Rakhi":"Pizza","Vandana":"Burger","Aditi":"Punjabi tadka","Sugiya":"pasta",
    "Shivango":{"Pizza","Burger","Punjabi tadka","Pasta"}}

print(d1["Shivango"])

print(d1["Aditi"])

d1["Mummy"]="Roti Sabzi"

print(d1)

del d1["Vandana"]

print(d1)
d1.update({"Rahul":"Icecream"})
print(d1)

d2=d1
del d2["Rahul"]
print(d1)

d2=d1.copy()
del d2["Rakhi"]
print(d1)
print(d2)

print(d2.get("Mummy"))

print(d2.keys())
print(d2.items())

# set can only contain the different values,same values cannot be added in the list
l=[1,2]
set_from_list=set(l)
print(set_from_list)
print(type(set_from_list))
set_from_list.add(3)
set_from_list.add(3)
print(set_from_list)
s1=set_from_list.union({1,2,3,4})
s2=set_from_list.intersection({1,2,3,4})
print(set_from_list,s1)
print(set_from_list,s2)
print(set_from_list.isdisjoint(s1))
