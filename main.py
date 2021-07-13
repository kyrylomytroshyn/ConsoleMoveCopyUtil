from argparse import ArgumentParser
from os.path import isdir
from logging import basicConfig, DEBUG
from file_util import FileUtil


def main():
    basicConfig(filename='util_logs.log',
                level=DEBUG, filemode="w")

    parser = ArgumentParser()
    parser.add_argument('--operation', help='foo help', type=str)
    parser.add_argument('--from', help='file source', type=str)
    parser.add_argument('--to', help='destination file', type=str)
    parser.add_argument('--threads', help='count of threads', type=int)
    args = vars(parser.parse_args())
    source = args['from']
    operation = args['operation']
    if not isdir(args['to']):
        raise IOError("You entered the wrong destination link to copy/move.")

    util = FileUtil(source, args['to'])
    pos = source.find("*.")
    if pos > 0:
        util.copy_move_mask(action=operation, pos=pos, threads=args['threads'], )
    else:
        util.copy_move(operation, args['threads'], )


if __name__ == '__main__':
    main()
