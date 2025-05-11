import os
import gdown

# Set your desired output directory
output_dir = "raw_data"
os.makedirs(output_dir, exist_ok=True)

# Download from the folder
folder_url = "https://drive.google.com/drive/folders/1Lwwo05G5fxnasGasdScKv9SFuOeNXOaG?usp=sharing"
gdown.download_folder(folder_url, quiet=False, use_cookies=False)