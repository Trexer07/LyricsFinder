import requests, os, json

os.system("title Lyrics Finder Made By Trexer")
os.system("cls")
print("API 제공 : 윈섭 Winsub")
print("="*30)

api_key = "윈섭 api 키" #https://api.winsub.kr

def finder(artist, song):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    api = f"https://api.winsub.kr/lyrics/?key={api_key}&artist={artist}&name={song}"
    req = requests.post(api, headers=header)
    req.encoding ="utf-8"
    res = req.json()['ly']['ly']
    rep = res.replace("<br>", "\n")
    return rep



artist = str(input("노래 아티스트를 입력해주세요 : "))
song = str(input("노래 제목을 입력해주세요 : "))
artist = artist.replace(" ", "")
song = song.replace(" ", "")
lyrics = finder(artist, song)
f = open(f"{artist.upper()}ㅣ{song.upper()}.txt", "w")
f.write(lyrics)

