from pytube import YouTube

def get_stream_for_res(streams, res):
    stream = list(filter(lambda x: x.resolution == res, streams))
    return stream

video_url = input("Enter YouTube Video URL: ").strip()
youtube_obj = YouTube(video_url)

video_res = input(f"Enter YouTube Video Resolution for {youtube_obj.title}: ").strip()
req_stream_obj = get_stream_for_res(youtube_obj.streams, video_res)[0]

req_stream_obj.download()
print(f"YouTube Video {youtube_obj.title} Downloaded With Resolution {video_res}")