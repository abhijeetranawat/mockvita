for j in range(int(input())):
    lst=sorted(list(input()))
    all_freq = {}
    for i in lst:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print( max(all_freq, key=all_freq.get))