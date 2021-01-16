from des import DesKey


class DesAlgorithm:

    def __init__(self, key):
        self.key = DesKey(str.encode(key))

    def encrypt(self, msg):
        data_bytes = str.encode(msg)
        encrypted = self.key.encrypt(data_bytes, padding=True)
        return encrypted.decode('latin-1')

    def decrypt(self, msg):
        data_bytes = str.encode(msg, 'latin-1')
        decrypted = self.key.decrypt(data_bytes, padding=True)
        return decrypted.decode('latin-1')
