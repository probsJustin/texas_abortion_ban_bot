
import subprocess
import multiprocessing


class ThreadHandler:
    data = list()
    p = None

    def mp_handler(self, instances_of_thread):
        self.p = multiprocessing.Pool(instances_of_thread)
        self.p.map(self.mp_workerFunctionLoggingTiming, self.data)

    def mp_execute(self, name, how_often, func_name_instance, *args):
        print(f"[ {name} ] {how_often} : {directory}")
        func_name_instance(*args)

    def mp_workerFunctionLoggingTiming(self, name, how_often, func_name_instance, *args):
        print(" Processs Starting: " + name)
        self.mp_execute( name, how_often, func_name_instance, *args)
        print(" Process Stopping: " + name)