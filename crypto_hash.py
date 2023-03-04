import hashlib
import json


def crypto_hash(data):
    """
    Return a sha-256 hash of the given data.
    """
    stringified_data = json.dumps(data)
    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('foo'): {crypto_hash('foo')}")


if __name__ == '__main__':
    main()
