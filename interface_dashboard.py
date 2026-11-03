import getpass
import os
import sys
import time

# Gesimuleerde database/configuratie
USER_DATABASE = {
    "admin": "Thunder123"  # Gebruikersnaam: Wachtwoord
}

NETWORK_CONFIG = {
    "DHCP_Status": "Enabled",
    "Gateway_IP": "192.168.7.137",
    "Subnet_Mask": "255.255.255.0",
    "Stream_Status": "Active (MetaForce)",
    "XML_Engine": "v0.admin_Interface"
}

def clear_screen():
    """Maakt de terminal schoon voor een nette interface."""
    os.system('cls' if os.name == 'nt' else 'clear')

def login_interface():
    """Behandelt het inlogproces."""
    clear_screen()
    print("=" * 45)
    print("        THUNDER OPERATION - LOGIN          ")
    print("=" * 45)
    
    username = input("Gebruikersnaam: ").strip()
    # getpass zorgt ervoor dat het wachtwoord onzichtbaar is tijdens het typen
    password = getpass.getpass("Wachtwoord: ")
    
    if username in USER_DATABASE and USER_DATABASE[username] == password:
        print("\n[+] Toegang verleend. Dashboard laden...")
        time.sleep(1.5)
        return True
    else:
        print("\n[-] Ongeldige inloggegevens. Systeem herstart...")
        time.sleep(2)
        return False

def show_dashboard():
    """Toont het terminal dashboard."""
    while True:
        clear_screen()
        print("=" * 45)
        print("    CONTROL BASE DASHBOARD - METAFORCE    ")
        print("=" * 45)
        print(f" XML Engine  : {NETWORK_CONFIG['XML_Engine']}")
        print(f" DHCP Status : {NETWORK_CONFIG['DHCP_Status']}")
        print(f" Gateway IP  : {NETWORK_CONFIG['Gateway_IP']}")
        print(f" Subnet Mask : {NETWORK_CONFIG['Subnet_Mask']}")
        print(f" Stream State: {NETWORK_CONFIG['Stream_Status']}")
        print("=" * 45)
        print(" [1] Reset XML-Engine")
        print(" [2] Schakel DHCP Om (On/Off)")
        print(" [3] Uitloggen & Sluiten")
        print("=" * 45)
        
        keuze = input("Maak een keuze (1-3): ").strip()
        
        if keuze == "1":
            print("\n[!] XMLCODE herstarten...")
            time.sleep(1)
            print("[+] Herstart succesvol.")
            time.sleep(1)
        elif keuze == "2":
            if NETWORK_CONFIG["DHCP_Status"] == "Enabled":
                NETWORK_CONFIG["DHCP_Status"] = "Disabled"
            else:
                NETWORK_CONFIG["DHCP_Status"] = "Enabled"
            print("\n[+] DHCP-status bijgewerkt!")
            time.sleep(1)
        elif keuze == "3":
            print("\n[+] Veilig uitgelogd. Tot ziens!")
            break
        else:
            print("\n[-] Ongeldige keuze, probeer opnieuw.")
            time.sleep(1)

# Main execution flow
if __name__ == "__main__":
    # Start met de login. Als deze slaagt, open het dashboard.
    if login_interface():
        show_dashboard()
