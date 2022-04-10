# importing the module 
from pytube import YouTube , Playlist
from alive_progress import alive_bar  
# where to save 
SAVE_PATH = "Downloads/" #to_do 
  

def download(link):

    url = Playlist(link)
    
    for video in url.videos:
        print(video.title)
        st = video.streams.get_highest_resolution()
        with alive_bar() as bar:
            st.download(SAVE_PATH)
            bar() 
        print('Video was successfully downloaded!') 

def get_link():
    # link of the video to be downloaded 
    print("Please Enter The URL of the youtube playlist:")
    link = input()  
    return link  

link = get_link()
download(link)