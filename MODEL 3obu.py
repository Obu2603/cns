import hashlib

password = input("Enter your password: ")

hashed_password = hashlib.sha1(password.encode()).hexdigest()

print("The resulting SHA-1 message digest for the password is:")
print(hashed_password)
