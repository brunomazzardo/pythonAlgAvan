prime = 101
def pattern_matching(text, pattern):
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(pattern, m - 1)
    text_hash = create_hash(text, m - 1)
    generate_hash = recalculate_hashNew(text_hash,m)
    for i in range(1, n - m + 2):
        if pattern_hash == text_hash:
            if check_equal(text[i-1:i+m-1], pattern[0:]) is True:
                return i - 1;
        if i < n - m + 1:
            text_hash = generate_hash.__next__()
    return -1;
    
def check_equal(str1, str2):
    if len(str1) != len(str2):
        return False;
    i = 0
    j = 0
    for i, j in zip(str1, str2):
        if i != j:
            return False;
    return True
    
def create_hash(input, end):
    hash = 0
    for i in range(end + 1):
        hash = hash + ord(input[i])*pow(prime, i)
    return hash

def recalculate_hashNew( oldHash,pattern_len):
    for char in  range(1,len(text)):
        oldHash = (oldHash - ord(text[char-1]))/3 +ord(text[char+pattern_len-1])*pow(prime, pattern_len - 1)
        yield  oldHash





import time
start_time = time.clock()
text='fghjk'
pattern = 'hj'
index = pattern_matching(text, pattern)
if index > 0:
    print ('Pattern occurs with shift' )
    print (index)
else:
         print ('No match found')    

print("--- %s seconds ---" % (time.clock() - start_time)) 