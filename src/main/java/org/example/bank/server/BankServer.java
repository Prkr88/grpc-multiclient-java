package org.example.bank.server;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class BankServer {
    public static void main(String[] args) throws IOException, InterruptedException {
        System.out.println("Hello, im a gRPC server");

        // simple server at 50051
        Server server = ServerBuilder.forPort(50051)
                .addService(new BankServiceImpl())
                .build();

        server.start();

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("Received Shutdown Request");
            server.shutdown();
            System.out.println("Successfully stopped the server");
        }));

        server.awaitTermination();
    }
}
