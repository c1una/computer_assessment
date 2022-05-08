import platform
from user_accounts.user_accounts import get_user_accounts
from applications.applications import get_applications_list

# create a folder for this module
def main():
    opearting_system = platform.system()
    match opearting_system:
        case "Windows":
            get_user_accounts("Windows")
            get_applications_list("Windows")

        case "Darwin":
            get_user_accounts("MacOS")


if __name__ == "__main__":
    main()
