import subprocess


def get_applications_list(operating_system):
    match operating_system:
        case "Windows":
            cmd = r"foreach ($UKey in 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\SOFTWARE\Wow6432node\Microsoft\Windows\CurrentVersion\Uninstall\*','HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*','HKCU:\SOFTWARE\Wow6432node\Microsoft\Windows\CurrentVersion\Uninstall\*'){foreach ($Product in (Get-ItemProperty $UKey -ErrorAction SilentlyContinue)){if($Product.DisplayName -and $Product.SystemComponent -ne 1){$Product.DisplayName}}} -> .\InstalledPrograms.txt"
            applications = subprocess.run(
                ["powershell", "-Command", cmd], capture_output=True, text=True
            )
            print("\nList of applications installed\n{}".format(applications.stdout))
