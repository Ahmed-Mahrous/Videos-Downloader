# importing the module 
from pytube import YouTube , Playlist
from alive_progress import alive_bar  
# where to save 
SAVE_PATH = "Downloads/" #to_do 
  

def download(link):

    
    try: 
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(link) 
    except: 
        print("Connection Error") #to handle exception 
    
    # filters out all the files with "mp4" extension 
    mp4files = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    with alive_bar() as bar:
        try: 
            # downloading the video 
            mp4files.download(SAVE_PATH) 
        except: 
            print("Some Error!") 
        bar()    
    print('Video was successfully downloaded!') 
   

def get_link():
    # link of the video to be downloaded 
    print("Please Enter The URL of the youtube video:")
    link = input()  
    return link  

link = get_link()
download(link)