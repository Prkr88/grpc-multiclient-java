# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/bank/user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.bank import account_pb2 as proto_dot_bank_dot_account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/bank/user.proto\x12\x04\x62\x61nk\x1a\x18proto/bank/account.proto\"Y\n\x04User\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\x12\x1e\n\x07\x61\x63\x63ount\x18\x04 \x01(\x0b\x32\r.bank.Account\"$\n\nWithdrawal\x12\x16\n\x0erequest_amount\x18\x01 \x01(\x05\"\'\n\x0bUserRequest\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.bank.User\"\x1e\n\x0cUserResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"S\n\x11WithdrawalRequest\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.bank.User\x12$\n\nwithdrawal\x18\x02 \x01(\x0b\x32\x10.bank.Withdrawal\"$\n\x12WithdrawalResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\x88\x01\n\x0bUserService\x12\x36\n\x0bUserDetails\x12\x11.bank.UserRequest\x1a\x12.bank.UserResponse\"\x00\x12\x41\n\nWithdrawal\x12\x17.bank.WithdrawalRequest\x1a\x18.bank.WithdrawalResponse\"\x00\x42\x12\n\x0e\x63om.proto.bankP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.bank.user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.proto.bankP\001'
  _USER._serialized_start=57
  _USER._serialized_end=146
  _WITHDRAWAL._serialized_start=148
  _WITHDRAWAL._serialized_end=184
  _USERREQUEST._serialized_start=186
  _USERREQUEST._serialized_end=225
  _USERRESPONSE._serialized_start=227
  _USERRESPONSE._serialized_end=257
  _WITHDRAWALREQUEST._serialized_start=259
  _WITHDRAWALREQUEST._serialized_end=342
  _WITHDRAWALRESPONSE._serialized_start=344
  _WITHDRAWALRESPONSE._serialized_end=380
  _USERSERVICE._serialized_start=383
  _USERSERVICE._serialized_end=519
# @@protoc_insertion_point(module_scope)
