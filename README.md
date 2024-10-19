# TwistyCrypt

TwistyCrypt is a playful yet powerful bit-level encryption and verification tool designed to encrypt passwords by flipping bits based on the password length. The package includes two key modules: `encrypt.py` to perform encryption and password hashing, and `verify.py` to verify the hashed passwords.

## Features

- Encrypts passwords using a custom bit-flipping algorithm.
- Dynamically adjusts the number of bits flipped based on the password length.
- Uses `bcrypt` for password hashing.
- Verifies entered passwords against their stored hash.

## Prerequisites

Make sure you have `bcrypt` installed. You can install it using `pip`:

```bash
pip install bcrypt

