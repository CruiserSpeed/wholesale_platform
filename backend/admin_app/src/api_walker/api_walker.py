import grpc
import api_walker.api_walker_pb2
import api_walker.api_walker_pb2_grpc
from globals import (
    API_WALKER_HOST,
    API_WALKER_PORT
)


def send_request_to_api_walker():
    with grpc.insecure_channel(f"{API_WALKER_HOST}:{API_WALKER_PORT}") as channel:
        stub = api_walker.api_walker_pb2_grpc.ApiWalkerStub(channel)
        request_message = api_walker.api_walker_pb2.RequestMessage()
        request_message.message = "Anton"
        reply_message = stub.GetReply(request_message)
        return reply_message.message