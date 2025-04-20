import hashlib

# Function to hash a password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to log in a user
def login(email, password_to_check, stored_logins):
    hashed_input = hash_password(password_to_check)  # Hash the input password
    stored_hash = stored_logins.get(email)  # Get the stored hash for this email
    
    return hashed_input == stored_hash  # Compare the two hashes


def main():
    # Example stored logins: emails mapped to password hashes
    stored_logins = {
        "alice@gmail.com": hash_password("apple123"),
        "bob@gmail.com": hash_password("banana456"),
        "charlie@gmail.com": hash_password("carrot789"),
        "admin@gmail.com": hash_password("admin123")
    }

    # Simulate a login
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == '__main__':
    main()
