# nonebot-plugin-autotalk
autotalk是一个适用于NoneBot的模板回复插件、。**所有代码均使用GPT构建**

## 阅前提醒
 - **此`README.md`仅适用于最新的`Release`


## 安装教程
 - 前往最新的Release，按需下载`autotalk.py`
 - 将下载的所有 `autotalk.py` 放入你的NoneBot的`plugins`文件夹即可
   
## 使用教程
 - 插件第一次载入时，会在工作区创建一个名为 `qtoa` 的文件夹
 - 打开 `qtoa` 文件夹，在其中放置 `文本（.txt）` 或 `图片(.jpg .jpeg .png)`或`语音（.mp3 .wav）` ，并将文件名改为你想作为的触发词
 - 如果你放置的是文本文件，你需要向其中输入内容。如果是其他则不用管
 - 在对接的平台发送刚添加文件的文件名给Bot
 - 若有多个相同名称不同后缀的文件会一起发送
 - *可以在仓库中下载 `测试.txt` 放入插件创建的`qtoa`文件夹，然后向Bot发送 `测试` 查看插件效果*

## 指令集
请前往仓库的`qtoa`文件夹查看`关键词帮助.txt`

## 目前的不足
 - 不可发送多张图片
 - 无法设置权限规则，默认谁都可以触发命令
 - 更高级的功能请去尝试lgc233大佬的插件：[NoneBot-Plugin-AutoReply](https://github.com/lgc-NB2Dev/nonebot-plugin-autoreply)

## 例图
![例图](eg.png)
