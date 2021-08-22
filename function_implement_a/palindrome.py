def isPalindrome(s):
    if not s:
        print('s cannot be empty!')
        raise

    if len(s) > 200000:
        print('s is too long!')
        raise

    if not s.isascii():
        print('s is not in ASCII!')
        raise

    q = ''.join(filter(str.isalnum, s)).lower()
    if q == q[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print('true' if isPalindrome(input('s = ')) else 'false')
