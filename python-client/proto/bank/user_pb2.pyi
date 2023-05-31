from google.protobuf import any_pb2 as _any_pb2
from proto.bank import account_pb2 as _account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["account", "first_name", "id", "last_name"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    first_name: str
    id: int
    last_name: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., id: _Optional[int] = ..., account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ...) -> None: ...

class UserRequest(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...
