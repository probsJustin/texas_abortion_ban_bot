import configuration
import logging
import thread_handler


logging.basicConfig(filename='./ping.log', level=logging.DEBUG)
instance_configuration = configuration()
instance_thread_handler = thread_handler()


