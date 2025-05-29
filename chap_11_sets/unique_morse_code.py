def unique_morse_representations(words) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    return_set = set()
    for word in words:
        morse_word = []
        for char in word:
            morse_index = ord(char) - ord('a')
            morse_word.append(morse[morse_index])
        return_set.add("".join(morse_word))
    return len(return_set)