class User:
    def __init__(self, login, role):
        self.login = login
        self.role = role

def check_user_admin(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user.role == "админ":
                return func(*args, **kwargs)
            else:
                print(f"Доступ запрещен для {user.login}")
        return wrapper
    return decorator

admin = User("Terminal", "админ")
guest = User("Ardager", "пользователь")

@check_user_admin(admin)
def create_report():
    print("Отчет создан")

@check_user_admin(guest)
def delete_report():
    print("Отчет удален")

if __name__ == "__main__":
    create_report()
    delete_report()