import internal_module_configuration
import internal_module_thread_handler
import internal_module_system_arguments
import internal_module_selenium_scripts.example_google
import logging


logging.basicConfig(filename='./ping.log', level=logging.DEBUG)
instance_configuration = internal_module_configuration.TABB_configuration()
instance_thread_handler = internal_module_thread_handler.ThreadHandler()
instance_system_arguments = internal_module_system_arguments.args()

# instantiate the instances of the scripts to be run
instance_selenium_script_example_google = internal_module_selenium_scripts.example_google

if __name__ == '__main__':
    instance_thread_handler.mp_handler(1)
    # instance_thread_handler.mp_workerFunctionLoggingTiming("name", "how_often", "function passed here", "args for that function")
    instance_thread_handler.mp_workerFunctionLoggingTiming("Example Google Script", 10, instance_selenium_script_example_google.run, chrome_driver="C:\chromedrivers\chromedriver_win32_92.0.4515.107\chromedriver")
