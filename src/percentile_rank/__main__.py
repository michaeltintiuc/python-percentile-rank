import argparse
from rank_calculator import RankCalculator
from file_handler import FileHandler


def init(args):
    rank_calculator = RankCalculator()
    rank_calculator.calculate()

    file_handler = FileHandler.make(args.input, args.output, args.file_type)
    file_handler.exportFile(args.skip_index)


def main():
    parser = argparse.ArgumentParser(description='Calculate percentile rank')
    parser.add_argument(
        'input', type=argparse.FileType('r'),
        help='input file containing data to parse')

    parser.add_argument(
        'output', type=argparse.FileType('w'),
        help='output file to write data to')

    parser.add_argument(
        '-t', default='auto', metavar="TYPE", dest="file_type",
        type=FileHandler.parse_file_types, choices=FileHandler.FILE_TYPES,
        help='input file type')

    parser.add_argument(
        '-i', default='0', metavar="INDEX", dest="data_index",
        help='index/key containing the values to work on')

    parser.add_argument(
        '-s', default=None, metavar="SKIP", dest="skip_index",
        help='index(es)/key(s) to skip when writing output')

    parser.add_argument(
        '-r', default='percentile_rank', dest="rank_index", metavar="RANK",
        help='index/key to hold the percentile rank to when writing output')

    init(parser.parse_args())


if __name__ == '__main__':
    main()
