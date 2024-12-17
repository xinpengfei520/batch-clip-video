# 批量图片视频剪辑工具

一个基于Python的自动化视频剪辑工具，可以将多张图片批量转换为带有缩放动画效果和背景音乐的视频。

## 功能特性

- 批量处理图片生成视频
- 每10张图片自动生成一个视频文件
- 支持图片缩放动画效果（2秒内从100%放大到120%）
- 自动添加背景音乐
- 支持多种图片格式（PNG、JPG、JPEG）
- 自动裁剪背景音乐以匹配视频长度

## 环境要求

- Python 3.9+
- moviepy
- Pillow 9.5.0（注意：必须使用此版本，更高版本可能导致兼容性问题）
- numpy
- imageio-ffmpeg

## 安装步骤

1. 创建并激活虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate
```

2. 安装依赖：

```bash
pip uninstall
```
