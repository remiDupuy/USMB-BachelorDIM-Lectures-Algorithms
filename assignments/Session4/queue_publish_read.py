##
# @author : Remi Dupuy : IT Student
# Add arguments

import argparse

import subprocess

parser = argparse.ArgumentParser()
# Create both arguments
parser.add_argument('-publish', action='store_true', help='Publish a message in queue')
parser.add_argument('-read', action='store_true', help='Read a message in queue')
parser.add_argument('-concurrency', action='store_true', help='Publish/Read in concurrency mode')

publish = parser.parse_args().publish
read = parser.parse_args().read
concurrency = parser.parse_args().concurrency

string_concurrency = ''
if(concurrency):
    string_concurrency = ' -concurrency'

# Exec selected scripts
if publish:
    subprocess.call('python /home/remidupuy/Workspace/AlgoC/code/USMB-BachelorDIM-Lectures-Algorithms/assignments/Session4/simple_queue_publish.py'+string_concurrency)

if read:
    subprocess.call('python /home/remidupuy/Workspace/AlgoC/code/USMB-BachelorDIM-Lectures-Algorithms/assignments/Session4/simple_queue_read.py'+string_concurrency)

