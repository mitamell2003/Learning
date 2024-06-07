# tính tổng các số chia hết cho 2 và nhỏ hơn 15
x = 2
sum = 0
while x < 15:
  if x % 2 == 0:
    sum += x
  x +=1
print(sum)

