def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter something!")

def main():
    print("==== Welcome to Mad Libs Game ====")
    thing = get_input("Enter a noun: ")
    place = get_input("Enter a place name: ")
    quality = get_input("Enter a quality of something: ")

    story = f"{thing} is my favorite name. I become happy when I see {place}, which has {quality}."
    print("\n---- Your Mad Libs Story ---")
    print(story)


if __name__ == "__main__":
    main()
