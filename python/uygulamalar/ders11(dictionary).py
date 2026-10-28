car={
    "brand":"Skoda",
    "model":"Octavia",
    "year":1959
}
print(car)

myFriends={
    "friend1":{
        "name":"Murat",
        "year":1987
    },
    "friend2":{
        "name":"Emrullah",
        "year":1988
    },
    "friend3":{
        "name":"Kuzey",
        "year":2005
    }
}
for outer_key,outer_value in myFriends.items():
    print(outer_key)
    for inner_key in outer_value:
        print(inner_key+":",outer_value[inner_key])