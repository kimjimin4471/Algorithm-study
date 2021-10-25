maxValue = 0
# for i in range(999, 100, -1):
#     for j in range(999, 100, -1):
#         num = i * j
#         if num == int(str(num)[::-1]):
#             if maxValue < num:
#                 maxValue = num
lpp = [i * j for i in range(100, 999)
       for j in range(100, 999) if (i * j) == int(str(i * j)[::-1])]
print(sorted(lpp)[-1])
