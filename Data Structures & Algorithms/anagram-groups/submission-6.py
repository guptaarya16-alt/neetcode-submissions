class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #index through the list (input):
        #start by outting first index of the input into its own given list.
        #if the next index of the og list is an anagram of the first index thay has already been put im its own list
        #append that next index to that given list
        # how do u check for anagram? we want to traverse by the char and input each char of the given index into its own lsit. usign the sorted python function we can then check if the lists are equal of not
        #if not an annagram of first create another new list and then do the same until u reach the emd of the og array

        #im gonne create a dictionary and then i will append every item in the og string into that dictionary.
        #ill set the key to the sorted word and the value will be the actuall word. if there r the same keys within the dictionary 
        #the values will be appneded to mkae one big list. 
        master={}
        for word in strs:
            key= sorted(word)
            key="".join(key)
            if key not in master:
                master[key]=[]
            master[key].append(word)
        return list(master.values())
        
            
            
        