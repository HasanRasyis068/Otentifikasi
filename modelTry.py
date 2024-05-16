from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    password: str

    def set_password(self, password):
        self.password = hash_password(password)

    def check_password(self, password):
        return self.password == hash_password(password)

    def save(self):
        # Implementasi penyimpanan data pengguna

@dataclass
class ServiceProvider:
    name: str
    email: str
    phone: str
    password: str

    def set_password(self, password):
        self.password = hash_password(password)

    def check_password(self, password):
        return self.password == hash_password(password)

    def save(self):
        # Implementasi penyimpanan data staff pelayanan jasa
