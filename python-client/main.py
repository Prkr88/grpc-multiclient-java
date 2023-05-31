import grpc
import proto.bank.user_pb2_grpc as user_grpc
import proto.bank.user_pb2 as user_pb2
import proto.bank.account_pb2_grpc as account_grpc
import proto.bank.account_pb2 as account_pb2


if __name__ == "__main__":
    request = user_pb2.UserRequest()
    request.user.account.balance = 40
    request.user.account.transactions.insert(0, 10)
    request.user.account.transactions.insert(1, 20)
    request.user.account.transactions.insert(2, 30)
    request.user.account.transactions.insert(3, 40)
    request.user.id = 123456789
    request.user.first_name = "Matan"
    request.user.last_name = "Parker"

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_grpc.UserServiceStub(channel)
        # response = stub.User(user_pb2.UserRequest())
        response = stub.User(request)
        print("Greeter client received following from server: " + response.result)
    print()
