import os
import asyncio

try:
    import aiohttp
except ModuleNotFoundError:
    os.system('pip install aiohttp')

os.system("cls && title Tellonym Username Checker ^| github.com/Plasmonix") 

class Tellonym:
    def __init__(self):
        self.available = 0
        self.unavailable = 0
        self.errors = 0
        self.update_title = lambda: os.system(f"title Tellonym Username Checker - Available: {self.available} ^| Unavailable: {self.unavailable} ^| Errors: {self.errors}") 

    def hit_saver(self, arg: str):
        with open('hits.txt', 'a', encoding='utf8') as f:
            f.write(f'{arg}\n')

    async def checker(self):
        async with aiohttp.ClientSession() as client:
            for username in open(self.username_list, "r", encoding="utf8").read().splitlines():
                try:
                    async with client.get(f"https://tellonym.me/{username}", headers={'Host': 'tellonym.me','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36','Accept-Language': 'ar','Connection': 'keep-alive'}) as res:
                        if res.status == 200:
                            print(f"[\x1b[32mAVAILABLE\x1b[0m] {username}")
                            self.available += 1
                            self.hit_saver(username)
                            self.update_title()
                        else:
                            print(f"[\x1b[31mUNAVAILABLE\x1b[0m] {username}")
                            self.unavailable += 1
                            self.update_title()
                except:
                    print(f"[\x1b[31mFAILURE\x1b[0m] Could not establish connection.")
                    self.errors += 1
    
    def main(self):
        self.username_list = input('\x1b[36m>\x1b[0m Username list: ')
        os.system("cls")
        asyncio.run(self.checker())

if __name__ == "__main__":
    n = Tellonym()
    n.main()
    