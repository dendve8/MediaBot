import os
import subprocess
import zipfile
from datetime import datetime

def show_banner():
    banner = """
\033[96m
╔═══ Z3R0S3S ══════════════════╗
║ Mega Mass Downloader Tools V1║
╚═══════════════ EST 2024 ═════╝\033[0m"""
    print(banner)

def instagram_downloader():
    try:
        print("\033[36mInstagram Downloader is running...\033[0m")
        lib_folder = os.path.join(os.path.dirname(__file__), 'lib')
        instagram_script = 'instagram.py'
        path_instagram_script = os.path.join(lib_folder, instagram_script)
        subprocess.run(['python', path_instagram_script])
    except KeyboardInterrupt:
        print("\033[31mEngine Stopped!!!\033[0m")

def youtube_downloader():
    try:
        print("\033[36mYoutube Downloader is running...\033[0m")
        lib_folder = os.path.join(os.path.dirname(__file__), 'lib')
        youtube_script = 'youtube.py'
        path_youtube_script = os.path.join(lib_folder, youtube_script)
        subprocess.run(['python', path_youtube_script])
    except KeyboardInterrupt:
        print("\033[31mEngine Stopped!!!\033[0m")

def zip_folder(folder_path, zip_name):
    try:
        print(f"\033[36mZipping {folder_path}...\033[0m")
        zip_filename = f"{datetime.now().strftime('%Y-%m-%d')}_{zip_name}.zip"
        zip_filepath = os.path.join(os.path.dirname(__file__), zip_filename)
        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        print(f"\033[32mZip file created: {zip_filepath}\033[0m")
    except Exception as e:
        print(f"\033[31mError zipping folder: {e}\033[0m")

def main():
    show_banner()

    while True:
        try:
            print("\033[36m\n╔═══════════════════════════════\033[0m")
            print("\033[36m║ 1. Instagram Downloader \033[0m")
            print("\033[36m║ 2. Youtube Downloader \033[0m")
            print("\033[36m║ 3. Zip folder Result \033[0m")
            print("\033[36m║ 4. Exit \033[0m")
            choice = input("\033[33mEnter your choice (1/2/3/4): \033[0m")

            if choice == '1':
                instagram_downloader()
            elif choice == '2':
                youtube_downloader()
            elif choice == '3':
                print("\033[36m\n╔═══════════════════════════════\033[0m")
                print("\033[36m║ 1. Zip From Instagram \033[0m")
                print("\033[36m║ 2. Zip From Youtube \033[0m")
                zip_choice = input("\033[33mEnter your choice (1/2): \033[0m")
                if zip_choice == '1':
                    zip_folder('result_insta', 'insta')
                elif zip_choice == '2':
                    zip_folder('result_youtube', 'youtube')
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            elif choice == '4':
                print("Exiting Mega Mass Downloader Tools...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except KeyboardInterrupt:
            print("\033[31mEngine Stopped!!!\033[0m")
            break

if __name__ == "__main__":
    main()
