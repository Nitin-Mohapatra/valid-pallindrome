# 🔁 Palindrome String Checker

This Python script checks whether a given string is a **valid palindrome**, considering only alphanumeric characters and ignoring cases.

---

## 📘 Problem Statement

Given a string `s`, determine if it is a **palindrome**, considering only **alphanumeric characters** and **ignoring cases**.

### A palindrome:
A word, phrase, or sequence that reads the same backward as forward after filtering out non-alphanumeric characters.

---

## 🧠 Approach

1. Initialize an empty string `pl` to store processed characters.
2. Traverse the input string `s`.
3. For each character:
   - If it's alphanumeric, convert it to lowercase and append
  
## ⏱ Time and Space Complexity
Time Complexity: O(n)
  - The input string is traversed once and reversed once.

Space Complexity: O(n)
  - For storing the filtered characters in pl.
