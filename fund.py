import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='what is the first number?')

    parser.add_argument('--y', type=float, default=1.0,
                        help='what is the second number?')

    parser.add_argument('--operation', type=str, default='add',
                        help='what the operation? Can choose add, sub, mul, or div')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):

    if args.operation == 'add':
        return args.x +args.y

    elif args.operation == 'sub':
        return args.x - args.y

    if args.operation == 'mul':
        return args.x * args.y

    if args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()