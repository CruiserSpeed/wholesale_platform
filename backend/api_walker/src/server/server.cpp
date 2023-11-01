#include <string>
#include "server.hpp"

Status TServer::GetReply(ServerContext* context, const RequestMessage* request, ReplyMessage* response) {
    const std::string str = request->message();
    response->set_message("Hello, " + str);
    return Status::OK;
}



