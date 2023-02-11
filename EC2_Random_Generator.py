import random
import string

def generate_name(dept, num):
    # Function to generate the unique EC2 instance names.
    names = []
    for i in range(num):
        # Generates a random string of 8 characters.
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        # Concatenates the department name and the random string to form the unique EC2 name.
        names.append(dept + '-' + random_string)
    return names

def main():
    # List of allowed departments
    allowed_depts = ['Marketing', 'Accounting', 'FinOps']
    # Gets the number of EC2 instances for which the user needs names for.
    instances_num = int(input("How many EC2 instances would you like to create names for? "))
    # Checks that the number of instances entered is at least 1.
    while instances_num < 1:
        print("Error: You must need at least 1 EC2 instance name.")
        instances_num = int(input("How many EC2 instances would you like to create names for? "))
    # Gets the name of the user's department.
    dept = input("Enter the name of your department: ").capitalize()
    # Checks if the input department name is in the list of allowed departments.
    if dept not in allowed_depts:
        # Capitalizes the input department name again in case the user inputs it in lowercase.
        dept = dept.capitalize()
        if dept not in allowed_depts:
            # If the department name still cannot be found in the allowed departments list, prints an error message and exits.
            print("Sorry, the Name Generator is only available for the Marketing, Accounting, and FinOps departments.")
            return
    # Calls the function to generate the unique EC2 instance names.
    names = generate_name(dept, instances_num)
    # Prints the generated names.
    print("Your unique EC2 instance names are:")
    for name in names:
        print(name)

# Calls the main function if the script is being run as the main program.
if __name__ == '__main__':
    main()

print("\n---Thank you for using Matt's EC2 Instance Random Name Generator!---")
