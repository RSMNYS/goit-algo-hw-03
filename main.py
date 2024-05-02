import argparse
import os

from os_utils import handle_directory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src', type=str, help='Source directory')
    parser.add_argument('-d', '--dst', type=str, help='Destination directory')

    args = parser.parse_args()

    source_directory = args.src if args.src else os.getcwd()
    current_directory = os.getcwd()
    parent_directory_name = os.path.dirname(current_directory)
    destination_directory = args.dst if args.dst else f'{parent_directory_name}/dist'

    handle_directory(source_directory, destination_directory)
   
if __name__ == '__main__':
    main()