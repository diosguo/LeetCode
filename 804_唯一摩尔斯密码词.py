from typing import List 


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_char_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_words = set()

        for word in words:
            word_morse = []
            for char in word:
                morse_code = morse_char_map[ord(char) - ord('a')]
                word_morse.append(morse_code)
            word_morse = ''.join(word_morse)

            morse_words.add(word_morse)
        return len(morse_words)


if __name__ == '__main__':
    s = Solution() 

    r= s.uniqueMorseRepresentations(['gin','zen','gig','msg'])
    print(r)