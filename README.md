[![Build Status](https://travis-ci.org/systelab/cpp-jwt-utils.svg?branch=master)](https://travis-ci.org/systelab/cpp-jwt-utils)
[![Build status](https://ci.appveyor.com/api/projects/status/jtbc93k8i6vtnx56?svg=true)](https://ci.appveyor.com/project/systelab/cpp-jwt-utils)
[![codecov](https://codecov.io/gh/systelab/cpp-jwt-utils/branch/master/graph/badge.svg)](https://codecov.io/gh/systelab/cpp-jwt-utils)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dd32a177d926495dab93be941a939881)](https://www.codacy.com/app/systelab/cpp-jwt-utils?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=systelab/cpp-jwt-utils&amp;utm_campaign=Badge_Grade)

# C++ JSON Web Token Utilities

This library provides utilities to generate, parse and validate JWTs (JSON Web Tokens) used to implement an authentication mechanism over a REST API. 

## Setup

### Build from sources

Prerequisites:
  - [Git](https://git-scm.com/)
  - [Conan](https://conan.io/)
  - [CMake](https://cmake.org/)
  - [Visual Studio](https://visualstudio.microsoft.com/) (only on Windows)
  - [GCC](https://gcc.gnu.org/) (only on Linux)

Build library with the following steps:
  1. Clone this repository in a local drive
  2. Make a build directory (i.e. `build/`)
  3. Install `conan` dependencies in the build directory
  4. Run `cmake` in the build directory to configure build targets
  5. Use `Visual Studio` (on Windows) or `make` (on Linux) to build the library

#### Windows
``` bash
> git clone https://github.com/systelab/cpp-jwt-utils
> md build && cd build
> conan install .. -s arch=x86
> cmake ..
> devenv.exe JWTUtils.sln
```

#### Linux
``` bash
> git clone https://github.com/systelab/cpp-jwt-utils
> mkdir build && cd build
> conan install ..
> cmake .. -DCMAKE_BUILD_TYPE=[Debug | Coverage | Release]
> make
```

### Download using Conan (not available yet)

  1. Create/update your `conanfile.txt` to add this library as follows:

```
[requires]
JWTUtils/1.0.0@systelab/stable

[generators]
cmake
```

  2. Integrate Conan into CMake by adding the following code into your `CMakeLists.txt`:

```cmake
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
```

  3. Link against `${CONAN_LIBS}` when configuring your executables in CMake:

```cmake
set(MY_PROJECT MyProject)
add_executable(${MY_PROJECT} main.cpp)
target_link_libraries(${MY_PROJECT} ${CONAN_LIBS})
```

## Usage

### Build a token

Use the `TokenBuilderService` class to generate a valid token containing a vector of claims:

```cpp
TBD: Code to call the service
```

### Parse a token

Use the `TokenParserService` class to parse a JWT token and retrieve the claims contained on it. It will return false when the provided JWT is not valid.

```cpp
TBD: Code to call the service
```

