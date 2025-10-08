import re

def score_password(pwd):
    score = 0
    if len(pwd) >= 8:
        score += 1
    if re.search(r'[A-Z]', pwd):
        score += 1
    if re.search(r'[a-z]', pwd):
        score += 1
    if re.search(r'\d', pwd):
        score += 1
    if re.search(r'[^A-Za-z0-9]', pwd):
        score += 1
    return score

if __name__ == '__main__':
    pwd = input('Enter password to check: ')
    s = score_password(pwd)
    print(f'Password strength score (0-5): {s}')
