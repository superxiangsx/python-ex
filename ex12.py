from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you love me, {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}")
address = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about loving me.
You live in {address}. Not sure where it is.
And you have a {computer} computer. Nice
"""
)
