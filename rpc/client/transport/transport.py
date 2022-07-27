from rpc.client.transport.transport_task import TransportTask
from rpc.types.procedure import Procedure, ProcedureResponse
from rpc.types.transport_type import TransportType
from rpc.client.protocol.protocol import Protocol
from rpc.types.protocol import ProtocolType
from rpc.loger import Logger
import rpc.utils

import threading
import _thread


class Transport:
    def __init__(self, transport_type: TransportType, protocol: Protocol):
        self._transport_type = transport_type
        self._protocol = protocol

        self._tasks_to_send = []
        self._finish_send_worker_eve = threading.Event()
        self._wait_send_tasks_cv = threading.Condition(threading.Lock())

        self._finish_recv_worker_eve = threading.Event()

        self._wait_workers_finish_barier = threading.Barrier(3)
        return


    def start(self):
        send_thread_id = _thread.start_new_thread(self.send_worker)
        recv_thread_id = _thread.start_new_thread(self.recv_worker, [self._finish_recv_worker_eve])

    def finish_transport(self):
        self._finish_send_worker_eve.set()
        self._finish_recv_worker_eve.set()

        self._wait_workers_finish_barier.wait()
        return

    def send_procedure(self, procedure: Procedure, response_handler):
        Logger.info(procedure._name, ": ", procedure._params)

        with self._wait_send_tasks_cv:
            self._tasks_to_send.append(procedure)
            self._wait_send_tasks_cv.notify()
        return

    def send_task(self, task: TransportTask):
        rpc.utils.unimpl_meth()
        return

    def complete_task(self, task: TransportTask):
        task._response_handler(task._procedure_response, task._result)
        return

    def send_worker(self,*args):
        while(True):
            tasks_to_send  = []

            with self._wait_send_tasks_cv:
                self._wait_send_tasks_cv.wait()
                self._tasks_to_send, tasks_to_send = tasks_to_send, self._tasks_to_send 

            for task in tasks_to_send:
                self.send_task(task)
            
            if(self._finish_send_worker_eve.is_set()):
                break
        
        self._wait_workers_finish_barier.wait()
        return

    def recv_worker(self, *args):
        self.recv_loop(self._finish_recv_worker_eve)

        self._wait_workers_finish_barier.wait()
        return

    def recv_loop(self, finish_loop_eve: threading.Event):
        rpc.utils.unimpl_meth()
        return

    