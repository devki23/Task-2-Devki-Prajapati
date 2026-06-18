# Project 2: Basic Encryption & Decryption — Caesar Cipher Implementation

**DecodeLabs Cybersecurity Internship — Batch 2026**  
**Author:** Devki Prajapati

---

## Overview

A Python program that implements the **Caesar Cipher** — one of the oldest encryption techniques — to encrypt and decrypt user-provided text using a shift-based substitution algorithm. The project demonstrates core cryptography concepts including symmetric encryption, ASCII encoding, and modular arithmetic.

---

## Project Goal

Encrypt and decrypt user text using Caesar Cipher:

1. Apply shift-based logic to transform plaintext into ciphertext
2. Decrypt back by reversing the shift to recover the original message
3. Spaces, numbers, and punctuation are preserved as-is
4. Display Original, Encrypted, and Decrypted results

**Tools Used:** Python 3, VS Code

---

## What is Caesar Cipher?

The Caesar Cipher is the oldest encryption technique — famously used by Julius Caesar to protect military communications.

- Each letter is shifted by a fixed number of positions in the alphabet
- **Example with Shift = 3:** `A → D`, `B → E`, `K → N`, `Z → C` (wraps around)
- It is a form of **Symmetric Encryption** — the same key is used to both encrypt and decrypt

---

## The Math Behind the Cipher

### Encryption Formula:
```
E(x) = (x + n) mod 26
```

### Decryption Formula:
```
D(x) = (x - n) mod 26
```

Where `x` = character position (0–25) and `n` = shift key.

### Python Conversion Functions:
| Function | Purpose |
|---|---|
| `ord()` | Converts a letter to its ASCII numeric value |
| `chr()` | Converts a number back to its character representation |

---

## Algorithm — Step by Step

**Encrypting the letter "A" with a shift of 3:**
1. Convert `A` to number → position 0
2. Add shift: `0 + 3 = 3`
3. Apply modulo: `3 % 26 = 3`
4. Convert back: position 3 → `D`

**Wrap-Around Example — Encrypting "Y" with shift 3:**
1. `Y` is at position 24
2. `24 + 3 = 27`
3. `27 % 26 = 1` → `B`

> The `% 26` modulo operation is what makes the alphabet wrap seamlessly from Z back to A.

---

## Python Implementation — Code Breakdown

| Component | Description |
|---|---|
| `caesar_encrypt()` | Applies the forward shift (+n) to each alphabetic character |
| `caesar_decrypt()` | Applies the reverse shift (-n) to restore original text |
| `isalpha()` check | Skips spaces, numbers, and symbols — copies them as-is |
| `isupper()` handling | Treats uppercase (base 65) and lowercase (base 97) separately |

```python
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
```

---

## Output Proof

| Test Input | Shift | Encrypted Output | Decrypted Output | Status |
|---|---|---|---|---|
| `Hello` | 3 | `Khoor` | `Hello` | ✅ |
| `Decode Lab Project` | 1 | `Efdpef Mbc Qspkfdu` | `Decode Lab Project` | ✅ |
| `Internship 2026` | 3 | `Lqwhuqvkls 2026` | `Internship 2026` | ✅ |

---

## Edge Cases Handled

| Edge Case | Handling Approach |
|---|---|
| Spaces & Numbers | `isalpha()` check ensures non-letter characters are copied exactly as-is |
| Uppercase vs Lowercase | Base 65 (A–Z) and base 97 (a–z) used separately to preserve case |
| Custom Shift Key | User inputs their own key every time — fully flexible encryption strength |
| Wrap Around Z→A | `% 26` modulo handles automatic wrap from the end of the alphabet back to the start |

---

## Vulnerability & Evolution

### Caesar Cipher Weakness:
- Only **25 possible keys** — trivial to brute force in seconds
- **Frequency analysis** can crack it without even trying all keys

### Real-World Standard: AES
| | Caesar Cipher | AES-256 |
|---|---|---|
| Role | Foundation — teaches core substitution logic | Real shield — protects real-world data at scale |
| Key Space | 25 keys | 2²⁵⁶ possible keys |
| Technique | Simple shift | Confusion + Diffusion + 128-bit blocks |

---

## Skills Learned

**Technical Skills:**
- ASCII encoding & character mapping
- Modular arithmetic in practice
- Function design & reusability
- Edge case handling

**Cybersecurity Concepts:**
- Data Confidentiality
- Symmetric Encryption
- IPO Model (Input → Process → Output)

---

## Conclusion

**Project 2 Successfully Completed!**

This project demonstrated how classical encryption logic translates directly into code — and laid the conceptual foundation for understanding modern encryption algorithms like AES.

---

*Devki Prajapati | DecodeLabs Cybersecurity Internship | Batch 2026*
