#!/bin/python3
# If you’ve ever put a print() statement in your code to output some variable’s 
# value while your program is running, you’ve used a form of logging to debug your
# code. Logging is a great way to understand what’s happening in your program and
# in what order it’s happening. Python’s logging module makes it easy to create a
# record of custom messages that you write. These log messages will describe when
# the program execution has reached the logging function call and list any 
# variables you have specified at that point in time. On the other hand, a missing
# log message indicates a part of the code was skipped and never executed.

import logging
#the filepath is optional 
#debug level can be DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')