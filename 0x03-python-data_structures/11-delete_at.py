#!/user/bin/python3
def delete_at(my_list=[], idx=0):
    for x in range(len(my_list)):
        if(x is idx):
            del my_list[x]
    return(my_list)
