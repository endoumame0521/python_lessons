# import user
# from user import AdminUser

# import mypackage.user as mymodule

from mypackage.user import AdminUser

# bob = user.AdminUser("bob", 23)
bob = AdminUser("bob", 23)

print(bob.name)
bob.say_hi()
bob.say_hello()