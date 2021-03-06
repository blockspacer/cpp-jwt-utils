import os
from conans import ConanFile, tools

class JWTUtilsTestUtilitiesConan(ConanFile):
    name = "JWTUtilsTestUtilities"
    description = "Test utilities for C++ JSON Web Token Utilities"
    url = "https://github.com/systelab/cpp-jwt-utils"
    homepage = "https://github.com/systelab/cpp-jwt-utils"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "jwt", "utils", "security")
    license = "MIT"
    generators = "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"
    options = {"gtest": ["1.7.0", "1.8.1", "1.10.0"], "OpenSSL": ["1.0.2n", "1.0.2s"]}
    default_options = {"gtest":"1.10.0", "OpenSSL":"1.0.2s"}
    exports_sources = "*"

    def configure(self):
        self.options["JWTUtils"].gtest = self.options.gtest
        self.options["JWTUtils"].OpenSSL = self.options.OpenSSL

    def requirements(self):
        if self.options.gtest == "1.7.0":
            self.requires("gtest/1.7.0@systelab/stable")
        elif self.options.gtest == "1.8.1":
            self.requires("gtest/1.8.1@bincrafters/stable")
        else:
            self.requires("gtest/1.10.0@systelab/stable")

        if ("%s" % self.version) == "None":
            self.requires("JWTUtils/%s@systelab/stable" % os.environ['VERSION'])
        else:
            self.requires("JWTUtils/%s@systelab/stable" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy("*.so*", dst="bin", src="lib")

    def package(self):
        self.copy("*.h", dst="include/JWTUtilsTestUtilities", keep_path=True)
        self.copy("*JWTUtilsTestUtilities.lib", dst="lib", keep_path=False)
        self.copy("*JWTUtilsTestUtilities.pdb", dst="lib", keep_path=False)
        self.copy("*JWTUtilsTestUtilities.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
