/*
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

*/

int longestPalindrome(char * s){

    int slen = strlen(s);
    int cnt = 0;
    int odd = 0;

    int sAscii[256] = {0};
    
    for(int i=0;i<slen;i++){
        sAscii[s[i]] += 1; 
    }

    for(int i=0;i<256;i++){
        if(sAscii[i] % 2 == 0){
            cnt += sAscii[i];
        }
        else {
            odd = 1;
            cnt += sAscii[i] - 1;
        }
    }

    return (cnt + odd);
}
