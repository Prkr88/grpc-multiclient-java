package org.example.bank.client;

import com.proto.bank.*;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import javax.net.ssl.SSLException;
import java.util.ArrayList;
import java.util.stream.IntStream;

public class BankClient {

    public static void main(String[] args) throws SSLException {
        System.out.println("Hello I'm a gRPC client");

        BankClient main = new BankClient();
        main.run();
    }

    private void run() {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()
                .build();


        doUnaryCall(channel);
    }

    private void doUnaryCall(ManagedChannel channel) {
        // Blocking Client
        UserServiceGrpc.UserServiceBlockingStub userClient = UserServiceGrpc.newBlockingStub(channel);

        ArrayList<Integer> randomTransactionList = getSampleTransactionList();

        // Account message
        Account account = Account.newBuilder()
                .setBalance(sumTransactions(randomTransactionList))
                .addAllTransactions(randomTransactionList)
                .build();

        // User message
        User user = User.newBuilder()
                .setFirstName("Matan")
                .setLastName("Parker")
                .setId(123456789)
                .setAccount(account)
                .build();

        Withdrawal withdrawal = Withdrawal.newBuilder()
                .setRequestAmount(100)
                .build();

        // Build user request
        UserRequest userRequest = UserRequest.newBuilder()
                .setUser(user)
                .build();

        WithdrawalRequest withdrawalRequest = WithdrawalRequest.newBuilder()
                .setUser(user)
                .setWithdrawal(withdrawal)
                .build();

        // Send the request and save the response
        UserResponse userResponse = userClient.userDetails(userRequest);

        WithdrawalResponse withdrawalResponse = userClient.withdrawal(withdrawalRequest);

        System.out.println(userResponse.getResult());
        System.out.println(withdrawalResponse.getResult());

    }

    public ArrayList<Integer> getSampleTransactionList() {
        ArrayList<Integer> transactionList = new ArrayList<>();
        IntStream.range(1, 10).forEach(
                i -> transactionList.add((getRandomTransactionAmount()))
        );
        return transactionList;
    }

    public int getRandomTransactionAmount() {
        int min = -1000; // Minimum value of range
        int max = 1000; // Maximum value of range

        return (int) Math.floor(Math.random() * (max - min + 1) + min);
    }

    public int sumTransactions(ArrayList<Integer> transactionList) {
        return transactionList.stream().mapToInt(Integer::intValue).sum();
    }
}
