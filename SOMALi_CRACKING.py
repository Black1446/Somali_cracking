import hashlib
import itertools
import string

def crack_hash_from_wordlist(password_hash, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            for password in file:
                password = password.strip()
                if hashlib.sha256(password.encode()).hexdigest() == password_hash:
                    return password
        return None
    except FileNotFoundError:
        print(f"Faylka '{wordlist_file}' lama helin!")
        return None

def crack_hash_bruteforce(password_hash, max_length=4):
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt_str = ''.join(attempt)
            if hashlib.sha256(attempt_str.encode()).hexdigest() == password_hash:
                return attempt_str
    return None

if __name__ == "__main__":
    print("""
    #######################################################
    #                                                     #
    #             🇸🇴(SOMALi_CRACKING) 🇸🇴            #
    #      ██████████████████████████████████████████     #
    #      ██████████████████████████████████████████     #
    #      ███████████   🟦   🌟   🟦   ████████████     #
    #      ██████████████████████████████████████████     #
    #                                                     #
    #            ** EDUCATIONAL PURPOSE ONLY **           #
    #######################################################
    
    CODED BY BLACK1446
    """)

    # Liiska options
    print("\nFadlan dooro mid ka mid ah adeegyada hoos ku qoran:")
    services = ["Facebook", "TikTok", "PUBG", "YouTube", "Twitter", "Instagram", "Telegram", "Snapchat", "WhatsApp", "Gmail"]
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")

    # Doorashada adeegga
    try:
        choice = int(input("\nGali nambarka adeegga (1-10): "))
        if 1 <= choice <= 10:
            selected_service = services[choice - 1]
            print(f"\nWaxaad dooratay: {selected_service}")
        else:
            print("\nDoorasho khaldan! Dib isku day.")
            exit()
    except ValueError:
        print("\nDoorasho khaldan! Dib isku day.")
        exit()

    # Weydii username
    username = input("\nGali username-kaaga: ")

    # Weydii password hash
    hashed_password = input("\nGali sha256 password hash-ka: ")

    # Habka lagu furayo password
    method = input("Ma rabtaa inaad isticmaasho (1) Wordlist ama (2) Brute-force? Doorasho: ")
    
    if method == "1":
        wordlist_file = "passwords.txt"  # Ku qor faylka password-ka
        password = crack_hash_from_wordlist(hashed_password, wordlist_file)
    elif method == "2":
        max_length = int(input("Gali dhererka ugu badan ee password-ka (tusaale: 4): "))
        password = crack_hash_bruteforce(hashed_password, max_length)
    else:
        print("Doorasho khaldan! Dib isku day.")
        exit()

    # Natiijada ugu dambeysa
    if password:
        print(f"\nAdeegga: {selected_service}")
        print(f"Username-kaaga: {username}")
        print(f"Password-ka la helay waa: {password}")
    else:
        print("\nPassword lama helin!")
