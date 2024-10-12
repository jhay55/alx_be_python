def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """This is a shopping list simple program where you can add, remove and view
    items in your shopping cart. It is simple but efficient"""

    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            # Prompt for and add an item
            user_input = input('Enter the item to add: ').strip().lower()
            shopping_list.append(user_input)
            print(f'You have added {user_input} to your shopping list.')
            print()
        elif choice == '2':
            # Prompt for and remove an item
            user_input = input('What item do you want to remove from your list: ').strip().lower()

            if user_input not in shopping_list:
                print('Sorry, Item not found in current list')
            else: 
                shopping_list.remove(user_input)
            #print(f'You have removed {user_input} to your shopping list.')
            print()

        elif choice == '3':
            # Display the shopping list
            print('Your shopping list includes the folowing items: ')
            for item in shopping_list:
                print(item)
            print()
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
