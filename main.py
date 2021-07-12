import argparse
import shutil
import logging
from file_util import FileUtil

logging.basicConfig(filename="log.log", level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--operation', help='foo help', type=str)
    parser.add_argument('--from', help='file source', type=str)
    parser.add_argument('--to', help='destination file', type=str)
    parser.add_argument('--threads', help='count of threads', type=int)
    args = vars(parser.parse_args())

    util = FileUtil(args['from'], args['to'])
    operation = args['operation']
    print(operation)

    if operation == "copy":
        util.copy(args['threads'])
    elif operation == "move":
        util.move(args['threads'])


if __name__ == '__main__':
    main()
