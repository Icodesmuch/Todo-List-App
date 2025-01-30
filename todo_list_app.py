# ### **1. To-Do List CLI App**

# - **Concepts:** Variables, loops, functions, lists.
# - **Key Features:** Add, delete, and mark tasks as completed.
# - **What You’ll Learn:**
#     - User input handling (`input()`)
#     - Storing and retrieving data using lists
#     - Functions for modularity


ListItems = []
completedItems = []


def addItem(item):
    
    ListItems.append(item)
    

def deleteItems():
    if not ListItems:
        print('The list is empty. Invalid input.')
        return 
    
    # Display list then prompt the user to enter the number that corresponds to the item. 

    displayList(ListItems)
    option = int(input('Enter the number that corresponds to the element you would like to delete.'))

    # remove the element at 'option' index

    ListItems.pop(option - 1)
    print('Here is the new list: ')
    displayList(ListItems)

         
def displayList(List):
     i = 1
     for item in List:
        print(f'\n{i}.' + item)
        i += 1


def markTask():


    displayList(ListItems)
    
    option = int(input('Enter the number that corresponds to the element you want to mark as completed: '))
    item = ListItems.pop(option - 1)
    completedItems.append(item)
    
    

def toDoApp():
    while True:
        print('\nTO-DO LIST APP')
        print('1. Enter Task.')
        print('2. Delete Task.')
        print('3. Mark Task As Completed.')
        print('4. Display List.')
        print('5. Display Completed List.')
        print('6. Exit Program.')
        option = str(input())


        if option == '1':

            while True:
                item = input("Add list Item. (Enter 'quit' to end): ")
                if item == 'quit':
                    break
                addItem(item)
                print('Item Added Succesfully.')


        elif option == '2':
            deleteItems()
            print('Item Deleted.')


        elif option == '3':
            markTask()
            print('Task Marked As Completed.') 


        elif option == '4':
            print('\n\t***************To-Do Items***************')
            displayList(ListItems)


        elif option == '5':
            print('\n\t***************Completed Items***************')
            displayList(completedItems)


        elif option == '6':
            print('Have a good day :)') 
            break


if __name__ == "__main__":
    toDoApp()