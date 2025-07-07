from programming_language import ProgrammingLanguage

def main():
    """Test the ProgrammingLanguage class."""

    # Create language objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print one language to test __str__ method
    print(python)

    # Put the languages into a list
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()

