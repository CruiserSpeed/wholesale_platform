#include <iostream>
#include "server/server.hpp"

void RunServer() {
  std::string server_address("0.0.0.0:50051");
  TServer service;

  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;
  server->Wait();
}

int main() {
    std::cout << "main" << std::endl;
    RunServer();
    return 0;
}