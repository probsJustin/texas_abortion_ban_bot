import internal_module_configuration
import internal_module_thread_handler
import internal_module_system_arguments
import logging


logging.basicConfig(filename='./ping.log', level=logging.DEBUG)
instance_configuration = internal_module_configuration.TABB_configuration()
instance_thread_handler = internal_module_thread_handler.ThreadHandler()
instance_system_arguments = internal_module_system_arguments.args()

