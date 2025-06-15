#Global variables
task_list = ['Car Wash', 'Eat', 'Workout', 'Play video games']
due_list = [10, 0.5, 1, 0.2]
menu_list = ['1. Add Task ', '2. View Task ', '3. Delete Task ', '4. Quit App']

#Add A task Function
def add_task():
    user_add = input('\nWhat task would you like to add? ')
    try:
        when_due = float(input('\nPlease enter when task is due in hours. Decimal places are okay: '))
        if when_due > 0:
            task_list.append(user_add)
            due_list.append(when_due)
            print('\nTask Added!')
        #task_list is appeneded in the try block because it should only append to list if when_due is valid. Else, indexing gets out of order.
        else:
            print('\nMust be a positive number!')
            Menu()
    except ValueError:
        print('\nPlease enter a number!')
        Menu()

#View tasks Function
def view_task(tasks, due):
    print('')
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task} Due in {due[idx - 1]} hour(s)")
        #Subtract 1 from index so due_list and tast_list match.

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    print('')
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
    try:
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"\nDeleted: {removed}")
            #Choice - 1 because indexes start at zero. If a user picks '1' we need to remove the list item at index 0
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

#Quit Application
def quit_app():
    print('\nGoodbye!\n')

#Capture user menu selection
def Menu():
    print('\nWelcome to your To-Do Application, please select a number to continue: ')

    print('')

    for i in menu_list:
        print(i)

    try:
        option_select = int(input('\nSelection: '))
    except ValueError:
        print('Must be a number!')
        Menu()

    #Switch for user selection
    match option_select:
        case 1:
            add_task()
            Menu()
        case 2:
            view_task(tasks=task_list, due=due_list)
            Menu()
        case 3:
            delete_task(tasks=task_list)
            Menu()
        case 4:
            quit_app()
        case _:
            print('Invalid Choice')
            Menu()

Menu()