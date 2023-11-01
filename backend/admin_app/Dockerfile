FROM ubuntu:latest

COPY ./admin_app/requirements.txt .

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install -r requirements.txt
    # python3 -m pip install grpcio && \
    # python3 -m pip install grpcio-tools


WORKDIR /app
COPY ./admin_app/src/ ./src/
COPY ./admin_app/tests/ ./tests/
COPY ./admin_app/pytest.ini .

# RUN python -m grpc_tools.protoc -I ../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/helloworld.proto
