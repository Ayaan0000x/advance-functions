list=["rubber","pencil","pen","scale","highlighter","sharpner"]


stock_count=[10,20,25,15,30,0]


inventory={key:value for key,value in zip(list,stock_count)}

print(inventory)


instockitems=[i for i in list if inventory[i] >0  ]


print(instockitems)


chosen_item=input("which item do you require?")


if chosen_item not in inventory or inventory[chosen_item==0] :
    print("there is no item")

    