def is_leap_year(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

# گرفتن ورودی از کاربر
year = int(input("یک سال وارد کن: "))

# بررسی و چاپ نتیجه
if is_leap_year(year):
    print(f"{year} یک سال کبیسه است.")
else:
    print(f"{year} یک سال کبیسه نیست.")