#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    list_n = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            x = 0
        except ZeroDivisionError:
            print("division by 0")
            x = 0
        except IndexError:
            print("out of range")
            x = 0
        finally:
            list_n.append(x)
    return list_n
