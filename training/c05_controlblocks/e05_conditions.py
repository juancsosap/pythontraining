print('Email Validator'.center(50))
print(''.center(50,'-'))
email = input('Email: ')

print(''.center(50,'-'))

# Changing to Lower Case
email = email.lower()

# Has only one @
has_at = ('@' in email)
is_one = (email.find('@') == email.rfind('@'))
print(has_at, is_one)
valid = has_at and is_one
if(valid):
    ati = email.find('@')
    # Spliting email
    nick, domain = email[:ati], email[ati+1:]

    # The nick and domain length is almost 4 characters
    nick_len = (len(nick) >= 4)
    domain_len = (len(domain) >= 4)
    print(nick_len, domain_len)
    valid = valid and nick_len and domain_len

    # Only start with letters
    startwith_letters = nick[0].isalpha()
    print(startwith_letters)
    valid = valid and startwith_letters

    # Has almost one dot in the domain part
    has_dot = ('.' in domain)
    print(has_dot)
    valid = valid and has_dot

    # The dot is almost 2 characters from the end
    last_dot = not ('.' in domain[-2:])
    print(last_dot)
    valid = valid and last_dot

print(''.center(50,'-'))

print("Valid Email" if valid else "Invalid Email")
