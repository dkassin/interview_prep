from collections import Counter
def find_substring(s,words):
    tracker = Counter(words)
    word_length = len(words[0])
    window_size = word_length * len(words)
    start = 0
    result = []

    for end in range(len(s)):
        if end - start == window_size:
            test_counter = Counter()
            for i in range(start, start+window_size, word_length):
                word = s[i:i+word_length]
                test_counter[word] += 1
            if test_counter == tracker:
                result.append(start)
            start += 1

    return result
