from question_c import create_multiplication_table , display_multiplication_table

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        cont = input("\nWould you like to generate the table again? yes or no?: ").lower()
        if cont != 'yes':
            print("Exiting...")
            break
main()
