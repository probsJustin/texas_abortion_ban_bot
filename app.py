import configuration
import logging
import thread_handler
import system_arguments
import sys


logging.basicConfig(filename='./ping.log', level=logging.DEBUG)
instance_configuration = configuration.TABB_configuration()
instance_thread_handler = thread_handler.ThreadHandler()
instance_system_arguments = system_arguments.args()

