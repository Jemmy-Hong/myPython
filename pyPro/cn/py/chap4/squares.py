# 创建平方
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 使用列表解析创建
squares2 = [value ** 2 for value in range(1, 11)]
print(squares2)
