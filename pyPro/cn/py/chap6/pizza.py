# 存储所点比萨的信息
pizza = {
    'curst': 'thick',
    'toppings': ['mushroom', 'extra cheese']
    }

# 概述所点的披萨
print("You ordered a " + pizza['curst'] + "-curst pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)