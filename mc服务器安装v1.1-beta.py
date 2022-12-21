import os
import time
os.system('color 0a')
print('==============================================')
print('')
print('         星空MC服务器安装脚本')
print('')
print('==============================================')
eula = open("eula.txt", "a")
eula.write("eula=true")
eula.close()
print('Eula协议已释放')
print('支持类型：')
print('1.纯净服')
print('2.模组服')
print('3.插件服')
fwd = input('输入您要安装的服务器类型：')
if fwd == '1':
    print('emmmm,正在开发')
elif fwd == '2':
    print('1.forge')
    print('2.fabric')
    fwd=input("输入您要选择的服务端：")
    if fwd == '1':
        print('版本列表')
        print('1.1.12.2')
        print('2.1.16.5')
        fwd = input("输入您要选择的版本：")
        if fwd == '1':
            print('forge安装包开始下载')
            os.system('curl -# -O https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar --ssl-no-revoke')
            print('forge安装包下载完成')
            print('开始安装')
            os.system('java -jar forge-1.12.2-14.23.5.2860-installer.jar --installServer')
            print('forge进程已结束，程序将在3秒后退出')
        elif fwd == '2':
            print('forge安装包开始下载')
            os.system('curl -# -O https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.5-36.2.39/forge-1.16.5-36.2.39-installer.jar --ssl-no-revoke')
            print('forge安装包下载完成')
            print('开始安装')
            os.system('java -jar forge-1.16.5-36.2.39-installer.jar --installServer')
            print('forge进程已结束，程序将在3秒后退出')
        else :
            print('错误，3秒后退出')
    elif fwd == '2':
        print('fabric需要手动安装')
        print('1.Windows')
        print('2.Linux')
        print('3.Macos')
        fwd = input('请选择您的系统：')
        if fwd == '1':
            print('开始下载fabric安装包')
            os.system('curl -# -O https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.1/fabric-installer-0.11.1.exe --ssl-no-revoke')
            print('fabric安装包下载完成')
            print('开始安装')
            print('请选择服务端，然后点击安装')
            os.system('fabric-installer-0.11.1.exe')
            print('fabric进程已结束，程序将在3秒后退出')
        elif fwd == '2':
            print('开始下载fabric安装包')
            os.system('curl -# -O https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.1/fabric-installer-0.11.1.jar --ssl-no-revoke')
            print('fabric安装包下载完成')
            print('开始安装')
            print('请选择服务端，然后点击安装')
            os.system('java -jar fabric-installer-0.11.1.jar')
            print('fabric进程已结束，程序将在3秒后退出')
        elif fwd == '3':
            print('开始下载fabric安装包')
            os.system('curl -# -O https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.1/fabric-installer-0.11.1.jar --ssl-no-revoke')
            print('fabric安装包下载完成')
            print('开始安装')
            print('请选择服务端，然后点击安装')
            os.system('java -jar fabric-installer-0.11.1.jar')
            print('fabric进程已结束，程序将在3秒后退出')
        else :
            print('错误，3秒后退出')
    else :
        print('错误，3秒后退出')
elif fwd == '3':
    pass
else :
    print('错误，3秒后退出')
time.sleep(3)
exit(0)
