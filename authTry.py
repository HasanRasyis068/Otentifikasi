from models import User, ServiceProvider

def authenticate_user(username, password):
    """Melakukan pengecekan kredensial pengguna"""
    user = User.get_by_username(username)
    if user and user.check_password(password):
        return user
    return None

def register_user(username, email, password):
    """Mendaftarkan pengguna baru"""
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def register_service_provider(name, email, phone, password):
    """Mendaftarkan staff pelayanan jasa baru"""
    provider = ServiceProvider(name=name, email=email, phone=phone)
    provider.set_password(password)
    provider.save()
    return provider
