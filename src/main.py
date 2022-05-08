import platform
from user_accounts.user_accounts import get_user_accounts
from applications.applications import get_applications

# create a folder for this module
def main():
    opearting_system = platform.system()
    get_user_accounts(opearting_system)
    # get_applications(opearting_system)


if __name__ == "__main__":
    main()
