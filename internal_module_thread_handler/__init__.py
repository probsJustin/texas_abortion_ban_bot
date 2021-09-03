
import subprocess
import multiprocessing


class ThreadHandler:
    data = list()
    p = None
    function_holder = None
    chrome_driver = None

    def set_number_of_instances_to_run(self, func_number_of_instances):
        for x in range(0, func_number_of_instances):
            self.data.append(x)

    def set_chrome_driver(self, func_chrome_driver):
        self.chrome_driver = func_chrome_driver

    def set_function(self, func_function_holder):
        self.function_holder = func_function_holder

    def mp_handler(self, instances_of_thread):
        p = multiprocessing.Pool(instances_of_thread)
        p.map(self.mp_workerFunctionLoggingTiming, self.data)

    def mp_execute(self, chrome_driver, *args):
        self.function_holder(self.chrome_driver)

    def mp_workerFunctionLoggingTiming(self, id):
        print(" Processs Starting: " + str(id))
        self.mp_execute(self.chrome_driver)
        print(" Process Stopping: " + str(id))