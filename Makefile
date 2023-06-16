
stubs:
    protoc -I=<path_to_integration_proto> --python_out=. /integration.proto
    protoc -I=<path_to_directory_proto> --python_out=. /directory.proto

run_cli_dir: stubs
    python3 client.py $(arg)

run_serv_dir: stubs
    python3 server.py $(arg)

run_cli_int: stubs
    python3 client2.py $(arg)

run_serv_int: stubs
    python3 server2.py $(arg)

clean:
    # Remove intermediate files
    rm -f *.pyc
    rm -f *_pb2.py