import grpc
import sys
import integration_pb2
import integration_pb2_grpc
import directory_pb2
import directory_pb2_grpc

def run_client(server_address):
    channel = grpc.insecure_channel(server_address)
    stub_i = integration_pb2_grpc.IntegrationStub(channel)
   

    try:
        while True:
            command = input("Enter a command (C, T): ")

            if command.startswith("C"):
                command_parts = command.split(',')
                key = int(command_parts[1])

                response = stub_i.Query(integration_pb2.QueryRequest_(key=key))     
                if response.server_name == "ND":
                    print("ND")
                else:
                    directory_address = f"{response.server_name}:{response.server_port}"
                    directory_channel = grpc.insecure_channel(directory_address)
                    directory_stub = directory_pb2_grpc.DirectoryStub(directory_channel)

                    query_response = directory_stub.Query(directory_pb2.QueryRequest(key=key))
                    formatted_number = "%7.4f" % query_response.item.value
                    print(str(query_response.item.desc)+","+ str(formatted_number))
                   

            elif command == "T":
                response = stub_i.Terminate(integration_pb2.TerminateRequest_())
                print(response.num_keys)
                break

    except KeyboardInterrupt:
        print("\nTerminating client")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python integration_client.py <server_address>")
        sys.exit(1)

    server_address = sys.argv[1]
    run_client(server_address)
