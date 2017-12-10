def odd_even(num):
    if(num%2==0):
        print("The number {} is even.".format(num))

    else:
        print("The number {} is odd.".format(num))

num= int(input("Enter a number:"))
odd_even(num)
