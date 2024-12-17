from moviepy.editor import *
import os
from PIL import Image
import numpy as np

# 可以在运行前添加这段代码来验证
from PIL import Image
print(f"PIL version: {Image.__version__}")
print(f"ANTIALIAS available: {hasattr(Image, 'ANTIALIAS')}")

def create_video_from_images(image_dir, audio_path, output_dir="output"):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取所有图片文件并排序
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()
    
    # 每10张图片生成一个视频
    for i in range(0, len(image_files), 10):
        batch_files = image_files[i:i+10]
        clips = []
        
        # 处理每张图片
        for img_file in batch_files:
            img_path = os.path.join(image_dir, img_file)
            # 创建图片剪辑
            clip = ImageClip(img_path).set_duration(2)
            
            # 添加缩放动画
            w, h = clip.size
            def resize_func(t):
                scale = 1 + (0.2 * t/2)  # 在0-2秒内从100%缩放到120%
                new_w = int(w * scale)
                new_h = int(h * scale)
                return (new_w, new_h)
            
            clip = clip.resize(resize_func)
            clips.append(clip)
        
        # 连接所有剪辑
        final_clip = concatenate_videoclips(clips)
        
        # 添加音频
        audio = AudioFileClip(audio_path)
        # 裁剪音频至视频长度
        audio = audio.subclip(0, final_clip.duration)
        final_clip = final_clip.set_audio(audio)
        
        # 生成输出文件名
        output_file = os.path.join(output_dir, f"video_batch_{i//10+1}.mp4")
        
        # 导出视频
        final_clip.write_videofile(output_file, 
                                 fps=24, 
                                 codec='libx264',
                                 audio_codec='aac')
        
        # 清理内存
        final_clip.close()
        audio.close()

# 使用示例
image_dir = "/Users/vancexin/Downloads/24.11航海/演示图"
audio_path = "/Users/vancexin/Downloads/24.11航海/biubiubiu.m4a"

create_video_from_images(image_dir, audio_path)