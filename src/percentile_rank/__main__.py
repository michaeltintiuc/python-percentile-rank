import argparse


file_types = ['csv', 'json', 'yaml', 'auto']


def parse_file_types(file_type):

    if file_type.lower() not in file_types:
        msg = 'File type "%s" not supported' % file_type
        raise argparse.ArgumentTypeError(msg)

    return file_type


def main():
    parser = argparse.ArgumentParser(description='Calculate percentile rank')
    parser.add_argument(
        'input',
        help='input file containing data to parse')

    parser.add_argument(
        'output',
        help='output file to write data to')

    parser.add_argument(
        '-t', default='auto', type=parse_file_types,
        choices=file_types, metavar="TYPE",
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


if __name__ == '__main__':
    main()
