import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # these are positional arguments
    # parser.add_argument("number1", help="first number")
    # parser.add_argument("number2", help="second number")
    # parser.add_argument("operation", help="operation")
    
    # these are optional arguments
    parser.add_argument("--number1", help="first number")
    parser.add_argument("--number2", help="second number")
    #parser.add_argument("--operation", help="operation")
    # To restrict users from entering other operations
    parser.add_argument("--operation", help="operation", \
        choices=["add", "subtract", "multiply"])
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    # whatever value we provide in the command line, it will come back as a string.
    # So, we need to convert it to an integer value
    n1 = int(args.number1)
    n2 = int(args.number2)
    # initialize the result to none
    result = None
    
    if args.operation == 'add':
        result = n1 + n2
    elif args.operation == 'subtract':
        result = n1 - n2
    elif args.operation == 'multiply':
        result = n1 * n2
    else:
        print("Unsupported operation.")
        
    print("Result:", result)
    