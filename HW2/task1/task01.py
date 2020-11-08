"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
# import re
import itertools
import string
from collections import defaultdict
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape") as f:
        d_words = defaultdict(int)
        for line in f.readlines():
            # line = re.sub(r'[^\w\s]', '', line).split()
            line = line.translate(str.maketrans("", "", string.punctuation)).split()
            for word in line:
                d_words[word] = len(set(word))
        l_words = sorted(d_words.items(), key=lambda l: l[1], reverse=True)[:10]
        l_words = [i[0] for i in l_words]
        return l_words


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape") as f:
        dic_chars = defaultdict(int)
        for line in f.readlines():
            line = line.strip().split()
            for symbol in itertools.chain.from_iterable(line):
                dic_chars[symbol] += 1
        rar_char = sorted(dic_chars.items(), key=lambda k: k[1])[0][0]
        return rar_char


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as f:
        amount = 0
        for line in f.readlines():
            line = line.strip().split()
            for i in itertools.chain.from_iterable(line):
                if i in string.punctuation:
                    amount += 1
        return amount


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as f:
        amount = 0
        for line in f.readlines():
            line = line.strip().split()
            for i in itertools.chain.from_iterable(line):
                if not i.isascii():
                    amount += 1
        return amount


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape") as f:
        m_com = defaultdict(int)
        for line in f.readlines():
            line = line.strip().split()
            for i in itertools.chain.from_iterable(line):
                if not i.isascii():
                    m_com[i] += 1
        return sorted(m_com.items(), key=lambda v: v[1])[-1][0]
