




if __name__ == '__main__':


    while(True):
        abekeres = int(input("Enter 'a' value: "))
        bbekeres = int(input("Enter 'b' value: "))

        try:

            k = abekeres/bbekeres
            print(k)

        except ZeroDivisionError:

            print("Division by zero not allowed.")

        finally:

            print("Out of try except blocks.")
