import os


def main():
    name = os.getenv("USERNAME")
    language = os.getenv("LANGUAGE")
    print(f"Hello {name} from GithubActions using {language}")


if __name__ == "__main__":
    main()
