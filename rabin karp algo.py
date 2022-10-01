# Rabin-Karp algorithm in python
deci = 10
def search(pattern, text, prime):
    m = len(pattern)
    n = len(text)
    hash_p = 0
    hash_t = 0
    h = 1
    i = 0
    j = 0
    check=False
    for i in range(m-1):
        h = (h * deci) % prime

    # Calculate hash value for pattern and text
    for i in range(m):
        hash_p = (deci * hash_p + ord(pattern[i])) % prime
        hash_t = (deci * hash_t + ord(text[i])) % prime

    # Find the match
    for i in range(n-m+1):
        if hash_p == hash_t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                check=True
                print("Pattern is found at position: "
                      + str(i+1))

        if i < n-m:
            hash_t = (deci * (hash_t - ord(text[i]) * h)
                      + ord(text[i + m])) % prime

            if hash_t < 0:
                hash_t = hash_t + prime
    if check:
        print()
    else:
        print("Pattern is not in the String")

text = "Furqanali@gmail.com and Jameelkhalid@gmail.com"
pattern = input("Please Enter the pattern you want to find:")
print("Text= ",text)
print("Pattern= ",pattern)
q =97
search(pattern, text, q)
