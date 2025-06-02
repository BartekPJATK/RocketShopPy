def pretty_print(message, tag="INFO"):
    tag = tag.upper()
    tags = {
        "INFO": "\033[94m[INFO]\033[0m",     # niebieski
        "SUCCESS": "\033[92m[SUCCESS]\033[0m", # zielony
        "ERROR": "\033[91m[ERROR]\033[0m",   # czerwony
    }
    print("\n" + "=" * 50)
    print(f"{tags.get(tag, '')} {message}")
    print("=" * 50 + "\n")