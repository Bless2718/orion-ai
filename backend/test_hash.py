from backend.app.core.security import (
    hash_password,
    verify_password
)

password = "password123"

hashed = hash_password(password)

print("Hash:")
print(hashed)

print("\nVerify:")
print(
    verify_password(
        "password123",
        hashed
    )
)