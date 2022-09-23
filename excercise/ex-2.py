#if name is less than 2 characters
#long name must be atleast 3 characters
#otherwise if its more than 50 characters long name
#can be a maximum of 50 characters otherwise name looks good

name = "Canniest Badger"

if len(name)<3:
    print("Name must be atleast 3 characters")
elif len(name)>50:
    print("Name must be maximum of 50 characters")
else:
    print("name looks good")
