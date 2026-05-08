class User:
    # атрибуты класса
    user_count = 0
    default_password = "123456789"

    def __init__(self, name, phone):
        # атрибуты экземпляра
        self.name = name
        self.phone = phone
        self.role = "user"
        self.password = User.default_password
        User.user_count += 1

    def test(self):
        print(User.user_count, User.default_password)

    @classmethod
    def create_admin(cls, name, phone):
        # для особенного создания объектов
        admin = cls(name, phone)
        admin.role = "admin"
        admin.password = "qwerty"
        print(cls.get_user_count())
        return admin

    @classmethod
    def get_user_count(cls):
        return User.user_count

    @staticmethod
    def validate_password(password):
        # для проверки длины пароля
        if len(password) < 8:
            return False
        else:
            return True

        # short version
        return len(password) >= 8

    def change_password(self, new_password):
        if not User.validate_password(new_password):
            raise ValueError("Пароль слишком короткий")
        self.password = new_password

print(f"Количество юзеров: {User.user_count}")
user1 = User("Igor", "996555000001")
print(f"Количество юзеров: {User.user_count}")
user2 = User("Artur", "996555000002")
print(f"Количество юзеров: {User.user_count}")
user1.test()
user2.test()
print(f"Passwords: {user1.password}, {user2.password}")
print(f"Class attributes: {User.user_count}, {User.default_password}")
admin1 = User.create_admin("Kurmanbek", "996000003")
print(f"Admin user: {admin1.name}, {admin1.phone}, {admin1.role}, {admin1.password}")
print(f"User count:", User.get_user_count())
print(User.validate_password("xxxxxxxxxxx"))
user1.change_password("1ilehrgkfjdgljfdk")