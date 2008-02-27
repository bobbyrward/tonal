#!/usr/bin/env python

import os
import os.path
from fnmatch import fnmatch
from itertools import ifilter, imap
from functools import partial


def match_patterns(fname, patterns):
    for pattern in patterns:
        if fnmatch(fname, pattern):
            return True
    return False

def processdir(dir, patterns, fn):
    for root, dirs, files, in os.walk(dir):
        map(fn, 
                ifilter(
                    partial(match_patterns, patterns=patterns), 
                    imap(
                        partial(os.path.join, root), 
                        files
                    )
                )
            )

if __name__ == '__main__':
    from sys import argv

    argc = len(argv)

    if argc == 1:
        print 'usage: %s <directory> [extension ...]' % argv[0]
        print '       extension list defaults to *.*'
        print
    elif argc == 2:
        dir = argv[1]
        patterns = ['*.*']
    else:
        dir = argv[1]
        patterns = argv[2:]

    def print_func(msg):
        print msg

    processdir(dir, patterns, print_func)

