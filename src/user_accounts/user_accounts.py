import subprocess
import yaml


def read_yaml():
    with open("src/config.yaml", "r") as f:
        return yaml.safe_load(f)


def get_user_accounts(opearting_system):
    match opearting_system:
        case "Windows":
            users = subprocess.run(
                ["wmic", "useraccount", "get", "name"], capture_output=True, text=True
            ).stdout
            print("List of users\n{}".format(users.split()[1:-1]))
        case "Darwin":
            cmd = r"dscl . list /Users | grep -v '_'"
            process = subprocess.run(
                ["/bin/bash", "-c", cmd],
                capture_output=True,
                text=True,
            )
            user_accounts = process.stdout
            output(user_accounts)


def output(string):
    with open("user_accounts.txt", "w") as f:
        return f.write(string)
