import subprocess


def get_user_accounts(opearting_system):
    match opearting_system:
        case "Windows":
            users = subprocess.run(
                ["wmic", "useraccount", "get", "name"], capture_output=True, text=True
            ).stdout
            print("List of users\n{}".format(users.split()[1:-1]))
        case "MacOS":
            users = subprocess.run(
                ["dscl", ".", "list", "/Users", "|", "grep", "-v", "“^_”"],
                capture_output=True,
                text=True,
            )
            print("".format(users))
