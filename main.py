def print_story(text):
    print(text)

contents = ""
with open("./books/frankenstein.txt", "r") as file:
    contents = file.read()

print_story(contents)