motorcycles = ['honda', 'yamaha', 'suzuki' ]
print(motorcycles)

#获取
motorcycles[0] = 'ducati'
print(motorcycles)

#追加
motorcycles.append('lianxing')
print(motorcycles)

#任意位置添加
motorcycles.insert(0, 'yaoyue')
print(motorcycles)

#删除任意位置
del motorcycles[0]
print(motorcycles)

#弹出末尾元素
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

#弹出其他位置元素
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

#根据值删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print('\nA ' + too_expensive + " is too expensive for me.")
