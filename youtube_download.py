from pytube import YouTube
link = input("Enter the link: ")
video = YouTube(link)

print(video.title)


'''
stream = video.streams.get_highest_resolution()
stream.download()
'''