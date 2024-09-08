import os
from pytube import YouTube
from pytube import Channel
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

        print(Fore.GREEN + f"Procces Downloading ........ : {video_title}")
        video_stream.download(output_path=destination_folder, filename=f"{video_title}.{file_extension}")
        print(Fore.GREEN + "Download Completed Saved to :", file_path)

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
            print(Fore.YELLOW + f"{total_urls} Url From {file_path}")
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

def grab_playlist_urls(channel_url):
    try:
        channel = Channel(channel_url)
        playlist_url = channel.get_playlist_url()

        if not playlist_url:
            raise ValueError("No playlists found for the given channel.")

        playlist = channel.playlist_url(playlist_url)
        playlist_urls = [video.url for video in playlist.videos]

        return playlist_urls

    except Exception as e:
        print(Fore.RED + "Error:", str(e))
        return []

if __name__ == "__main__":
    banner = """
\033[31m
╔═══ Z3R0S3S ══════════════════╗
║ Mass Downloader Youtube  V.1 ║
╚═══════════════ EST 2024 ═════╝\033[0m"""

    print(banner)
    while True:
        print(Fore.CYAN + "=========================")
        print(Fore.CYAN + "| 1. Download Single Link ")
        print(Fore.CYAN + "| 2. Download Bulk Links")
        print(Fore.CYAN + "| 3. Grab URLs From Yt Channel By List")
        print(Fore.CYAN + "| 4. Exit")
        print(Fore.CYAN + "=========================")
        print(Style.RESET_ALL)
        choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4): " + Style.RESET_ALL)

        if choice == "1":
            video_url = input(Fore.YELLOW + "Input YouTube URL: ")
            result_folder = input(Fore.YELLOW + "Enter the Result Folder name (example: Result): ")
            file_extension = input(Fore.YELLOW + "Enter file extension (mp4/mp3): ").lower()
            download_video(video_url, result_folder, file_extension)

        elif choice == "2":
            file_path = input(Fore.YELLOW + "Please Input Name File bulk Url: ")
            result_folder = input(Fore.YELLOW + "Enter the Result Folder name (example: Result): ")
            file_extension = input(Fore.YELLOW + "Enter file extension (mp4/mp3): ").lower()
            download_bulk_videos(file_path, result_folder, file_extension)

        elif choice == "3":
            channel_url = input(Fore.YELLOW + "Please Input Channel URL: ")
            result_folder = input(Fore.YELLOW + "Enter the Result Folder name (example: Result): ")

            playlist_urls = grab_playlist_urls(channel_url)
            if playlist_urls:
                with open('playlist_urls.txt', 'w') as file:
                    for url in playlist_urls:
                        file.write(f"{url}\n")
                print(Fore.GREEN + "Playlist URLs saved to playlist_urls.txt")

                download_bulk_videos('playlist_urls.txt', result_folder)
            else:
                print(Fore.RED + "No playlists found for the given channel.")

        elif choice == "4":
            print("Thanks, Bot Ending, See you...")
            break

        else:
            print("Please choose correctly...")
