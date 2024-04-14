def allowed_dating_age(my_age):
    girls_age = (my_age/2) + 7
    return girls_age

mojo_limit = allowed_dating_age(26 )
print(f'Mojo is allowed to date girls {mojo_limit} years or older.')