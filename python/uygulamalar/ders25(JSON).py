import json

# person='{"name":"Emir","age":19,"city":"İstanbul","hobbies":["Kodlama","Müzik","Spor"]}'

# with open("uygulamalar/data.json","r",encoding="utf-8") as f:
#     result=json.load(f) #dosyadan okumak için load  direkt alcaksan loads
#     print(type(result))
#     print(f"Name:{result["name"]}")
#     print(f"Age:{result["age"]}")
#     print(f"City:{result["city"]}")
#     print("Hobbies:",end="")
#     for item in result["hobbies"]:
#         print(item,end=" ")
# print("\n\n") 
# persona={"name":"Burak","age":22,"city":"İstanbul","hobbies":["Kodlama","Müzik","Spor"]}

# json_result=json.dumps(persona,ensure_ascii=False,indent=4,sort_keys=True,separators=(".","= ")) #jsona dönüştürür  , türkçe karakter

# print(type(json_result))
# print(json_result)

# with open("uygulamalar/people.json","w",encoding="utf-8") as f:
#     json_resulting=json.dump(persona,f,ensure_ascii=False,indent=4)

#UYGULAMA

import os
#import json

FILE_NAME="uygulamalar/person.json"

class Person:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open("uygulamalar/person.json","w",encoding="utf-8") as f:
                json.dump([],f,ensure_ascii=False,indent=4)

    def read_people(self):     
        with open(FILE_NAME,"r",encoding="utf-8") as f:
            return json.load(f)
    
    def save_people(self,people):     
        with open(FILE_NAME,"w",encoding="utf-8") as f:
            json.dump(people,f,ensure_ascii=False,indent=4)

    def add_person(self):
        name=input("Name:")
        age=int(input("Age:"))
        city=input("City:")

        new_person={"name":name,"age":age,"city":city}

        people=self.read_people()
        people.append(new_person)
        self.save_people(people)

        print(f"{name} has been added!")

    def delete_person(self):
        name=input("Enter the name of the person to delete:")
        people=self.read_people()
        update_people=[item for item in people if item["name"] != name]

        if len(people)==len(update_people):
            print(f"{name} not found!") 
        else:
            self.save_people(update_people)
            print(f"{name} has been deleted!")

    def show_people(self):
        people=self.read_people()

        if not people:
            print("No people found!")
        else:
            for item in people:
                print(f"Name:{item["name"]}, Age:{item["age"]}, City:{item["city"]}")

class App:
    def __init__(self):
        self.manager=Person()  #composition
    
    def run(self):
        while True:
            print("\n1-Add Person")
            print("\n2-Delete Person")
            print("\n3-Show All Person")
            print("\n4-Exit")
            choice=int(input("Choose an option"))
        
            if choice==1: self.manager.add_person()
            elif choice==2: self.manager.delete_person()
            elif choice==3: self.manager.show_people()
            elif choice==4: 
                print("Exiting...")
                break
            else:
                print("Invalid option! Please try again")

if __name__=="__main__":
    app=App()
    app.run()