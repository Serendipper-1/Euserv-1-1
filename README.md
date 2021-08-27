# Euserv续期脚本——selenium版本
这是鄙人学习python自动化测试的时候突发奇想,只是单纯的测试一下euserv的续期测试哈哈哈😁还真可以续期,本人测试过了,初步脚本已经写出来了,脚本会有所改进,还是有不少可以优化的地方的.请大佬指教指教,好菜ing✨

------

### 脚本使用

##### 一键安装脚本(主要是selenium等环境的搭建和测试环境,执行一次就可,主要是测试使用环境是否能够运行)

> 目前只有centos版,其他待更新...........

```shell
wget -N --no-check-certificate https://cdn.jsdelivr.net/gh/hngyedu/EUserv_extend@1.1/Euse1.sh && chmod +x Euse1.sh && ./Euse1.sh
```

> 脚本分为windows版和linux无界面版

- euserv_test_linux.py
- euserv_test_win.py

这两个文件主要区别就是linux无界面,win是有界面的测试,vps可以使用宝塔或crontab计划任务运行一下命令:

```python
python3 euserv_test_linux.py
```

根据自己的小鸡到期时间进行配置

![QQ截图20210826120602.png](https://gitee.com/liujie2021/imgre/raw/master/QQ截图20210826120602.png)

![QQ截图20210826120608](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120608.png)

![QQ截图20210826120618](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120618.png)

![QQ截图20210826120625](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120625.png)

![QQ截图20210826120715](https://gitee.com/liujie2021/imgre/raw/master/QQ%E6%88%AA%E5%9B%BE20210826120715.png)

### 说明

如何安装python3、selenium、Chrome、chromedriver等遇到相关问题请提[issues](https://github.com/huanngy/EUserv_extend/issues)
