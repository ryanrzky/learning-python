message = "\nhey you, enter a number of days and unit and will convert to hours or minutes!\n"

# Function
def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return(f"{num_of_days} days are {num_of_days * 24} hours")
    elif conversion_unit == "minutes":
        return(f"{num_of_days} days are {num_of_days * 24 * 60} minutes")
    else:
        return "unsupported unit"

# Combination function with input user
def validate_and_exec(num_of_days_element_dict): # perlu di kasih num_of_days_element_dict agar function tau variable num_of_days_element_dict
    # if user_input.isdigit():
    try:
        # casting user_input to integer
        num_user_input = int(num_of_days_element_dict["days"])
        if num_user_input > 0:
            calculation_value = days_to_unit(num_user_input, num_of_days_element_dict["unit"]) # ini sama dengan merubah num_user_input ke days_to_unit
            print(calculation_value)
        elif num_user_input == 0:
            print("you entered a 0, please enter a valid positf number")
        else:
            print("you entered a negative number")
    # else:
    except ValueError:
        print("your input is not a valid number")