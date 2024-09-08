import os
from pytube import YouTube, Playlist
from colorama import Fore, Style, init

init(autoreset=True)

def download_video(url, destination_folder, file_extension='mp4'):
    try:
        yt = YouTube(url)
        
        if file_extension == 'mp4':
            video_stream = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
        elif file_extension == 'mp3':
            video_stream = yt.streams.filter(only_audio=True).first()
        else:
            raise ValueError("Invalid file extension. Supported extensions: mp4, mp3")

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        video_title = yt.title.replace("/", "-").replace("\\", "-").replace(":", "-").replace("*", "-").replace("?", "-").replace("\"", "-").replace("<", "-").replace(">", "-").replace("|", "-")
        file_path = os.path.join(destination_folder, f"{video_title}.{file_extension}")

        print(Fore.GREEN + f"Processing Download ........ : {video_title}")
        video_stream.download(output_path=destination_folder, filename=f"{video_title}.{file_extension}")
        print(Fore.GREEN + "Download Completed. Saved to :", file_path)

    except Exception as e:
        print(Fore.RED + "Error:", str(e))
    finally:
        print(Style.RESET_ALL)

def download_bulk_videos(file_path, destination_folder, file_extension='mp4'):
    try:
        with open(file_path, 'r') as file:
            video_urls = file.readlines()
            total_urls = len(video_urls)

            print(Fore.RED + "===========================")
            print(Fore.YELLOW + f"{total_urls} URLs from {file_path}")
            print(Fore.BLUE + f"Ready To Downloading To {file_extension}")
            print(Fore.RED + "===========================")
            print(Style.RESET_ALL)      

            for idx, video_url in enumerate(video_urls, start=1):
                print(f"Processing {idx}/{total_urls}...")
                video_url = video_url.strip()
                download_video(video_url, destination_folder, file_extension)

            print("Download of all videos completed!")

    except Exception as e:
        print(Fore.RED + "Error:", str(e))
    finally:
        print(Style.RESET_ALL)

def download_playlist(username, playlist_index, destination_folder, file_extension='mp4'):
    try:
        playlist = Playlist(f"https://www.youtube.com/playlist?list={username}")
        playlist.populate_video_urls()

        total_videos = len(playlist.video_urls)
        print(Fore.RED + "===========================")
        print(Fore.YELLOW + f"{total_videos} Videos in Playlist")
        print(Fore.BLUE + f"Ready To Downloading To {file_extension}")
        print(Fore.RED + "===========================")
        print(Style.RESET_ALL)

        for idx, video_url in enumerate(playlist.video_urls, start=1):
            print(f"Processing {idx}/{total_videos}...")
            download_video(video_url, destination_folder, file_extension)

        print("Download of all playlist videos completed!")

    except Exception as e:
        print(Fore.RED + "Error:", str(e))
    finally:
        print(Style.RESET_ALL)

if __name__ == "__main__":
    banner = """
\033[31m
╔═══ Z3R0S3S ══════════════════╗
║ Mass Downloader Youtube  V.1 ║
╚═══════════════ EST 2024 ═════╝\033[0m"""

    print(banner)
    while True:
        print(Fore.CYAN + "=========================")
        print(Fore.CYAN +"| 1. Download Single Link ")
        print(Fore.CYAN +"| 2. Download Bulk Links")
        print(Fore.CYAN +"| 3. Download Playlist")
        print(Fore.CYAN +"| 4. Exit")
        print(Fore.CYAN + "=========================")
        print(Style.RESET_ALL)
        choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

        if choice == "1":
            video_url = input(Fore.YELLOW +"Input YouTube URL: ")
            result_folder = input(Fore.YELLOW + "Enter the Result Folder name (example: Result): ")
            file_extension = input(Fore.YELLOW + "Enter file extension (mp4/mp3): ").lower()
            download_video(video_url, result_folder, file_extension)

        elif choice == "2":
            file_path = input(Fore.YELLOW + "Please Input Name File bulk Url: ")
            result_folder = input(Fore.YELLOW + "Enter the Result Folder name (example: Result): ")
            file_extension = input(Fore.YELLOW + "Enter file extension (mp4/mp3): ").lower()
            download_bulk_videos(file_path, result_folder, file_extension)

        elif choice == "3":
            username = input(Fore.YELLOW + "Enter YouTube username: ")
            playlist_index = input(Fore.YELLOW + "Enter the playlist index (default: 0): ")
            result_folder = input(Fore.YELLOW + "Enter the Result Folder name (example: Result): ")
            file_extension = input(Fore.YELLOW + "Enter file extension (mp4/mp3): ").lower()
            download_playlist(username, playlist_index, result_folder, file_extension)

        elif choice == "4":
            print("Thanks, Bot Ending, See you...")
            break

        else:
            print("Please choose correctly...")
