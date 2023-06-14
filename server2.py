import grpc
import sys
import integration_pb2
import integration_pb2_grpc
import threading
from concurrent import futures


class IntegrationServicer(integration_pb2_grpc.IntegrationServicer):
    def __init__(self, stop_event):
        self.directories = {}
        self._stop_event = stop_event

    def Register(self, request, context):
        server_name = request.server_name
        server_port = request.server_port
        keys = request.keys
        for i in keys:
            if i in self.directories:
                self.directories[i].append((server_name, server_port))
            else:
                self.directories[i] = [(server_name, server_port)]

        return integration_pb2.RegisterResponse_(result=len(keys))

    def Query(self, request, context):
        key = request.key
        response = integration_pb2.QueryResponse_()

        if key in self.directories:
            r = self.directories[key][0]
            response.server_name = r[0]
            response.server_port = r[1]
            return response
        response.server_name = "ND"
        response.server_port = 0
        return response

    def Terminate(self, request, context):
        self._stop_event.set()
        return integration_pb2.TerminateResponse_(num_keys=len(self.directories))


def run_server(port):
    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor())
    integration_pb2_grpc.add_IntegrationServicer_to_server(
        IntegrationServicer(stop_event), server)
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    stop_event.wait()
    server.stop(grace=1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python integration_server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])

    run_server(port)
