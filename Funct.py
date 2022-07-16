def input_number_test_float(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        elif coord.isdecimal:
            coord = float(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else :
            print("Введенное значение не является числом")
    return coord

def input_pos_num(text):

    int_test = True
    is_minus = False
    while int_test:
        coord = input(f"{text}")
        if coord[0] == "-":
            is_minus = True
            coord = coord.replace("-","")
        if coord.isdigit():
            coord = int(coord)
            if coord <= 0:
                print("Enter number > 0")
            else:
                int_test = False
        else :
            print("Not a number , try again")
    return coord