def age_check(age):
    if age<0:
        raise ValueError("Age cannot be negative!")
    else:
        print("Age:", age)
try:
    age_check(-7)
except ValueError as e:
    print("Error:", e)