try:
    from moviepy.editor import VideoFileClip
    print("MoviePy successfully imported!")
except Exception as e:
    print(f"Error importing MoviePy: {str(e)}") 