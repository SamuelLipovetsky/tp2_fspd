# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: directory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64irectory.proto\"#\n\x04Item\x12\x0c\n\x04\x64\x65sc\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"9\n\rInsertRequest\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\" \n\x0eInsertResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x1b\n\x0cQueryRequest\x12\x0b\n\x03key\x18\x01 \x01(\x05\"$\n\rQueryResponse\x12\x13\n\x04item\x18\x01 \x01(\x0b\x32\x05.Item\";\n\x0fRegisterRequest\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12\x13\n\x0bserver_port\x18\x02 \x01(\x05\"\"\n\x10RegisterResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"\x12\n\x10TerminateRequest\"%\n\x11TerminateResponse\x12\x10\n\x08num_keys\x18\x01 \x01(\x05\x32\xcb\x01\n\tDirectory\x12+\n\x06Insert\x12\x0e.InsertRequest\x1a\x0f.InsertResponse\"\x00\x12(\n\x05Query\x12\r.QueryRequest\x1a\x0e.QueryResponse\"\x00\x12\x31\n\x08Register\x12\x10.RegisterRequest\x1a\x11.RegisterResponse\"\x00\x12\x34\n\tTerminate\x12\x11.TerminateRequest\x1a\x12.TerminateResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'directory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ITEM._serialized_start=19
  _ITEM._serialized_end=54
  _INSERTREQUEST._serialized_start=56
  _INSERTREQUEST._serialized_end=113
  _INSERTRESPONSE._serialized_start=115
  _INSERTRESPONSE._serialized_end=147
  _QUERYREQUEST._serialized_start=149
  _QUERYREQUEST._serialized_end=176
  _QUERYRESPONSE._serialized_start=178
  _QUERYRESPONSE._serialized_end=214
  _REGISTERREQUEST._serialized_start=216
  _REGISTERREQUEST._serialized_end=275
  _REGISTERRESPONSE._serialized_start=277
  _REGISTERRESPONSE._serialized_end=311
  _TERMINATEREQUEST._serialized_start=313
  _TERMINATEREQUEST._serialized_end=331
  _TERMINATERESPONSE._serialized_start=333
  _TERMINATERESPONSE._serialized_end=370
  _DIRECTORY._serialized_start=373
  _DIRECTORY._serialized_end=576
# @@protoc_insertion_point(module_scope)