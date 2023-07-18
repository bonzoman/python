car = {"name1": "BMW", "name2": {"price1": "7000", "price2": "7000"}}

value = car.get("company")

if 'price1' in car:
    print("Key exist! The value is " + car["price1"])
else:
    print('Key not exist!')
