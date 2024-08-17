def hello():
    print("Hola People")

def pack(size, weight, volume):
    return [size, weight, volume]

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food_list)):
            if i == 0:
                print(f"First I eat {food_list[i]}.")
            else:
                print(f"Next I eat {food_list[i]}.")

# Function calls outside of any function definitions
hello()
print(pack("size", "weight", "volume"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["lasagna"])
eat_lunch(["orange", "cracker", "lasagna", "cake"])
