/*
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
*/

bool isIsomorphic(char * s, char * t){
    int slen = strlen(s);
    int sAscii[256];
    int tAscii[256];

    for(int i=0;i<256;i++){
        sAscii[i] = tAscii[i] = -1;
    }
    
    for(int i=0;i<slen;i++){

        if(sAscii[s[i]] != tAscii[t[i]]){
            return false;
        }
        sAscii[s[i]] = tAscii[t[i]] = i;
    }
    
    return true;
}
