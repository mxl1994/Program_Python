# 1、一行代码实现1到100之和
# print(sum(range(1,101)))
# 2、如何在一个函数内部修改全局变量
# global a

#3、列出5个python的标准库

# os：提供了不少与操作系统相关联的函数
# sys:   通常用于命令行参数
# re:   正则匹配
# math: 数学运算
# datetime:处理日期时间

# 4、字典如何删除键和合并两个字典
    # 删除键：①del d["key"]
    #        ②popitem() 随机删除，返回删除元组，包含key\value ③d.pop("key")
    # 清空字典 clear()
    # 合并字典：update()  eg:d1.update(d2)

# 5、谈下python的GIL
    # 全局解释器锁
    # GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。
    #
    # 多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

# 6、python实现列表去重的方法
    # set()

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
    # *args 接受所有的位置参数（装包），将多个实参保存在元组中
    # **kwargs 接受关键字参数，将参数保存在一个字典中,此类参数只能有一个，并放在所有参数的最后
    # 了解下拆包
# 8、python2和python3的range（100）的区别
    # python2 返回的是列表，python3返回的是迭代器，节约内存，只在调用的时候才会生成

# 9、一句话解释什么样的语言能够用装饰器?
    # 函数可以作为参数传递的语言，可以使用装饰器
# 10、python内建数据类/型有哪些
    # 整型int 字符串str 布尔型bool 列表list 元组tuple 字典dict

# 11、简述面向对象中__new__和__init__区别
#   __new__实例化对象(是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。)
#   __init__初始化对象(是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。)
# 12、简述with方法打开处理文件帮我我们做了什么？
#   with结束后，自动关闭文件(自动执行了finally中的close)
# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# map()函数的第一个参数是函数，第二个参数一般是列表，第三个参数也可以是list,也可以不写
list = [1,2,3,4,5]
def fn(x):
    return x**2
result = map(fn,list)
result = [i for i in result if i > 10]
print result
# 14、python中生成随机整数、随机小数、0—1之间小数方法
# random.randint(a,b)生成a到b之间的整数
# 随机小数：通常利用numpy,通过np.random.randn(5)生成5个随机小数
# 0-1之间小数：random.random(),不带任何参数
# 15、避免转义给字符串加哪个字母表示原始字符串？
# r 表示需要原始字符串，不转义特殊字符
# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
#
# 17、python中断言方法举例
# assert() 断言成功，则程序继续执行；断言失败，则程序报错
# 18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# select distinct name from student
# 19、10个Linux常用命令
#  cd mv cat ls pwd touch rm cp more grep echo tree
# 20、python2和python3区别？列举5个
# 1、python3使用print必须要以小括号包裹打印内容；python2既可以使用小括号的方式，也可以使用一个空格来分隔打印内容
# 2、Python3 range(1,10)返回迭代器节约内存，python2返回列表
# 3、python2中使用ascii编码，python3中使用utf-8编码
# 4、python2 中unicode表示字符串序列，str表示字节序列
#    python3中str表示字符串序列，byte表示字节序列
# 5、python2中为正常显示中文，引入coding声明，python3中不需要
# 6、python2是raw_input()函数，python3中是input()函数

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
# 可变数据类型：list dict；允许变量的值发生变化
# 不可变数据类型：数值型、字符串型string和元组tuple;不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象
#(一个地址)
# 22、s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”
# set去重，去重转成list,利用sort方法排序，reverse = False是从小到大排
# 23、用lambda函数实现两个数相乘
# lambda a,b:a*b
# 24、字典根据键从小到大排序dict={“name”:”zs”,”age”:18,”city”:”深圳”,”tel”:”1362626627”}
# dict={"name":"zs","age":18,"city":"shenzhen","tel":"1362626627"}
# list = sorted(dict.items(),key=lambda i:i[0],reverse=False)
# print (list)
# new_dict ={}
# for i in list:
#     new_dict[i[0]] = i[1]
# print(new_dict)
# 25、利用collections库的Counter方法统计字符串每个单词出现的次数”kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h”
# from collections import Counter
# str = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# res = Counter(str)
# print(res)
# 26、字符串a = “not 404 found 张三 99 深圳”，每个词中间是空格，用正则过滤掉英文和数字，最终输出”张三  深圳”
#import re
# a = "not 404 found 张三 99 深圳"
# list = a.split(" ")
# print(list)
# res = re.findall('\d+|[a-zA-Z]+',a)
# for i in res:
#     if i in list:
#         list.remove(i)
# new_str = " ".join(list)
# print(res)
# print(new_str)
# 27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def fn(a):
#     return a%2==1
# newlst = filter(fn,a)
# print(newlst)
# 28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newlist = [i for i in a if i%2==1]
# print(newlist)
# 29、正则re.complie作用
# 是将正则表达式编译成一个对象，加快速度，并重复使用
# 30、a=（1，）b=(1)，c=(“1”) 分别是什么类型的数据？
# （1，）元组 (1)int (“1”)str

# 31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
# list1 = [1,5,7,9]
# list2 = [2,2,6,8]
# list1.extend(list2)
# print(list1)
# list1.sort(reverse=False)
# print(list1)

# 32、用python删除文件和用linux命令删除文件方法
# python:os.remove(文件名)
# linux:rm 文件名

