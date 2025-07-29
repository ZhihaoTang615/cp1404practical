"""
CP1404/CP5632 Practical
Wikipedia API program
"""

import wikipedia


def main():
    print("Wikipedia Search")
    while True:
        search_phrase = input("Enter page title (or blank to quit): ").strip()
        if not search_phrase:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"\n{page.title}\n{page.summary}\n{page.url}\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()
