
import subprocess
import multiprocessing


class ThreadHandler:
    data = list()

    def mp_handler(self):
        p = multiprocessing.Pool(12)
        p.map(self.mp_workerFunctionLoggingTiming, self.data)

    def mp_execute(self, directory, name, howOften):
        print("[" + name + "]" + directory)
        # thing to execute as a thread

    def mp_workerFunctionLoggingTiming(self, directory, name, howOften):
        print(" Processs Starting: " + name)
        self.execute(name)
        print(" Process Stopping: " + name)