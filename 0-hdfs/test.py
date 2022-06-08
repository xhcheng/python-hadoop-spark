import pyhdfs
import os

if __name__=="__main__":
    fs=pyhdfs.HdfsClient(hosts="192.168.170.100:50070",user_name="guigu")

    #fs.mkdirs("/test")
    fs.delete("/test")
    file_or_dirs=fs.listdir("/")
    print(file_or_dirs)