import argparse
import sys

from wd_curator import Wiki


def arg_parser(args):
    parser = argparse.ArgumentParser(description='Run a worker for a given wiki')
    parser.add_argument('--path', '-p', nargs='?', required=True,
                        help='Path to yaml file of the wiki')

    parser.add_argument('--once', '-o', action='store_true', required=False,
                        help='Break after an one-time run')
    return parser.parse_known_args(args)[0]


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = arg_parser(argv)

    wiki = Wiki.from_config(open(args.path, 'r'))
    wiki.run(forever=not args.once)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
