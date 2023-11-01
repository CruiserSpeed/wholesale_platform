cmake_minimum_required(VERSION 3.15)
set(PROJECT_NAME api_walker)
project(${PROJECT_NAME})

set(CMAKE_CXX_STANDARD 20)

file(GLOB SRC_FILES
    src/main.cpp
    src/server/server.cpp
    src/server/proto/api_walker.pb.cc
    src/server/proto/api_walker.grpc.pb.cc
)

find_package(Protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)
add_executable(${PROJECT_NAME} ${SRC_FILES})
target_link_libraries(${PROJECT_NAME} gRPC::grpc++)