import hashlib

def hash_file(filename):  # This is a function to get the hash name of the file.
    h = hashlib.sha1()

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def get_sha(data):
    return hashlib.sha256(data.encode()).hexdigest()

