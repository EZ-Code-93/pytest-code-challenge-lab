import pytest

from lib.palindrome import longest_palindromic_substring

def test_longest_palindromic_substring():
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("hello") == "ll"
    assert longest_palindromic_substring("banana") == "anana"
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_longest_palindromic_substring_empty():
    assert longest_palindromic_substring("") == ""

def test_longest_palindromic_substring_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_longest_palindromic_substring_non_palindromic():
    assert longest_palindromic_substring("abcdef") in ["a", "b", "c", "d", "e", "f"]

def test_longest_palindromic_substring_multiple_palindromes():
    assert longest_palindromic_substring("abacdfgdcaba") in ["aba", "cdc"]

def test_longest_palindromic_substring_long_string():
    long_palindrome = "a" * 1000
    assert longest_palindromic_substring(long_palindrome) == long_palindrome
