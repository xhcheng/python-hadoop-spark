import pyhdfs
import os

if __name__=="__main__":
    fs=pyhdfs.HdfsClient(hosts="192.168.170.100:50070",user_name="guigu")

    #在HDFS上指定目录下创建一个文件夹，然后查看此文件夹是否存在
    fs.mkdirs("/test")
    file_or_dirs=fs.listdir("/")
    print(file_or_dirs)

    #在HDFS上获取用户的根目录
    home_dir = fs.get_home_directory()
    print(home_dir)

    #获取可用的节点
    active_nodes = fs.get_active_namenode()
    print(active_nodes)

    #在HDFS上创建一个文件，并写入内容：
    all_files = fs.listdir("/")
    print(all_files)
    fs.create("/demo_01.txt", b"hello world", override=True)
    all_files = fs.listdir("/")
    print(all_files)

    #删除文件
    all_files = fs.listdir("/")
    print(all_files)
    fs.delete("/demo_01.txt")
    all_files = fs.listdir("/")
    print(all_files)

    #查看文件是否存在
    print(fs.exists("/demo_01.txt"))
    all_files = fs.listdir("/")
    print(all_files)
    fs.create("/demo_01.txt", b"hello world")
    print(fs.exists("/demo_01.txt"))
    all_files = fs.listdir("/")
    print(all_files)

    #读取文件内容：
    f = fs.open("/demo_01.txt")
    ctx = f.read().decode("utf-8")
    print(ctx)
    f.close()

    #向文件中增加内容
    f = fs.open("/demo_01.txt")
    ctx = f.read().decode("utf-8")
    print(ctx)
    f.close()
    fs.append("/demo_01.txt", b"\nhello hadoop!")
    print("-------------------------")
    f = fs.open("/demo_01.txt")
    ctx = f.read().decode("utf-8")
    print(ctx)
    f.close()

    #查看文件属性
    status = fs.get_file_status("/demo_01.txt")
    print(status)

    #查看当前文件的状态
    status = fs.list_status("/demo_01.txt")
    print(status)

    #list_status 和get_file_status的区别是list_status可以查看路径
    print(fs.listdir("/"))
    fs.rename("/test_01", "/test_02")
    print(fs.listdir("/"))

    #将本地文件拷贝至HDFS
    print(fs.listdir("/"))
    fs.copy_from_local("demo_02.txt", "/demo_02.txt")
    print(fs.listdir("/"))

    #将HDFS上文件拷贝到本地
    print(os.listdir("."))
    fs.copy_to_local("/demo_01.txt", "demo_01.txt")
    print(os.listdir("."))

    #获取路径的总览信息（目录，文件个数等）
    summary = fs.get_content_summary("/")
    print(summary)

    #查看文件的校验和
    check_sum = fs.get_file_checksum("/demo_01.txt")
    print(check_sum)

    #设置文件所有者
    print(fs.get_file_status("/demo_01.txt"))
    fs.set_owner("/demo_01.txt", owner="hdfs")
    print(fs.get_file_status("/demo_01.txt"))

    #设置文件的副本数
    print(fs.get_file_status("/demo_01.txt"))
    fs.set_replication("/demo_01.txt", replication=5)
    print(fs.get_file_status("/demo_01.txt"))

    #设置文件的修改时间和访问时间，修改时间和访问时间均为长整形，指从1970年1月1日开始的milliseconds
    print(fs.get_file_status("/demo_01.txt"))
    fs.set_times("/demo_01.txt", modificationTime=1623756729499, accessTime=1623761641699)
    print(fs.get_file_status("/demo_01.txt"))