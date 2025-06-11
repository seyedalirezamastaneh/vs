#سال کبیسه
year = 5
if (year % 4) == 0:
  if (year % 100) == 0:
     if (year % 400) == 0:
         print("{0} YES".format(year))
     else:
         print("{0} NO".format(year))
  else:
     print("{0} YES".format(year))
else:
  print("{0} NO".format(year)) 
