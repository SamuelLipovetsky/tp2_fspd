import grpc
from concurrent import futures
import time
import socket 
import directory_pb2
import directory_pb2_grpc
import integration_pb2
import integration_pb2_grpc
import sys
import threading

class DirectoryServicer(directory_pb2_grpc.DirectoryServicer,integration_pb2_grpc.IntegrationServicer):
    def __init__(self,port,stop_event):
        self.directory = {}
        self.name =  socket.getfqdn()
        self.port = port
        self._stop_event = stop_event

    def Insert(self, request, context):
        key = request.key
        desc = request.desc
        value = request.value

        if key in self.directory:
            self.directory[key].desc = desc
            self.directory[key].value = value
            return directory_pb2.InsertResponse(status=1)
        else:
            self.directory[key] = directory_pb2.Item(desc=desc, value=value)
            return directory_pb2.InsertResponse(status=0)

    def Query(self, request, context):
        key = request.key

        if key in self.directory:
            return directory_pb2.QueryResponse(item=self.directory[key])
        else:
            return directory_pb2.QueryResponse()

    def Register(self, request, context):
        server_name = request.server_name
        server_port = request.server_port
        channel = grpc.insecure_channel(server_name +":"+str(server_port))
        stub = integration_pb2_grpc.IntegrationStub(channel)
        result = 0
        result = stub.Register(integration_pb2.RegisterRequest_(server_name=self.name,server_port=self.port,keys = self.directory.keys()))
        return directory_pb2.RegisterResponse(result=result.result)

    def Terminate(self, request, context):
        num_keys = len(self.directory)
        self._stop_event.set()
        return directory_pb2.TerminateResponse(num_keys=num_keys)

def serve(port):
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    directory_pb2_grpc.add_DirectoryServicer_to_server(
        DirectoryServicer(port,stop_event), server)
    server.add_insecure_port('[::]:'+str(port))
    server.start()
    stop_event.wait()
    server.stop(grace=1)
    # try:
    #     while True:
    #         time.sleep(100000)
    # except KeyboardInterrupt:
    #     server.stop(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python integration_server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    serve(port)