# 33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
# import datetime
# print(datetime.datetime.now())

# 34、数据库优化查询方法
# 外键、索引、联合查询、选择特定字段等等

# 35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
# pychart、matplotlib

# 36、写一段自定义异常代码
#def fn():
#     try:
#         for i in range(5):
#             if i>2:
#                 raise Exception("数字大于2了")
#     except Exception as ret:
#         print(ret)
# fn()

# 37、正则表达式匹配中，（.*）和（.?）匹配区别？
# (.*) 贪婪模式，将前面符合模式的尽可能多的匹配
# (.*?) 非贪婪模式匹配，会把满足正则的尽可能少匹配

# 38、简述Django的orm
#
# 39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
# a = [[1,2],[3,4],[5,6]]
# print([j for i in a for j in i])

# 40、x=”abc”,y=”def”,z=[“d”,”e”,”f”],分别求出x.join(y)和x.join(z)返回的结果
# x="abc"
# y="def"
# z=["d","e","f"]
# m = x.join(y)
# print(m)
# n = x.join(z)
# print(n)

# 41、举例说明异常模块中try except else finally的相关意义
#try..except..else没有捕获到异常，执行else语句
#try..except..finally不管是否捕获到异常，都执行finally语句
try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，则执行该语句')

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
finally:
    print('不管是否捕获到异常，都执行该语句')

# 42、python中交换两个数值
# a,b = 3,4
# print(a,b)
# a,b = b,a
# print(a,b)
# 43、举例说明zip（）函数用法
#
# 44、a=”张明 98分”，用re.sub，将98替换为100
import re
a="张明 98分"
new_a = re.sub(r"\d+","100",a)
print(new_a)
# 45、写5条常用sql语句
# show databases;
# show tables;
# desc 表名;
# select * from table
# update 表名 set 列名 = '' where id=5
# delete from table where  id =5;

# 46、a=”hello”和b=”你好”编码成bytes类型
    a = b"hello"
    b = "哈哈".encode()
    print(a,b)
    print(type(a),type(b))
# 47、[1,2,3]+[4,5,6]的结果是多少？
#  [1,2,3,4,5,6]
# 48、提高python运行效率的方法
# 1、使用生成器，因为可以节约大量内存
# 2、循环代码优化，避免过多重复代码的执行
# 3、核心模块用Cpython PyPy等，提高效率
# 4、多进程、多线程、协程
# 5、多个if elif 条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

# 49、简述mysql和redis区别
redis:内存型非关系数据库，数据保存在内存中，速度快
mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的io操作，访问速度相对慢
# 50、遇到bug如何处理

# 51、正则匹配，匹配日期2018-03-20
url=’https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462‘

52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

53、写一个单列模式

54、保留两位小数
题目本身只有a=”%.03f”%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）

55、求三个方法打印结果

56、列出常见的状态码和意义

57、分别从前端、后端、数据库阐述web项目的性能优化

58、使用pop和del删除字典中的”name”字段，dic={“name”:”zs”,”age”:18}

59、列出常见MYSQL数据存储引擎

60、计算代码运行结果，zip函数历史文章已经说了，得出[(“a”,1),(“b”,2)，(“c”,3),(“d”,4),(“e”,5)]

61、简述同源策略

62、简述cookie和session的区别

63、简述多线程、多进程

64、简述any()和all()方法

65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常

66、python中copy和deepcopy区别

67、列出几种魔法方法并简要介绍用途

68、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？

69、请将[i for i in range(3)]改成生成器

70、a = “  hehheh  “,去除收尾空格

71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]

72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序

73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小

74、列表嵌套字典的排序，分别根据年龄和姓名排序

75、列表嵌套元组，分别按字母和数字排序

76、列表嵌套列表排序，年龄数字相同怎么办？

77、根据键对字典排序（方法一，zip函数）

78、根据键对字典排序（方法二,不用zip)

79、列表推导式、字典推导式、生成器

80、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用

81、举例说明SQL注入和解决办法

82、s=”info:xiaoZhang 33 shandong”,用正则切分字符串输出[‘info’, ‘xiaoZhang’, ‘33’, ‘shandong’]

83、正则匹配以163.com结尾的邮箱

84、递归求和

85、python字典和json字符串相互转化方法

86、MyISAM 与 InnoDB 区别：

87、统计字符串中某字符出现次数

88、字符串转化大小写

89、用两种方法去空格

90、正则匹配不是以4和7结尾的手机号

91、简述python引用计数机制

92、int(“1.4”),int(1.4)输出结果？

93、列举3条以上PEP8编码规范

94、正则表达式匹配第一个URL

95、正则匹配中文

96、简述乐观锁和悲观锁

97、r、r+、rb、rb+文件打开模式区别

98、Linux命令重定向 > 和 >>

99、正则表达式匹配出 <html><h1>www.itcast.cn</h1></html>

100、python传参数是传值还是传址？


101、求两个列表的交集、差集、并集

102、生成0-100的随机数

103、lambda匿名函数好处

104、常见的网络传输协议

105、单引号、双引号、三引号用法

106、python垃圾回收机制

107、HTTP请求中get和post区别

108、python中读取Excel文件的方法

109、简述多线程、多进程

110、python正则中search和match