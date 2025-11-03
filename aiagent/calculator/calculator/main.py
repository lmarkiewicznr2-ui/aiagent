import sys
from pkg.calculator import calculate

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        result = calculate(expression)
        print(result)
    else:
        print("No expression provided.")