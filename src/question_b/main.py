from question_b import get_most_likely_ancestor_consensus

def main():
    while True:
        print("\n--- DNA Substring Locator ---")

        while True:
            dna_string1 = input("Enter a DNA string, 9-16 characters: ").upper()
            if len(dna_string1) <= 16:
                break
            print("Invalid. Must be 9 to 16 characters")

        while True:
            dna_string2 = input("Enter a DNA substring, 4 characters: ")
            if len(dna_string2) == 4:
                break
            print("Invalid. Must be 4 characters exactly")

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

        if result:
            print("Positions:", *result)
        else:
            print("No matches found")

        again = input("Try again? yes or no: ").lower()
        if again != 'yes':
            print("Goodbye")
            break
main()
