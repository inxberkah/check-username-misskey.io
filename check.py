import requests
import random
import string
#Author Berkah@code:~

headers = {
    'authority': 'misskey.io',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/json',
    'origin': 'https://misskey.io',
    'referer': 'https://misskey.io/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def generate_random_username():
    random_text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
    return random_text

def print_valid_username(username):
    print("\033[92mValid username:", username, "\033[0m")
    save_valid_username(username)

def save_valid_username(username):
    with open('valid_usernames.txt', 'a') as file:
        file.write(username + '\n')

def print_invalid_username(username):
    print("\033[91mInvalid username:", username, "\033[0m")

def process_username(username):
    json_data = {
        'username': username,
    }

    response = requests.post('https://misskey.io/api/username/available', headers=headers, json=json_data)
    response_data = response.json()

    if response_data.get('available'):
        print_valid_username(username)
    else:
        print_invalid_username(username)

def process_random_usernames(num_requests):
    for _ in range(num_requests):
        username = generate_random_username()
        process_username(username)

print("Selamat datang!")
print("1. Gunakan username acak")
print("2. Gunakan username dari file teks")

choice = input("Pilih opsi (1/2): ")
if choice == '1':
    num_requests = 0
    while num_requests <= 0:
        num_requests = int(input("Mau Berapa Username? : "))
    for _ in range(num_requests):
        username = generate_random_username()
        process_username(username)
elif choice == '2':
    file_path = input("File List: ")
    with open(file_path, 'r') as file:
        usernames = file.read().splitlines()
    for username in usernames:
        process_username(username)
else:
    print("Opsi yang dipilih tidak valid.")
