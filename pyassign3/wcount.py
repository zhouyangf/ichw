"""wcount.py: count words from an Internet file.

__author__ = "Zhou Yangfan"
__pkuid__  = "1600017735"
__email__  = "pkuzyf@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import string

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    
    punctuation = string.punctuation.replace("'", "")
    for i in punctuation:
        lines = lines.replace(i, " ")  # To replace all kinds of punctuations in the text string except "'" by " ".
    
    alist = lines.split()  # To convert the string to a list where every word in the string is set as an independent element.
    counts = {}
    for x in alist:
        counts[x] = counts.get(x, 0) + 1  # To count the times that every word appears in the text for, and put them in the dictionary, such as "'Alice':100".
    
    lst = list(counts.items())  # To convert the dictionary to a list which contains many tuples, the tuples are just like ("Alice", 100).
    nlst = []
    for x in lst:
        tup = (x[1], x[0])
        nlst.append(tup)  # To creat a new list which contains tuples like (100, "Alice") that inverses the elements in the tuples in the last list.
    
    nlst.sort(reverse = True)  # To sort the tuples by their first elements, they are "times".

    for i in range(topn):
        print(nlst[i][1].ljust(12), nlst[i][0])  # To print the top topn(topn is a int).

    pass

if __name__ == '__main__':
    
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
