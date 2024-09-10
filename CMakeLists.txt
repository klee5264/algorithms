cmake_minimum_required(VERSION 3.28)
project(algorithms)

set(CMAKE_CXX_STANDARD 17)

add_executable(algorithms main.cpp
        include/lengthOfLongestSubstring.h
        include/stringToInteger.h
        include/addTwoNumbers.h
        include/integerToRoman.h
        include/letterCombinations.h)
