def is_strong_password(password: str) -> bool:
    if len(password) < 6:
        return False

    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    special_count = sum(1 for ch in password if not ch.isalnum())

    return has_digit and has_upper and has_lower and special_count >=2

print(is_strong_password(("$PassW/12")))
print(is_strong_password("&&&!!!"))
print(is_strong_password("k2-iR!49"))
print(is_strong_password("12345"))
print(is_strong_password("3gT*5&0"))
print(is_strong_password("password"))

