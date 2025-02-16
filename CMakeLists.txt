cmake_minimum_required(VERSION 3.8)
project(NewType)


set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 14)

add_subdirectory(third_party)  # third party tools and libraries

add_library(dtype INTERFACE)
target_include_directories(dtype INTERFACE src/)

add_subdirectory(examples)

enable_testing()
add_subdirectory(tests)
