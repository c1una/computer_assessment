import platform


def main():    
    os = platform.system
    match os:
        case "Windows":
            return "Windows"
        case "Darwin":
            return "MacOS"
        


if __name__ == "__main__":
    print(main())
