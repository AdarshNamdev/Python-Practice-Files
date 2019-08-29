s = 'azcbobobegghakl'
longest = ''
current = s[0]
for i in range(len(s)-1):
    if s[i]<= s[i+1]:
        current = current + s[i+1]
    elif (s[i] > s[i+1])and(len(current)>len(longest)) :
        longest = current
        current = s[i+1]
    else:
        current = s[i+1]
        
print(longest)
        
        
    