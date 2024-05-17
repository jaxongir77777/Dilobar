def check_number_type(input_string):
    try:

        int_value = int(input_string)
        return 1 
    except ValueError:
        try:
            float_value = float(input_string)
            if float_value.is_integer():
                return 1  
            else:
                return 2  
        except ValueError:
            return 0 

input_string = "3.14"

result = check_number_type(input_string)
print("Type of number represented by the string:", result)
