"""Practice with dictionaries"""

#Constructing a dictionary []
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 56, "strawberry": 5}

#Adding the key and value pair
ice_cream ["mint"] = 3

#Removing the key ()
ice_cream.pop("mint")

#To access a value
ice_cream["chocolate"]
print(f"There are {ice_cream['chocolate']} orders of chocolate")

#To modify the value
ice_cream["vanilla"] = 10
print(f"There are {ice_cream['vanilla']} orders of chocolate")

#Length of dictionary
print(f"The number of key value pairs: {len(ice_cream)}")

#Check if key is in dictionary
print("Is chocolate in ice cream? ")
print("chocolate" in ice_cream)

if "mint" in ice_cream:
    print(f"Number of orders of mint is {ice_cream['mint']}")
else:
    print("No order")

#using the for in loop:
for key in ice_cream: 
    print(f"{key} has {ice_cream[key]}")



print("Made my dictionary")
print(ice_cream)

#######
# My reveiw note
# syntax
ice_cream: dict[str, int] = {"chocolate": 12, "vanila": 8, "strawberry": 5}

# adding keys and values pair
ice_cream["mint"] = 3

#remove keys
ice_cream.pop("mint")

# acess
print(ice_cream["chocolate"])
ice_cream["vanila"] = 10

#check
"chocolate" and "mint" in ice_cream

#loop
for keys in ice_cream:
    orders: int = ice_cream[keys]
    print(f"{keys} has {orders} orders")