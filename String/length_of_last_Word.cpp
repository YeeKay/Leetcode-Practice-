# include <string>

// Problem Description: Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.

// Well, the basic idea is very simple. 
// Start from the tail of s and move backwards to find the first non-space character. 
// Then from this character, move backwards and count the number of non-space characters until we pass over the head of s or meet a space character. 
// The count will then be the length of the last word.

class Solution 
{
public:
    int lengthOfLastWord(const std::string s) 
    {
        int len = 0, tail = s.length() - 1;

        while (tail >= 0 && s[tail] == ' ') tail --;

        while (tail >= 0 && s[tail] != ' ')
        {
            len++;
            tail --;
        }    

        return len;
    }
};

//  Input: s = "Hello World"
//  Output: 5

//  Input: s = "   fly me to the moon   "
//  Output: 4 

//  Input: s = "luffy is still joyboy"
//  Output: 6 