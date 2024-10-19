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
```
## Installation

Clone the repository or download the encrypt.py and verify.py files to your local machine.
```bash
git clone https://github.com/PoornavG/TwistyCrypt.git
cd TwistyCrypt
```

## Usage

### Encrypt a Password and Generate Hash

The `encrypt.py` script encrypts a password and generates a bcrypt hash using a bit-flipping algorithm.

1. Run the `encrypt.py` script:

   ```bash
   python encrypt.py
   ```
2.Enter the password when prompted:

  ```bash
      Enter the password: Hello123
  ```

## Verify a Password Against a Hash

The verify.py script verifies if the entered password matches the stored hash.

1.Run the verify.py script:

```bash
python verify.py
```

2.Enter the password and the hashed password for verification:

```bash
Enter the password for verification: Hello123
Enter the hashed password: b'$2b$12$grm.2E9oSppejVt6t92WduYu34kb6p8Rn2meTUzRbCMnouLcCAgOS'
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

