#Creating a simple program to tell the number of places in a number
def code():
    new = int(input("Enter a number :"))
    count = 0
    while new  > 1:
        new = new/10
        count += 1
    return count
    
def main():

    count = code()

    if count == 0 :
        print("enter a valid number")
    elif count == 1 :
        print("Tens")
    elif count == 2 :
        print("Hundreds")
    elif count == 3 :
        print("Thousands")
    elif count == 4 :
        print("Ten Thousands")
    elif count == 5 :
        print("Hundred Thousands")
    elif count == 6 :
        print("Millions")
    elif count == 7 :
        print("Billion")
main()