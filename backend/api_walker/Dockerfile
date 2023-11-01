FROM ubuntu:latest

WORKDIR /tmp

RUN apt-get update && \
    apt-get install -y cmake && \
    apt-get install -y git && \
    apt-get install -y protobuf-compiler && \
    apt-get install -y build-essential autoconf libtool pkg-config
RUN git clone --recurse-submodules -b v1.58.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
RUN cd grpc && \
    mkdir -p cmake/build && \
    cd cmake/build && \
    cmake -DgRPC_INSTALL=ON \
      -DgRPC_BUILD_TESTS=OFF \
      -DCMAKE_INSTALL_PREFIX=/usr \
      ../.. && \
    make -j 4 && \
    make install

WORKDIR /app

COPY ./api_walker/src/ ./src/
COPY ./protos/ ./protos/

RUN protoc -I ./protos --grpc_out=src/server/proto --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ./protos/api_walker.proto && \
    protoc -I ./protos --cpp_out=src/server/proto ./protos/api_walker.proto

COPY ./api_walker/CMakeLists.txt .

RUN mkdir build && \
    cd build && \
    cmake .. && \
    cmake --build .
