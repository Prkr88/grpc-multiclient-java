# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto.bank import account_pb2 as proto_dot_bank_dot_account__pb2


class AccountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Account = channel.unary_unary(
                '/bank.AccountService/Account',
                request_serializer=proto_dot_bank_dot_account__pb2.AccountRequest.SerializeToString,
                response_deserializer=proto_dot_bank_dot_account__pb2.AccountResponse.FromString,
                )


class AccountServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Account(self, request, context):
        """Unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Account': grpc.unary_unary_rpc_method_handler(
                    servicer.Account,
                    request_deserializer=proto_dot_bank_dot_account__pb2.AccountRequest.FromString,
                    response_serializer=proto_dot_bank_dot_account__pb2.AccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bank.AccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccountService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Account(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bank.AccountService/Account',
            proto_dot_bank_dot_account__pb2.AccountRequest.SerializeToString,
            proto_dot_bank_dot_account__pb2.AccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)