# ### **1. To-Do List CLI App**

# - **Concepts:** Variables, loops, functions, lists.
# - **Key Features:** Add, delete, and mark tasks as completed.
# - **What You’ll Learn:**
#     - User input handling (`input()`)
#     - Storing and retrieving data using lists
#     - Functions for modularity


ListItems = []


def addItem():
    item = input('Add list Item: ')
    ListItems.append(item)
    

