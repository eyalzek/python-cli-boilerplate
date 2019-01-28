#!/usr/bin/env python3

import argparse
from logger import logger


def parse_args():
    parser = argparse.ArgumentParser(description='Python CLI boilerplate')
    return parser.parse_args()


def main():
    args = parse_args()


if __name__ == '__main__':
    main()
