list1=['pen','pencil','eraser','ruler']
item=input()
rupee_pen=" Rs 10"
rupee_pencil=" Rs 5"
rupee_eraser="Rs 5"
rupee_ruler="Rs 10"

if item=="pen":
    a=item,rupee_pen
    a1=rupee_pen
    print(a)
    print("Print End to stop")
elif item=="pencil":
    a=item,rupee_pencil
    a1=rupee_pencil
    print(a)
    print("Print End to stop")
elif item=="eraser":
    v=print(item,rupee_eraser)
    print("Print End to stop")
elif item=="ruler":
    v=print(item,rupee_ruler)
    print("Print End to stop")
item2=input()

if item2=="pen":
    v2=item2,rupee_pen
    print(v2)
    print("Print End to stop")
elif item2=="pencil":
    v2= print(item2,rupee_pencil)
    print("Print End to stop")
elif item2=="eraser":
    v2=print(item2,rupee_eraser)
    print("Print End to stop")
elif item2=="ruler":
    v2=print(item2,rupee_ruler)
    print("Print End to stop")
elif item2=="end":
    print(a)
