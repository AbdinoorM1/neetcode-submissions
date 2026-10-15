class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t): #early flag, if len !=, then cant be an anagram
            s_dict = {}
            t_dict = {}
            frequency = 0

            for i in range(len(s)):
                if s[i] in s_dict:
                    s_dict[s[i]] += 1 #add one to the current value
                else:
                    s_dict[s[i]] = 1 #this case occurs if the key is new, so its value (frequency) is now 1

                if t[i] in t_dict:
                    t_dict[t[i]] += 1 #add one to the current value
                else:
                    t_dict[t[i]] = 1 #this case occurs if the key is new, so its value (frequency) is now 1


            if s_dict == t_dict: #if the dictionaries contain the same frequencies for the values in them (the string for a and b), then true


                return True



        return False