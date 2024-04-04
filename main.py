def count_words(text):
    return len(text.split())

def count_letters(text):
    text = text.lower()
    result = [
        {"char":"a", "count":0},
        {"char":"b", "count":0},
        {"char":"c", "count":0},
        {"char":"d", "count":0},
        {"char":"e", "count":0},
        {"char":"f", "count":0},
        {"char":"g", "count":0},
        {"char":"h", "count":0},
        {"char":"i", "count":0},
        {"char":"j", "count":0},
        {"char":"k", "count":0},
        {"char":"l", "count":0},
        {"char":"m", "count":0},
        {"char":"n", "count":0},
        {"char":"o", "count":0},
        {"char":"p", "count":0},
        {"char":"q", "count":0},
        {"char":"r", "count":0},
        {"char":"s", "count":0},
        {"char":"t", "count":0},
        {"char":"u", "count":0},
        {"char":"v", "count":0},
        {"char":"w", "count":0},
        {"char":"x", "count":0},
        {"char":"y", "count":0},
        {"char":"z", "count":0}
    ]

    for character in text:
        for part in result:
            if part["char"] == character:
                part["count"] += 1

    return result

def sort_on(dict):
    return dict["count"]

def my_sort(letter_count):
    letter_count.sort(reverse=True, key=sort_on)
    return letter_count

def print_story(text):
    print(text)

def print_report(story_dir, word_count, letter_count):
    sorted_letter_count = my_sort(letter_count)

    print(f"--- Begin report of {story_dir} ---")
    print(f"{word_count} words found in the document")
    print("")
    for part in sorted_letter_count:
        print(f"The '{part["char"]}' character was found {part["count"]} times")
    print("--- End report ---")

story_dir = "./books/frankenstein.txt"

contents = ""
with open(story_dir, "r") as file:
    contents = file.read()

print_story(contents)
word_count = count_words(contents)
letter_count = count_letters(contents)

print(word_count)
print(letter_count)

print_report(story_dir, word_count, letter_count)