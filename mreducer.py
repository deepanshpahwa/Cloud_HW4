#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
word = None

count = 0


for line in sys.stdin:
    line = line.strip()
    word, count_ = line.split('\t', 1)

    try:
        count_ = int(count_)
    except ValueError:
        continue

    if current_word != word:
        if current_word:
            print '%s\t%s' % (current_word, count)
        count = count_
        current_word = word

    else:
        count = count + count_

if current_word == word:
    print '%s\t%s' % (current_word, count)
