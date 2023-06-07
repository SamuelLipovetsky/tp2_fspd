import grpc
import sys

import directory_pb2
import directory_pb2_grpc


def run_client(server_address):
    channel = grpc.insecure_channel(server_address)
    stub = directory_pb2_grpc.DirectoryStub(channel)

    try:
        while True:
            command = input("Enter a command (I, C, R, T): ")
            command_parts = command.split(',')

            if command_parts[0] == 'I':
                key = int(command_parts[1])
                desc = command_parts[2]
                value = float(command_parts[3]) 
                response = stub.Insert(directory_pb2.InsertRequest(key=key, desc=desc, value=value))
                print(response.status)
            elif command_parts[0] == 'C':
                key = int(command_parts[1])
                response = stub.Query(directory_pb2.QueryRequest(key=key))
                if response.item.desc:
                    formatted_number = "%7.4f" % response.item.value
                    print(str(response.item.desc)+","+ str(formatted_number))
                else:
                    print("-1")
            elif command_parts[0] == 'R':
                server_name = command_parts[1]
                server_port = int(command_parts[2])
                response = stub.Register(directory_pb2.RegisterRequest(server_name=server_name, server_port=server_port))
                print(response.result)
            elif command_parts[0] == 'T':
                response = stub.Terminate(directory_pb2.TerminateRequest())
                print(response.num_keys)
                break
            else:
                print("Invalid command!")

    except grpc.RpcError as e:
        print(f" gRPC error: {e.details()}")
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python client.py <server_address>")
        sys.exit(1)

    server_address = sys.argv[1]
    run_client(server_address)
