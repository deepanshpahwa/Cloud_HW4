#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
count = 0

for line in sys.stdin:
        if count == 0:
            count =count + 1
            continue
        line_ar = line.rstrip().split(',')
        for it in range(24,29):
            try:
                line_ar[it] = int(line_ar[it])
            except:
                try:
                    if line_ar[it] == '':
                        continue
                    else:
                        print '%s\t%s' % (line_ar[it].upper(),1)
                except:
                        pass
