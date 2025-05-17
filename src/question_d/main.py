from question_d import get_stock_list, display_stock_list

def main():
    stock_list = get_stock_list()
    while True:
        print("\nStock Menu:")
        print("1- Display stock purchase history")
        print("2- Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_stock_list(stock_list)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid. Please try again")

main()