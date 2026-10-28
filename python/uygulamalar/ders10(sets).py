fruits={"grape","orange","strawberry","blackberyy","fig","plum"}
print(fruits)
fruits2=["apricot","melon","watermelon"]
fruits3={"apple","cherry"}
fruits4={"lemon","kiwi"}
fruits.update(fruits2)
print(fruits)

fruits |= fruits4 | fruits3
print(fruits)

print("\n\n")

removeItem=fruits.pop()
print(fruits)
print(f"remove item:{removeItem}")
fruits.discard("strawberry")
print(fruits)

setNumber1={1,7,9,19,23,4}
setNumber2={5,12,34,25,2,4}

print("\n\n\n")
result=fruits.union(fruits2)
print(result)

print("\n")
result2=setNumber1.intersection(setNumber2)
print(result2)