import time
start_time = time.clock()
text= "ababaaaa"
pattern = "aaa"
found=False
for s in range ((len(text)-len(pattern))+1):
    for j in range(len(pattern)):
            if text[s+j] != pattern[j]:
                break
            elif j == len(pattern) - 1:
                print ('Pattern occurs with shift' )
                print (s)
                found=True
    
if not found:
    print ('No match found'  )  
print("--- %s seconds ---" % (time.clock() - start_time))        