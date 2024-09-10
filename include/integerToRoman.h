#ifndef INTEGERTOROMAN_H
#define INTEGERTOROMAN_H

#include <string>

class IntToRoman {
public:
    string solution(int num) {
        string ones[] = {"","I","II","III","IV","V","VI","VII","VIII","IX"};
        string tens[] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        string hrns[] = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        string ths[]={"","M","MM","MMM"};

        return ths[num/1000] + hrns[(num%1000)/100] + tens[(num%100)/10] + ones[num%10];
    }
};

#endif //INTEGERTOROMAN_H

/*

class IntToRoman {
public:
    string solution(int num) {
        int[] n = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string[] s = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int i =0;
        string str = new string();
        while (num>0){
            if (num>=n[i]){
                str=str+s[i];
                num-=n[i];
            } else{
                i++;
            }
        }
        return str;
    }
}


Thank you for the great solution.

I think It can be a little bit more optimized memory wise if you use StringBuilder to not alocate new string for every iteration.

`class Solution {
public String intToRoman(int num) {
StringBuilder s = new StringBuilder("");
int[] numbers = {1000, 900, 500, 400, 100, 90, 50, 40, 10 ,9, 5, 4, 1};
String[] romanNumbers = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    int index = 0;
    while (num > 0) {
        if (num >= numbers[index]) {
            s.append(romanNumbers[index]);
            num -= numbers[index];
        } else {
            index++;
        }
    }

    return s.toString();
}
}`
 */