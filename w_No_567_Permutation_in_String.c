/*
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
*/

//Worong Answer
//s1 = "abc", s2 = "ccccbbbbaaaa" --> sum_s1 = 294(a+b+c), sum_s2 = 294(b+b+b)

bool checkInclusion(char * s1, char * s2){

    int lens1 = strlen(s1);
    int lens2 = strlen(s2);
    int sum_s1 = 0;
    int sum_s2 = 0;

    for(int i=0;i<lens1;i++){
        sum_s1 += s1[i];
    }

    for(int i=0;i<lens2-lens1+1;i++){
        for(int j=i;j<i+lens1;j++){
            sum_s2 += s2[j];
        }
        if(sum_s1 == sum_s2) return true;
        sum_s2 = 0;
    }

    return false;
}
