# List
# List is always changeable, mutable
suhoor_items: list =  ["White Rice", "Salad", "Qeema", "Chai"]
suhoor_items.append("Shaami")
print(suhoor_items)


suhoor_items.pop(2)
print(suhoor_items)

# suhoor_items.remove()
# print(suhoor_items)



# Tuples
# Tuples are inmutable, it means we cannot change them.
suhoor_items_tuple:tuple = ("Paani", "Chai","Bhaaji")
# suhoor_items_tuple[1]= "Lassi"
print(suhoor_items_tuple)