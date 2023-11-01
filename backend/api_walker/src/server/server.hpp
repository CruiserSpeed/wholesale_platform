#ifndef SERVER_HPP_
#define SERVER_HPP_

#include <grpc/grpc.h>
#include <grpcpp/security/server_credentials.h>
#include <grpcpp/server.h>
#include <grpcpp/server_builder.h>
#include <grpcpp/server_context.h>

#include "proto/api_walker.grpc.pb.h"
#include "proto/api_walker.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::ServerReader;
using grpc::ServerReaderWriter;
using grpc::ServerWriter;
using grpc::Status;
using apiwalker::RequestMessage;
using apiwalker::ReplyMessage;
using apiwalker::ApiWalker;
using std::chrono::system_clock;


class TServer final : public ApiWalker::Service {
public:
    Status GetReply(ServerContext* context, const RequestMessage* request, ReplyMessage* response) override;
}; // class TServer
 

#endif // SERVER_HPP_