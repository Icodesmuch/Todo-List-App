# ### **1. To-Do List CLI App**

# - **Concepts:** Variables, loops, functions, lists.
# - **Key Features:** Add, delete, and mark tasks as completed.
# - **What You’ll Learn:**
#     - User input handling (`input()`)
#     - Storing and retrieving data using lists
#     - Functions for modularity


ListItems = []
completedItems = []


def addItem():
    item = input('Add list Item: ')
    ListItems.append(item)
    

def deleteItems():
    if not ListItems:
        print('The list is empty. Invalid input.')
        return 
    
    # Display list then prompt the user to enter the number that corresponds to the item. 

    displayList()
    option = input('Enter the number that corresponds to the element you would like to delete.')

    # remove the element at 'option' index

    ListItems.pop(option - 1)
    print('Here is the new list: ')
    displayList()

         
def displayList():
     for item in ListItems:
        i = 0
        print(f'{i}.' + item)


def markTask():


    displayList()
    
    option = input('Enter the number that corresponds to the element you want to mark as completed.')
    item = ListItems.pop(option - 1)
    completedItems.append(item)
    
    
    