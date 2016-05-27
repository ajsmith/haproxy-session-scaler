"""\
Horizontally scale pods based on HAProxy session activity.
"""

import StringIO
import argparse
import csv
import os
import sys
import urllib


def get_session_data(url):
    return urllib.urlopen(url).read()


def scale(project, session_data):
    rows = csv.reader(StringIO.StringIO(session_data))
    (stats,) = filter(lambda r: r[0] == project and r[1] == 'BACKEND', rows)
    session_count = int(stats[4])
    return (1 + int(session_count / 10))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('project', help='Name of the project to inspect.')
    parser.add_argument('haproxy_url', help='Address of the HAProxy instance.')
    args = parser.parse_args()

    session_data = get_session_data(args.haproxy_url)
    print scale(args.project, session_data)
