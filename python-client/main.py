import grpc

import proto.bank.user_pb2 as user_pb2
import proto.bank.user_pb2_grpc as user_grpc

if __name__ == "__main__":
    details_request = user_pb2.UserRequest()
    details_request.user.account.balance = 200
    details_request.user.account.transactions.insert(0, 10)
    details_request.user.account.transactions.insert(1, 20)
    details_request.user.account.transactions.insert(2, 30)
    details_request.user.account.transactions.insert(3, 40)
    details_request.user.id = 123456789
    details_request.user.first_name = "Matan"
    details_request.user.last_name = "Parker"

    withdrawal_request = user_pb2.WithdrawalRequest()
    withdrawal_request.withdrawal.request_amount = 100
    withdrawal_request.user.account.balance = details_request.user.account.balance
    withdrawal_request.user.first_name = details_request.user.first_name

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_grpc.UserServiceStub(channel)
        # response = stub.User(user_pb2.UserRequest())
        details_response = stub.UserDetails(details_request)
        withdrawal_response = stub.Withdrawal(withdrawal_request)
        print(details_response.result)
        print(withdrawal_response.result)
