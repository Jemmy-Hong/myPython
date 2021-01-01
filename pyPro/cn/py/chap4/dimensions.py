dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 便利元组
for dimension in dimensions:
    print(dimension)

# 修改元组变量(通过重新赋值的方式)
dimensions = (200, 50)
print("Original in demensions：")
for dimension in dimensions:
    print(dimension)

# 通过重新赋值就可以改变元组中的元素
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
