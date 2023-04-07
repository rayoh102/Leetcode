class Codec:

    def encode(self, strs):
			res = ""
			# iterate through each word in the strs array
			for s in strs:
				# for each word, add the word length, delimiter "#", then the word itself to our res string  
				res += str(len(s)) + "#" + s
			return res
        

    def decode(self, s):
			res, i = [], 0
			# for each index in our encoded string
			while i < len(s):
				# i = the beginning index of our "word length" number
				j = i
				# Iterate through the indices until you reach the delimiter
				while s[j] != "#":
					# j = the end index of our "word length" number 
					j += 1

				# the number that represents our word length starts at index i, ends at index j
				length = int(s[i:j])

				# append the word to the result array 
				res.append(s[j + 1 : j + 1 + length])

				# update the index i to point at the next word 
				i = j + 1 + length
			return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))