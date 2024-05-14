cmake_minimum_required(VERSION 3.13.0)

set(CMAKE_CXX_STANDARD 17)

project(
  pygko
  LANGUAGES CXX
  DESCRIPTION
    "A wrapper for Ginkgo solver to provide GPGPU capabilities to OpenFOAM")

find_package(
    Ginkgo
    CONFIG
    1.7.0
    REQUIRED
)


find_package(Python REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED CONFIG)

pybind11_add_module(pygko
  ${PROJECT_SOURCE_DIR}/bindings/python.cpp
  ${PROJECT_SOURCE_DIR}/bindings/dense.cpp
  # ${PROJECT_SOURCE_DIR}/bindings/matrix.cpp
  # ${PROJECT_SOURCE_DIR}/bindings/cg.cpp
  # ${PROJECT_SOURCE_DIR}/bindings/preconditioner.cpp
  # ${PROJECT_SOURCE_DIR}/bindings/criteria.cpp
)

target_include_directories(pygko PRIVATE ${Ginkgo_BINARY_DIR}/include)
target_link_libraries(pygko PRIVATE Ginkgo::ginkgo)
