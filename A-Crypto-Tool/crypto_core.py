import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class FileEncryptor:
    """Gelişmiş dosya şifreleme motoru."""
    
    def __init__(self, password: str):
        self.password = password.encode()

    def _derive_key(self, salt: bytes) -> bytes:
        """Şifreden 100.000 iterasyon ile güvenli bir anahtar türetir."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
        )
        return base64.urlsafe_b64encode(kdf.derive(self.password))

    def encrypt_file(self, file_path: str):
        salt = os.urandom(16)
        key = self._derive_key(salt)
        fernet = Fernet(key)

        with open(file_path, 'rb') as f:
            data = f.read()

        encrypted_data = fernet.encrypt(data)
        
        # Salt ve şifreli veriyi dosyaya yaz
        with open(file_path + ".enc", 'wb') as f:
            f.write(salt + encrypted_data)

    def decrypt_file(self, file_path: str):
        with open(file_path, 'rb') as f:
            raw_data = f.read()

        salt = raw_data[:16]
        encrypted_data = raw_data[16:]
        
        key = self._derive_key(salt)
        fernet = Fernet(key)
        
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Orijinal dosyayı kurtar
        original_name = file_path.replace(".enc", "")
        with open("recovered_" + original_name, 'wb') as f:
            f.write(decrypted_data)