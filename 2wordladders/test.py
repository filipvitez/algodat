# import sys
# f = sys.stdin.read()
#
# lines = f.strip().split('\n')
#
# words = int(lines[0][0]) + 1
#
# l1 = lines[1]
#
# # for l in lines[2:words]:
# #
# #     print("testing: " + l1 + " with: " + l)
# #     print("testing: " + "".join(sorted(l1[-4:])) + " with: " + "".join(sorted(l)))
# #     print(("".join(sorted(l1[-4:])) in "".join(sorted(l)) and "".join(sorted(l[-4:])) in "".join(sorted(l1))))
# #     l1 = l
#
# import time
#
# t0 = time.time()
#
# j = 0
# for i in range(125000000000):
#     j = j+1
#
# t1 = time.time()
#
# print(t1-t0)

def sum():
    return 2+2

print(type(sum))
