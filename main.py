#!/usr/bin/env python3
import os
import pytube
# from sys import platform
# PLATFORM:str = platform.lower()

class YouTube:
    def __init__(self, defaultSavePath:str = "Downloads", fileExtension:str = "mp4") -> None:
        self.defaultSavePath:str = defaultSavePath
        self.fileExtension:str = fileExtension

        if(os.path.isdir(self.defaultSavePath) == False):
            os.mkdir(self.defaultSavePath)
        
    # Downloads a single file
    def download(self, url:str, fileName:str = None, savePath:str = None) -> None:
        if(savePath is None):
            savePath = self.defaultSavePath
        if(not os.path.isdir(savePath)):
            os.mkdir(savePath)
        if(fileName is None):
            fileName = url.split("/")[-1]
        try:
            yt = pytube.YouTube(url)
            yt.streams.filter(progressive=True, file_extension=self.fileExtension).order_by('resolution').desc().first().download(savePath, filename=f"{fileName}.{self.fileExtension}")
        except Exception as e:
            print(e)

    # Downloads multiple file
    # Need path for the list of file links
    def downloadMultiple(self, filePath:str, savePath:str = None) -> None:
        if(savePath is None):
            savePath = self.defaultSavePath
        try:
            if(not os.path.isdir(savePath)):
                os.mkdir(savePath)
        except Exception as e:
            print(e)
        with open(filePath, "r") as f:
            for line in f:
                try:
                    fileName = line.split("=")[0]
                    if(fileName == " " or fileName == "" or fileName == line):
                        fileName = line.split("/")[-1]
                except:
                    fileName = line.split("/")[-1]
                try:
                    url = line.split("=")[1]
                except:
                    url = line
                print(f"Url: {url} \t FileName: {fileName} \t savePath: {savePath}")
                self.download(url, fileName, savePath)

if __name__ == '__main__':
    y = YouTube()
    print("Downloading...")
    y.download("https://youtu.be/dQw4w9WgXcQ")
    # y.downloadMultiple("/tmp/test.txt")