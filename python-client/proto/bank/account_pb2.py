# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/bank/account.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/bank/account.proto\x12\x04\x62\x61nk\"4\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x05\x12\x18\n\x0ctransactions\x18\x02 \x03(\x05\x42\x02\x10\x01\"0\n\x0e\x41\x63\x63ountRequest\x12\x1e\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\r.bank.Account\"!\n\x0f\x41\x63\x63ountResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2J\n\x0e\x41\x63\x63ountService\x12\x38\n\x07\x41\x63\x63ount\x12\x14.bank.AccountRequest\x1a\x15.bank.AccountResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.bank.account_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACCOUNT.fields_by_name['transactions']._options = None
  _ACCOUNT.fields_by_name['transactions']._serialized_options = b'\020\001'
  _ACCOUNT._serialized_start=34
  _ACCOUNT._serialized_end=86
  _ACCOUNTREQUEST._serialized_start=88
  _ACCOUNTREQUEST._serialized_end=136
  _ACCOUNTRESPONSE._serialized_start=138
  _ACCOUNTRESPONSE._serialized_end=171
  _ACCOUNTSERVICE._serialized_start=173
  _ACCOUNTSERVICE._serialized_end=247
# @@protoc_insertion_point(module_scope)
