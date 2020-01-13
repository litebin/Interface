# stonenumber = 0
#
# if stonenumber >= 4:
#     print('获得了打败灭霸的力量，反杀稳了')
#
# elif stonenumber >= 1 or stonenumber <= 3:
#     print('可以全员出动，殊死一搏')
#
# else:
#     print('没办法了，只能尝试呼叫惊奇队长')
# money = 80
#
# if money >= 500:
#     print('欢迎进入史塔克穷人帮前三名')
#
# elif money >= 100 or money <= 300:
#     print('请找弗瑞队长加薪')
# elif money >= 500 or money <= 1000:
#     print('祝贺您至少可以温饱了。')
# elif money > 1000:
#     print('经济危机都难不倒您！')
# elif money > 1000 or money < 20000:
#     print('您快比钢铁侠有钱了！')
# elif money > 20000:
#     print('您是不是来自于瓦坎达国？')
# print('程序结束')


# print('请在以下四个选项【格兰芬多；斯莱特林；拉文克劳；赫奇帕奇】中，输入你想去的学院名字:')
# name = input('请输入你的名字：')
# if name == '格兰芬多':
#     print(name)
# elif name == '斯莱特林':
#     print(name)
# elif name == '拉文克劳':
#     print(name)
# else:
#     print(name)


helps = input('您好，欢迎来到古灵阁，请问您需要帮助吗')
if helps == '需要':
    hahaha = int(input('请问您需要什么帮助呢？'))
    if hahaha == 1:
        print('小精灵会推荐你去存取款窗')
    elif hahaha == 2:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        count = int(input('请问您需要兑换多少金加隆呢？'))
        print('好的，我知道了，您需要兑换' + 'count'+ '金加隆。')
        print('那么，您需要付给我' + str(count * 51.3) + '人民币')
    else:
        print('小精灵会推荐你去咨询窗口')
elif helps == '不需要':
    print('好的，再见！')


# age = 59
#
# choice = input('请你猜一下斯内普教授的年龄：')
#
# if choice == age:
#     print('猜对惹～你好厉害！ ヽ✿゜▽゜)ノ～～～')
#
# elif choice < age:
#     print('斯内普的提示：你猜小了（；´д｀）ゞ。。。。')
#
# else:
#     print('斯内普的提示：乃猜大了惹(＞﹏＜)～～')
