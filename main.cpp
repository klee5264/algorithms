#include <iostream>
#include <string>

// #include "C:\Workspace\algorithms\include\test.h"
#include "include/lengthOfLongestSubstring.h"
#include "include/stringToInteger.h"
#include "include/addTwoNumbers.h"
#include "include/integerToRoman.h"
#include "include/letterCombinations.h"


using namespace std;


int main() {
    cout << "Hello, C++ World!" << endl;

    string digit = "124";
    LetterCombinations algorithmClass;
    cout << algorithmClass.solution(digit) << endl;

    return 0;
}
