import os
from nonebot import on_message
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment
import logging

# 自定义回复目录
REPLY_DIR = "qtoa"

# 创建一个事件响应器，用于处理消息
reply = on_message()

@reply.handle()
async def handle_reply(event: Event):
    # 获取用户发送的消息
    user_msg = str(event.get_message()).strip()
    
    # 构建文件路径
    file_path = os.path.join(REPLY_DIR, user_msg)
    
    text_found = False
    image_found = False
    reply_msg = ""
    image = None

    # 首先检查是否有对应的 txt 文件
    if os.path.exists(file_path + ".txt"):
        try:
            with open(file_path + ".txt", "r", encoding="utf-8") as file:
                reply_msg = file.read()
                text_found = True
                logging.info(f"Text file found and read: {file_path}.txt")  # 调试信息
                await reply.send(reply_msg)
        except FileNotFoundError:
            logging.warning(f"Text file not found after being found: {file_path}.txt")  # 调试信息

    # 然后检查是否有对应的图片文件
    for ext in [".jpg", ".png", ".jpeg"]:
        image_path = file_path + ext
        if os.path.exists(image_path):
            logging.info(f"Image file found: {image_path}")  # 调试信息
            # 构造图片消息段
            try:
                abs_image_path = os.path.abspath(image_path)  # 使用绝对路径
                image = MessageSegment.image(f"file:///{abs_image_path}")
                image_found = True
                logging.info(f"Prepared image: {abs_image_path}")  # 调试信息
                await reply.send(image)
                break  # 发送一张图片后停止
            except Exception as e:
                logging.error(f"Failed to prepare image: {e}")

    # 如果既没有找到图片也没有找到文本
    if not text_found and not image_found:
        logging.warning(f"No corresponding text or image found for: {file_path}")

# 在插件加载时检查目录是否存在，如果不存在则创建
def check_reply_dir():
    if not os.path.exists(REPLY_DIR):
        os.makedirs(REPLY_DIR)

check_reply_dir()
