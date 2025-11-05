from oops_project import chatbook

user1 = chatbook()
print(user1._chatbook__name)  # Accessing the mangled private variable
print(user1.id)


user2 = chatbook()
print(user2.id)


chatbook.set_id(10)
user3 = chatbook()
print(user3.id)

# getter and setter
print(user1.get_name())
user1.set_name('agent')
print(user1.get_name())