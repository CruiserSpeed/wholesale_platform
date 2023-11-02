FROM ubuntu:latest

COPY ./admin_app/requirements.txt .

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install -r requirements.txt && \
    python3 -m pip install grpcio-tools


WORKDIR /app
COPY ./admin_app/src/ ./src/
COPY ./admin_app/tests/ ./tests/
COPY ./admin_app/pytest.ini .
COPY ./admin_app/run_tests.sh .
COPY ./protos/ ./protos/

RUN python3 -m grpc_tools.protoc -I ./protos --python_out=src/api_walker --pyi_out=src/api_walker --grpc_python_out=src/api_walker ./protos/api_walker.proto
RUN ls src/api_walker
