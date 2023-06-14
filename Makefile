# Variable definitions
PROTO_GEN_DIR = path/to/generated/stubs
PROTO_FILE = example.proto
STUB_FILE = example_pb2.py
PYTHON_FILES = my_script.py

# Default target
all: build

# Generate gRPC stubs
$(PROTO_GEN_DIR)/$(STUB_FILE): $(PROTO_FILE)
	python -m grpc_tools.protoc \
		--proto_path=. \
		--python_out=$(PROTO_GEN_DIR) \
		--grpc_python_out=$(PROTO_GEN_DIR) \
		$(PROTO_FILE)

# Build the project
build: $(PROTO_GEN_DIR)/$(STUB_FILE)

# Run the Python script
run: $(PROTO_GEN_DIR)/$(STUB_FILE)
	python $(PYTHON_FILES)

# Clean generated files
clean:
	rm -rf $(PROTO_GEN_DIR)/*.py


