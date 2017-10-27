import argparse
from rank_calculator import RankCalculator
from file_handler import FileHandler


def parse_file_types(file_type):
    if file_type.lower() not in FileHandler.FILE_TYPES:
        msg = 'File type "%s" not supported' % file_type
        raise argparse.ArgumentTypeError(msg)

    return file_type


def main():
    parser = argparse.ArgumentParser(description='Calculate percentile rank')
    parser.add_argument(
        'input', type=argparse.FileType('r'),
        help='input file containing data to parse')

    parser.add_argument(
        'output', type=argparse.FileType('w'),
        help='output file to write data to')

    parser.add_argument(
        '-t', default='auto', type=parse_file_types,
        choices=FileHandler.FILE_TYPES, metavar="TYPE",
        help='input file type')

    parser.add_argument(
        '-i', default='0', metavar="INDEX",
        help='index/key containing the values to work on')

    parser.add_argument(
        '-s', default=None, metavar="SKIP",
        help='index(es)/key(s) to skip when writing output')

    parser.add_argument(
        '-r', default='percentile_rank', metavar="RANK",
        help='index/key to hold the percentile rank to when writing output')

    args = parser.parse_args()

    rank_calculator = RankCalculator()
    rank_calculator.calculate()

    file_handler = FileHandler(args.input, args.output, args.t)
    file_handler.write()


if __name__ == '__main__':
    main()
