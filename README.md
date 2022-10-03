# Rabin-Karp-Algorith
Robin Karp Algorithm using python (language)
# OVER VIEW
1)  Richard M. Karp and Michael O. Rabin created the Robin Karp algorithm in 1987.
2)	Robin Karp algorithm is a string searching or pattern finding algorithm.
3)  Robin Karp Algorithm is used to reduce the time complexity of matching strings.
4)	It uses the concept of Hashing.
5)	The important function in the algorithm is the hash function

# 	ADVANTAGES:

1) Complexity of Rabin Karp O(mn) where m=string/sentence length and n=pattern length
2) Rabin Karp is better for large text matching  



# USES
1) Plagiarism detection
2) Email detection
3) Pattern matching

# 	HASH FUNCTION:
1)	The complexity of comparing 2 string is O(min(n1,n2)) .
2)	Complexity of comparing 2 integer is O(1) .
3)	Basic idea of hashing is to convert a sting into integer using some formulas

# 	CONDITIONS FOR HASH FUNCTIONS:

1)	If two string s and t are equal, then their hash are also equal.
2)  s=t so hash(s)=hash(t) 

# 	IMPORTANT FORMULA (HASH FORMULA):

1	Hash value =Σ(v * dm-1) mod q
2	Where:
3	v= numerical weight
4	dm= 10^-1 (each turn
5	q= prime number 


# 	ALGORITHM:

1)	Start
2)	Assign a numerical value(v)/weight for the characters we will be using in the problem.
3)	let n be the length of the pattern and m be the length of the text.
4)	Calculate the hash value of the pattern.
5)	Calculate the hash value for the text-window of size m.
6)	We calculate the hash value of the next window by subtracting the first term and adding the next term 
7)	Compare the hash value of the pattern with the hash value of the text. If they match then, character-matching is performed.
8)	Repeat step 4,5,6,7 until all strings are not matched with pattern.

# 	PYTHON IMPLEMENTATION:
![image](https://user-images.githubusercontent.com/92653096/193650020-01702225-b175-461c-b2a8-53c9df946185.png)
![image](https://user-images.githubusercontent.com/92653096/193650047-21c3cd3b-e58b-4d39-add0-87dfe4e8c2ac.png)

# Testing
![image](https://user-images.githubusercontent.com/92653096/193650082-8098663b-5f5d-45b3-9b33-c4ee0007bc5d.png)
![image](https://user-images.githubusercontent.com/92653096/193650118-898ba86d-2986-4834-858e-8d4a51bcb946.png)









# CONCLUSION
In conclusion Rabin karp algorithm is used to find any pattern in the given sentence. 
This is done by using the hash value which is the efficient way of finding any pattern in the given string.
