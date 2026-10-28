# with open("uygulamalar/demo.txt","r",encoding="utf-8") as f:    #2.satırla aynı işlev sadece kapatmaya gerek kalmıyor
# f=open("uygulamalar/demo.txt","r",encoding="utf-8")
# for line in f:
#     print(line,end="")
# my_line=f.readlines()
# print(my_line)
# f.close()

# with open("uygulamalar/demo.txt","r+",encoding="utf-8") as f:
#     print(f.read(10))
#     print(f.tell())
#     print(f.read(10))
#     print(f.tell())  #cursor ın nerede olduğunu söyler
#     for line in f:
#         print(line,end="")
#     f.seek(0)
#     for lines in f.readlines():
#         print(lines,end="")
#     f.seek(0)
#     print("\n\n")
#     f.truncate(10) # a,w,r+,w+ da kullanılır
#     print(f.read(),end="")

## TELEFON REHBERİ UYGULAMASI
import os
from phone_class import PhoneBook

pb=PhoneBook()

while True:
    print("\nPhone Book")
    print("1-Add Contact")
    print("2-List Contact")
    print("3-Delete Contact")
    print("4-Exit")

    choice=int(input("Make your choice:"))

    if choice==1:
        first_name=input("First Name: ")
        last_name=input("Last Name: ")
        phone=input("Phone Number: ")
        pb.add_contact(first_name,last_name,phone)
    elif choice==2:
        pb.list_contacts()
    elif choice==3:
        name=input("Enter the name of the contact you want to delete:")
        pb.delete_contacts(name)
    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again!")