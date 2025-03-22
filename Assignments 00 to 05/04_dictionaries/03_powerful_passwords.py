import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    """
    Checks if the provided password matches the stored hashed password.
    :param email: The email associated with the login.
    :param password_to_check: The password to verify.
    :param stored_logins: A dictionary storing email-password_hash pairs.
    :return: True if the password matches, False otherwise.
    """
    if email not in stored_logins:
        return False
    return stored_logins[email] == hash_password(password_to_check)

def main():
    # Example stored logins with hashed passwords
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "admin@example.com": hash_password("adminpassword"),
    }
    
    # Test cases
    print(login("user@example.com", "securepassword123", stored_logins))  # Expected: True
    print(login("admin@example.com", "wrongpassword", stored_logins))  # Expected: False
    print(login("notregistered@example.com", "password", stored_logins))  # Expected: False

if __name__ == '__main__':
    main()