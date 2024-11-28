import sys
# This is my own library created
from saving import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])