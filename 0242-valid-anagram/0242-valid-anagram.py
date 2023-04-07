class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #if the strings have different lengths, we automatically know they are not anagrams of each other
        # as one of the strings will extra letter(s)
        if len(s) != len(t):
            return False
        
        #create a hashMap/ddictionary that maps each letter in the string to how many counts of that letter is
        # present in the string
        countS, countT = {}, {}
        
        #iterate through the length of string S for both string S and string T (since we know both string S and T are same length now)
        for i in range(len(s)):
            #reason why we use countS.get(s[i], 0): if the key we want to get doesn't exist in the hashmap, then it will return 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT