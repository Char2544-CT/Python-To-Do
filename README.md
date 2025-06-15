Python To-Do App

Global Variables:
Global variables so all functions can access them. They are all lists.

add_task:
-Asks user what task they would like to add, then 'tries' to ask user for when that task is due in hours. An input like '1.5' hours would be okay. If block insures input is greater than 0, then appends user input to list. ValueError insures a number is added.

view_task:
accepts two arguments, then using a for loops, prints tasks. By using 'enumerate' it iterates through tasks and starts at 1 instead of 0 index. However, we also want to print 'due' at the proper index so we subtract 1 from due's index.

delete_task:
If there are no tasks, alerts user, returns to menu. Takes the users choice subtracts one to match the index in the list and uses .pop method to remove it from the list. Also checks that the user choice is greater than or equal to 1 and amount of tasks.

quit_app:
quit app prints a message and the Menu function is not called again so the app quits.

Menu:
prints menu list using a for loop and user selection coordinates with a switch statement. Each case, starts a new function. Exception handling for ValueError, and switch statement handles invalid numbers.
