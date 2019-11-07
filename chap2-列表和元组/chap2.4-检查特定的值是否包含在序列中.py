# 检查特定的值是否包含在序列中  in
permissions = 'rw'
print('w' in permissions)  # true

users = ['mlh', 'foo', 'bar']
result = input("Enter you user name: ") in users
print(result)


# 序列成员资格示例
# 检查用户名和PIN码
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]
username = input("User name: ")
pin = input("PIN code: ")
if [username, pin] in database: print("Access granted")

numbers = [100, 34, 678]
print(len(numbers))  # 3
print(max(numbers))  # 678
print(min(numbers))  # 34
print(max(2, 3))  # 3
print(min(9, 3, 2, 5))  # 2

