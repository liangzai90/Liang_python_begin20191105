# 切片操作示例

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 第1个索引指定的元素包含在切片内，第2个索引指定的元素不包含在切片内
print(numbers[3:6])  # [3, 4, 5]
print(numbers[-3:-1])  # [8, 9]
# 第1个索引指定的元素（这里是元素8），位于第2个索引指定的元素（这里是0）后面，结果为空序列
print(numbers[-3:0])  # []
# 如果切片结束于序列末尾，可省略第2个索引
print(numbers[-3:])  # [8, 9, 10]
print(numbers[:3])  # [0, 1, 2]
print(numbers[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 从类似于 http://www.python.org 的URL中提取域名
# url = input("Please enter the URL:")
url = "http://www.python.org"
domain = url[11:-4]
print("Domain name: " + domain)

# 第3个参数是切片的步长（默认是1）
print(numbers[0:10:1])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:10:2])  # [0, 2, 4, 6, 8]
print(numbers[3:6:3])  # [3]

# 从序列中，每隔3个元素提取1个。提供步长4即可
print(numbers[::4])  # [0, 4, 8]
# 步长为0会报错
# 步长为负，从右向左提取元素
print(numbers[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-2])  # [10, 8, 6, 4, 2, 0]
print(numbers[10:0:-2])  # [10, 8, 6, 4, 2]
print(numbers[5:7:-2])  # []
# 从第5个元素到索引0，步长为2
print(numbers[5::-2])  # [5, 3, 1]
# 从最后到索引5，步长为2
print(numbers[:5:-2])  # [10, 8, 6]


