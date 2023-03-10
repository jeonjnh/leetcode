/*
12. Integer to Roman

https://leetcode.com/problems/integer-to-roman/description/
*/

#define num_roman 13

struct Roman{
    int value;
    int *symbol;
};

char * intToRoman(int num){

    char *result = (char *)malloc(50*sizeof(char));
    result[0] = '\0';
    struct Roman romanSymbol[num_roman] = {
        {1,"I"},{4,"IV"},{5,"V"},
        {9,"IX"},{10,"X"},
        {40,"XL"},{50,"L"},
        {90,"XC"},{100,"C"},
        {400,"CD"},{500,"D"},
        {900,"CM"},{1000,"M"}
    };

    for(int i=num_roman-1;i>=0;i--)
    {
        while(num - romanSymbol[i].value >= 0)
        {
            strcat(result, romanSymbol[i].symbol);
            num = num - romanSymbol[i].value;
        }
    }

    return result;

}
