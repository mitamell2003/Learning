import sys
month_30 = [4, 6 , 9, 11]
month_31 = [1, 3, 5, 7, 8, 10, 12]
day = int(input("nhập vào ngày "))
month = int(input("nhập vào tháng "))
year = int(input("nhập vào năm "))

nextDay = int(day + 1)
prevDay = int(day - 1)
nextMonth = month
nextYear = year
prevMonth = month
prevYear = year

if day == 30 and (month in month_30):
  
  nextDay == 1
  if month < 12 and month >=1:
    nextMonth += 1 
  else:
    nextMonth = 1
    nextYear += 1

elif day == 31 and (month in month_31):
  
  nextDay == 1
  if month < 12 and month >=1:
    nextMonth += 1 
  else:
    nextMonth = 1
    nextYear += 1

elif month == 2 and (day == 29 or day == 28):
  
  if (int(year) % 4) == 0 and day == 29 :
    nextDay = 1
    nextMonth = 3 
  elif (int(year) % 4) != 0 and day == 28 :
    nextDay = 1
    nextMonth = 3 
  else :
    sys.exit("nhập sai ngày")


if day == 1 and (month in month_30):

  prevDay = 31
  if month < 12 and month >=1:
    prevMonth -= 1 
  else:
    prevMonth = 12
    prevYear -= 1

elif day == 1 and (month == 1):
  
  prevDay = 30
  prevMonth = 12
  prevYear -= 1

elif month == 3 and (day == 1):
  
  if (int(year) % 4) == 0 :
    prevDay = 29
    prevMonth = 2
  else :
    prevDay = 28
    prevMonth = 2

elif (day == 1) and (month in month_31 and month != 3 or month == 2):
  prevDay = 30
  prevMonth -= 1
  

print(f"Ngày tiếp theo là: {nextDay}, month {nextMonth}, year {nextYear} ")
print(f"Ngày hôm qua là: {prevDay}, month {prevMonth}, year {prevYear}")