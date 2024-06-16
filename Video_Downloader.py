import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube
import instaloader
import os

def download_youtube_video(url, path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(path)
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download YouTube video: {str(e)}")

def download_instagram_post(url, path):
    try:
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        L.download_post(post, target=path)
        messagebox.showinfo("Success", f"Downloaded post from: {post.owner_username}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download Instagram post: {str(e)}")

def choose_directory():
    path = filedialog.askdirectory()
    if path:
        path_var.set(path)

def start_download():
    url = url_entry.get()
    platform = platform_var.get()
    path = path_var.get()
    os.makedirs(path, exist_ok=True)

    if platform == 'YouTube':
        download_youtube_video(url, path)
    elif platform == 'Instagram':
        download_instagram_post(url, path)
    else:
        messagebox.showerror("Error", "Unsupported platform")

# Creating the GUI
root = tk.Tk()
root.title("Video Downloader")

ttk.Label(root, text="URL:").grid(column=0, row=0, padx=10, pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Platform:").grid(column=0, row=1, padx=10, pady=5)
platform_var = tk.StringVar(value='YouTube')
platforms = ['YouTube', 'Instagram']
platform_menu = ttk.Combobox(root, textvariable=platform_var, values=platforms)
platform_menu.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Save to:").grid(column=0, row=2, padx=10, pady=5)
path_var = tk.StringVar(value='./videos')
path_entry = ttk.Entry(root, textvariable=path_var, width=50)
path_entry.grid(column=1, row=2, padx=10, pady=5)

choose_dir_button = ttk.Button(root, text="Browse", command=choose_directory)
choose_dir_button.grid(column=2, row=2, padx=10, pady=5)

download_button = ttk.Button(root, text="Download", command=start_download)
download_button.grid(column=1, row=3, padx=10, pady=10)

root.mainloop()
