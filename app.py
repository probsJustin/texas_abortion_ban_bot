import configuration
import logging
import thread_handler
import system_arguments
import sys


logging.basicConfig(filename='./ping.log', level=logging.DEBUG)
instance_configuration = configuration()
instance_thread_handler = thread_handler()
instance_system_arguments = system_arguments()

