#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num = 1
    argc = len(sys.argv) - num
    print('{} argument{}{}'.format(
        argc, 's' * (argc != 1),
        ':' if argc > 0 else '.'
        ))
    for arg in sys.argv[num:]:
        print('{}: {}'.format(num, arg))
        num += 1
