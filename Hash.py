import bcrypt
import hashlib

def invert_bits(c, num_bits_to_invert):
    # Get binary string representation, zero-padded to 8 bits
    binary_str = f"{ord(c):08b}"
    # Invert the specified number of bits
    inverted_binary = ''.join(
        '1' if bit == '0' and i < num_bits_to_invert else '0' if bit == '1' and i < num_bits_to_invert else bit
        for i, bit in enumerate(binary_str)
    )
    # Convert back to a character
    return chr(int(inverted_binary, 2))

def encrypt_memory(data, num_bits_to_invert):
    # Encrypt the data by inverting the specified number of bits of each character
    return ''.join(invert_bits(c, num_bits_to_invert) for c in data)

def generate_salt(password):
    # First, hash the password using sha256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Encrypt the first 9 characters of the hash (like the C function does)
    partial_hashed_password = hashed_password[:9]

    # Determine how many bits to invert, dynamically based on length % 8
    password_length = len(password)
    num_bits_to_invert = password_length % 8  # Dynamic bit inversion

    # Avoid 0-bit inversion by defaulting to 7 bits if mod result is 0
    if num_bits_to_invert == 0:
        num_bits_to_invert = 6

    encrypted_salt = encrypt_memory(partial_hashed_password, num_bits_to_invert)

    # Split into three parts
    part1 = encrypted_salt[:3]  # Front part
    part2 = encrypted_salt[3:6]  # Middle part
    part3 = encrypted_salt[6:]   # Rear part

    # Determine where to insert the middle part based on password length
    if password_length % 2 == 0:
        mid_index = password_length // 2
    else:
        mid_index = (password_length // 2) + 1

    # Build the salted password
    salted_password = part1 + password[:mid_index] + part2 + password[mid_index:] + part3

    return salted_password

def hash_password(password):
    """
    Hash the password without using salt using bcrypt.
    """
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    # Generate the hash using bcrypt
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())  # Use default salt from bcrypt
    return hashed_password

def validate_password_input(password):
    """
    Validate that the password is not empty and meets basic length requirements.
    """
    if not password:
        print("Error: Password cannot be empty.")
        return False
    elif len(password) < 6:
        print("Error: Password must be at least 6 characters long.")
        return False
    return True

def main():
    # Example password input
    password = input("Enter the password: ")

    # Validate the password
    if not validate_password_input(password):
        return  # Exit if password is invalid

    # Generate a custom salt based on the password (for reference, not used in hashing)
    salted_password = generate_salt(password)

    # Hash the password without using the custom salt
    hashed_password = hash_password(salted_password)
    print(f"Hashed Password: {hashed_password}")

if __name__ == "__main__":
    main()
