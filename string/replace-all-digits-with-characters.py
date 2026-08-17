class Solution:
    def replaceDigits(self, s: str) -> str:
        """
        What I learned:

        range in a for loop is (<num_to_start>, <end_num>, <inc_num>)
        chr in Python is turns an ASCII number representation into its char
        ord in Python is turns a char into its ASCII number representation
        """
        
        # Go through the list and get the index of the current letter
        # Then get the number and continue through the list from there
        # going forward until you find the resulting letter
        # Roll over if over 26

        # Get the alphabet in a list
        alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
        
        # Setup a string and turn s into a list so we can get the next element
        output_str = ""
        s = list(s)

        # Iterate through the list of chars getting the index
        for i in range(len(s)):
            # If it is not every other element then skip it
            if (i % 2) != 0:
                continue
            # Iterate through the list of letters and check if it matches the
            # letter in the string
            for j in range(len(alph)):
                # If it does match we will add it to the output string and if 
                # there is an index after that value get that and add it to 
                # the existing index to get the letter that should go there
                if s[i] == alph[j]:
                    output_str += alph[j]
                    if (i + 1) < len(s):
                        output_str += alph[j+int(s[i+1])]

        return output_str
