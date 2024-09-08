import instaloader
from instaloader import Profile
import os

L = instaloader.Instaloader(download_videos=True,download_pictures=True,dirname_pattern="result_insta/{target}", download_video_thumbnails=False, compress_json=False, save_metadata=False)

def insta_bulk_download(target_username, option):
    try:
        profile = Profile.from_username(L.context, target_username)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"\033[31m║ User {target_username} not found or is Privacy .\033[0m")
        return

    result_folder = os.path.join(target_username.replace("/", "_"))
    posts_to_download = []

    if option == 1: 
        posts_to_download.extend(post for post in profile.get_posts() if post.is_video)
    elif option == 2:  
        posts_to_download.extend(post for post in profile.get_posts() if not post.is_video)
    elif option == 3:  
        posts_to_download.extend(profile.get_stories())
    elif option == 4:  
        posts_to_download.extend(profile.get_tagged_posts())
    elif option == 5:  
        posts_to_download.extend(post for post in profile.get_posts() if post.is_video)
        posts_to_download.extend(post for post in profile.get_posts() if not post.is_video)
   
    for post in posts_to_download:
        L.download_post(post, target=result_folder)
    
    

def print_media_count(profile):
    total_media = profile.mediacount
    total_photos = sum(1 for post in profile.get_posts() if not post.is_video)
    total_videos = sum(1 for post in profile.get_posts() if post.is_video)

    print(f"\033[36m║ {total_media} Media @{target_username} {total_photos} Photo(s) {total_videos} Video(s)\033[0m")

def deleting_txt(direktori_insta='result_insta'):
    for folder_name in os.listdir(direktori_insta):
        folder_path = os.path.join(direktori_insta, folder_name)
        
        if os.path.isdir(folder_path):            
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        try:
                            os.remove(file_path)
                        except Exception as e:
                            print(f"Eror Deleting {file}: {e}")

banner = """
\033[35m
╔═══ Z3R0S3S ══════════════════╗
║ Mass Downloader Instagram  V1║
╚═══════════════ EST 2024 ═════╝\033[0m"""
print(banner)

try:
    while True:
        print("\033[36m\n╔═══════════════════════════════\033[0m")
        target_username = input("\033[36m║ Instagram Username: \033[0m")

        try:
            profile = Profile.from_username(L.context, target_username)
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"\033[31m║ User {target_username} not found.\033[0m")
            continue

        print_media_count(profile)

        print("\033[36m║ 1. Fetch To Videos Only")
        print("\033[36m║ 2. Fetch To Photo Only")
        print("\033[36m║ 3. Fetch To Story Only")
        print("\033[36m║ 4. Fetch To Photo/Videos tagged")
        print("\033[36m║ 5. Fetch All")

        option = int(input("\033[36m║ Enter option: \033[0m"))

        print("\033[33m║ Starting Grabbing Content...\033[0m")
        insta_bulk_download(target_username, option)
        print("\033[32m║ All content has been successfully downloaded.\033[0m")
        deleting_txt()
except KeyboardInterrupt:
    print("\033[31m║ Engine Stopped!!!\033[0m")
