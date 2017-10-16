##
# @author : Remi Dupuy : IT Student
# Add arguments

import argparse

import subprocess

parser = argparse.ArgumentParser()
# Create both arguments
parser.add_argument("-n", "--sendMany", help='Publish a message in queue')
number_readers = parser.parse_args().sendMany

for idx in xrange(int(number_readers)):
    subprocess.call(['python /home/remidupuy/Workspace/AlgoC/code/USMB-BachelorDIM-Lectures-Algorithms/assignments/Session4/simple_queue_read.py -concurrency'], shell=True)