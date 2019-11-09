print("------ 八皇后 问题 --------")

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

# 判断是否在同一列，或与他们的垂直距离相等（位于一条对角线）
# abs(state[i] - nextX) in (0, nextY - i)

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

ret = list(queens(4))
print(ret)  # [(1, 3, 0, 2), (2, 0, 3, 1)]

len_8 = len(list(queens(8)))
print(len_8)  # 92

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X' + '. ' * (length - pos -1)
    for pos in solution:
        print(line(pos))

import random
print(random.choice(list(queens(8))))
prettyprint(random.choice(list(queens(8))))


