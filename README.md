# TwistyCrypt
This repository contains Python programs to hash passwords and verify them using bcrypt. The hashing process includes a custom salt generation mechanism with a dynamic bit inversion for enhanced security.

Features
Custom Salt Generation: Dynamically generates a salt by hashing the password using SHA-256 and inverting a set number of bits in the first 9 characters of the hash.
Dynamic Bit Inversion: The number of bits inverted is based on the password length modulo 8. If the result is zero, it defaults to inverting 6 bits.
Password Hashing: Uses bcrypt to securely hash passwords.
Password Verification: Verifies the input password by comparing it with the provided hashed password.
File Overview
encrypt.py
This file contains the logic for:

Generating a custom salt from a password.
Hashing the password using bcrypt with the generated salt.
Functions
invert_bits(c, num_bits_to_invert): Inverts a specified number of bits in the binary representation of a character.
encrypt_memory(data, num_bits_to_invert): Applies bit inversion to the first 9 characters of the hashed password.
generate_salt(password): Generates a custom salt by encrypting the password hash using dynamic bit inversion.
hash_password(password): Hashes the password using bcrypt with a generated salt.
main(): Accepts user input for the password, generates a salted hash, and prints it.
Usage
Run the script:
bash
Copy code
python encrypt.py
Enter a password. The script will output the hashed password.
verify.py
This file contains the logic for verifying a password against a stored hash.

Functions
invert_bits(c, num_bits_to_invert): Same as in encrypt.py.
encrypt_memory(data, num_bits_to_invert): Same as in encrypt.py.
generate_salt(password): Same as in encrypt.py.
verify_password(entered_password, hashed_password): Verifies if the entered password matches the provided hashed password.
main(): Accepts user input for a password and the hashed password, and checks if they match.
Usage
Run the script:
bash
Copy code
python verify.py
Enter the password for verification and the previously hashed password.
The script will output whether the verification was successful or failed.
Example
Hashing a Password
bash
Copy code
$ python encrypt.py
Enter the password: Hello123
Hashed Password: b'$2b$12$grm.2E9oSppejVt6t92WduYu34kb6p8Rn2meTUzRbCMnouLcCAgOS'
Verifying a Password
bash
Copy code
$ python verify.py
Enter the password for verification: Hello123
Enter the hashed password: b'$2b$12$grm.2E9oSppejVt6t92WduYu34kb6p8Rn2meTUzRbCMnouLcCAgOS'
Password verification successful!
Test Cases
For more details on how to test the scripts using various edge cases, please refer to the Test Cases section in the project description.

Dependencies
Make sure you have the following Python libraries installed:

bcrypt
hashlib
Install dependencies using pip:

bash
Copy code
pip install bcrypt
License
This project is licensed under the MIT License.

Contributing
Feel free to open issues or pull requests to contribute to the project.

Author
PoornavG - GitHub: https://github.com/PoornavG

