##
# @author : Remi Dupuy : IT Student
# Add arguments

import argparse

parser = argparse.ArgumentParser()
# Create both arguments
parser.add_argument('-publish', action='store_true', help='Publish a message in queue')
parser.add_argument('-read', action='store_true', help='Read a message in queue')

publish = parser.parse_args().publish
read = parser.parse_args().read

# Exec selected scripts
if publish:
    execfile('simple_queue_publish.py')

if read:
    execfile('simple_queue_read.py')

