package org.example.bank.server;

import com.proto.bank.*;
import io.grpc.stub.StreamObserver;

import java.util.stream.Collectors;

public class BankServiceImpl extends UserServiceGrpc.UserServiceImplBase {
    @Override
    public void userDetails(UserRequest request, StreamObserver<UserResponse> responseObserver) {
        System.out.println("Got a User details Request!");
        // extract the User from the request
        User user = request.getUser();
        Account account = user.getAccount();

        // create the response
        String result = "Hello " + user.getFirstName()
                + "\nYour Balance is " + account.getBalance()
                + "\nRecent Transactions [" + account.getTransactionsList().stream().map(Object::toString).collect(Collectors.joining(", "))
                + "]";
        UserResponse response = UserResponse.newBuilder()
                .setResult(result)
                .build();

        // send the response
        responseObserver.onNext(response);

        // complete the RPC call
        responseObserver.onCompleted();
    }

    @Override
    public void withdrawal(WithdrawalRequest request, StreamObserver<WithdrawalResponse> responseObserver) {

        // extract the User from the request
        User user = request.getUser();
        Account account = user.getAccount();
        int withdrawalAmountRequest = request.getWithdrawal().getRequestAmount();

        System.out.println("Got a Withdrawal Request from: " + user.getFirstName());

        // create the response
        String result = "Hello " + user.getFirstName()
                + "\nYour Balance is " + account.getBalance()
                + "\nYou have requested " + withdrawalAmountRequest + " ... "
                + (withdrawalAmountRequest <= user.getAccount().getBalance() ? "Request approved" : "Request declined");
        WithdrawalResponse response = WithdrawalResponse.newBuilder()
                .setResult(result)
                .build();

        // send the response
        responseObserver.onNext(response);

        // complete the RPC call
        responseObserver.onCompleted();
    }
}
