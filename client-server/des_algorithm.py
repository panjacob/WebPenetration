from des import DesKey

"""
Title
-----
    DES algorithm adapted for current project

Author
-------
    Jakub Kwiatkowski
    Rafał Kreft
    
Description
-----------
DES encryption/decryption algorithm used from the previous project,
adapted to client server communication:
https://github.com/panjacob/Enigma2.0/blob/master/des_algorithm.py


DES - is a block cipher algorithm that takes plain text in blocks of 64 bits 
      and converts them to ciphertext using keys of 48 bits. It is a symmetric
      key algorithm, which means that the same key is used for encrypting and 
      decrypting data.

Source of encryption module      
---------------------------
https://pypi.org/project/des/
"""


class DesAlgorithm:
    """
    A class to represents DES encryption and decryption functions.

    Methods
    -------
        encrypt(self, data):
            Encrypts and encodes data input
        decrypt(self, data):
            Decrypts and decodes encrypted data
    """

    def __init__(self, key):
        """
        Creates DesKey from given plain text

        Parameters
        ----------
            key : String
                User-specified plain text encryption key
        """
        self.key = DesKey(str.encode(key))

    def encrypt(self, msg):
        """
        Takes in plain text data and encrypts it with DES/DES3 algorithm.

        Parameters
        ----------
            msg : String
                User-specified plain text message

        Returns
        -------
            encrypted : bytes object
                DES-encrypted result
        """
        data_bytes = str.encode(msg)
        encrypted = self.key.encrypt(data_bytes, padding=True)
        return encrypted.decode('latin-1')

    def decrypt(self, msg):
        """
         Takes in plain text data and decrypts it with DES algorithm.

         Parameters
         ----------
             msg : String
                 Encrypted input data

         Returns
         -------
             decrypted : bytes object
                 DES-decrypted result
         """
        data_bytes = str.encode(msg, 'latin-1')
        decrypted = self.key.decrypt(data_bytes, padding=True)
        return decrypted.decode('latin-1')
