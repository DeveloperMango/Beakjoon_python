#1181번: 단어정렬
#https://www.acmicpc.net/problem/1181

import sys

cnt = int(sys.stdin.readline())
words_list = []

for _ in range(cnt):
    word = str(sys.stdin.readline())
    word_count = len(word)
    words_list.append((word, word_count))

#중복 삭제
words_list = list(set(words_list))

#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0],end="")
