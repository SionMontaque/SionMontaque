import hashlib

def sha256sum(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == '__main__':
    path = input('Enter file path to hash: ')
    try:
        print('SHA256:', sha256sum(path))
    except Exception as e:
        print('Error:', e)
