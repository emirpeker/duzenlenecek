import random
#random.seed(7) #randomun başlangıç yerini seçiyo
print(random.random())
state=random.getstate()
print(random.random())
random.setstate(state)
print(random.random())
print(random.random())
