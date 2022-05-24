#!/usr/bin/env python3

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    user_vendor = input("Please input vendor name:")

    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("\nYou told me the IPv4 address is:", user_input)
    print("You told me the vendor was:", user_vendor)

main()

