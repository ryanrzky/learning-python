# calculation_to_hours = 24
# name_of_unit = "hours"

from function import validate_and_exec, message

# Call Function
# days_to_unit(20")
user_input = ""
while user_input != "exit":
    user_input = input(message)
    num_of_days_element = user_input.split(":")
    num_of_days_element_dict = {"days": num_of_days_element[0], "unit": num_of_days_element[1]}
    validate_and_exec(num_of_days_element_dict) #perlu dikasih variable num_days_element_dict untuk komunikasi ke function.py
        