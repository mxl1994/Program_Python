# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse
from app01 import models
from django.db.models import Avg,Max,Min,Count,Sum   # 聚合查询
from django.db.models import F,Q
import sys
reload(sys)
sys.setdefaultencoding("utf8")
def add_book(request):
    # book = models.Sites(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    book = models.app01_book.objects.create(title="如来神掌",price=300,publish="菜鸟出版社",pub_date="2010-10-10")
    print(book,type(book))
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")

def get_book(request):

    # book = models.app01_book.objects.all()
    # for i in book:
    #     print(i.title)

    # filter查询符合条件的数据
    # books = models.app01_book.objects.filter(pk=5)
    # print(books)
    # print("//////////////////////////////////////")
    # books = models.app01_book.objects.filter(publish='菜鸟出版社', price=300)
    # print(books, type(books))  # QuerySet类型，类似于list。

    # exclude查询不符合条件的数据
    # books = models.app01_book.objects.exclude(pk=5)
    # print(books)
    # print("//////////////////////////////////////")
    # books = models.app01_book.objects.exclude(publish='菜鸟出版社', price=300)
    # print(books, type(books))  # QuerySet类型，类似于list。


    # get() 方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误。
    # books = models.app01_book.objects.get(pk=5)
    # books = models.app01_book.objects.get(pk=18)  # 报错，没有符合条件的对象
    # books = models.app01_book.objects.get(price=200)  # 报错，符合条件的对象超过一个
    # print(books, type(books))  # 模型类的对象

    # order_by() 方法用于对查询结果进行排序
    # books = models.app01_book.objects.order_by("price")  # 查询所有，按照价格升序排列
    # books = models.app01_book.objects.order_by("-price")  # 查询所有，按照价格降序排列

    # reverse() 方法用于对查询结果进行反转
    # 按照价格升序排列：降序再反转
    # books = models.app01_book.objects.order_by("-price").reverse()


    # count() 方法用于查询数据的数量返回的数据是整数。
    # books = models.app01_book.objects.count()
    # books = models.app01_book.objects.filter(price=200).count()

    # first()方法返回第一条数据,返回的数据是模型类的对象,也可以用索引下标[0]。
    # last()方法返回最后一条数据,返回的数据是模型类的对象,不能用索引下标[-1]，ORM没有逆序索引。
    # books = models.app01_book.objects.first()
    # books = models.app01_book.objects.last()


    # exists() 方法用于判断查询的结果 QuerySet 列表里是否有数据。返回的数据类型是布尔，有为 true，没有为 false。
    # 注意：判断的数据类型只能为 QuerySet 类型数据，不能为整型和模型类的对象。
    # books = models.app01_book.objects.exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
    # books = models.app01_book.objects.count().exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
    # books = models.app01_book.objects.first().exists()


    # values() 方法用于查询部分字段的数据。
    # 返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个可迭代的字典序列，字典里的键是字段，值是数据。
    # books = models.app01_book.objects.values('pk','price')
    # print(books[0]["price"], type(books))   # 得到的是第一条记录的price字段的数据

    # values_list() 方法用于查询部分字段的数据。返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个个元组，元组里放的是查询字段对应的数据。
    # books = models.app01_book.objects.values_list("price","publish")
    # print(books)
    # print(books[0][0],type(books))

    # distinct() 方法用于对数据进行去重。返回的是 QuerySet 类型数据。distinct() 一般是联合 values 或者 values_list 使用。
    # books = models.app01_book.objects.values_list("publish").distinct()
    # books = models.app01_book.objects.distinct()    # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。

    # filter() 方法基于双下划线的模糊查询（exclude 同理）。注意：filter 中运算符号只能使用等于号 = ，不能使用大于号 > ，小于号 < ，等等其他符号。__in 用于读取区间，= 号后面为列表 。
    # books = models.app01_book.objects.filter(price__in=[200,260]).count()
    # books = models.app01_book.objects.filter(price__gt=260).count()
    # books = models.app01_book.objects.filter(price__gte=300).count()
    # books = models.app01_book.objects.filter(price__lt=300).count() # __lt 小于，=号后面为数字。
    # books = models.app01_book.objects.filter(price__lte=300).count()    # __lte 小于等于，= 号后面为数字。
    # books = models.app01_book.objects.filter(price__range=[200,300]).count()  # __range 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表。
    # books = models.app01_book.objects.filter(publish__contains="菜鸟").count()  # __contains 包含，= 号后面为字符串。
    # books = models.app01_book.objects.filter(publish__icontains="python").count()  # __icontains 不区分大小写的包含，= 号后面为字符串。
    # books = models.app01_book.objects.filter(publish__startswith="菜鸟")  # __startswith 以指定字符开头，= 号后面为字符串。
    # books = models.app01_book.objects.filter(publish__endswith="菜鸟")  # __endswith 以指定字符结尾，= 号后面为字符串。
    # books = models.app01_book.objects.filter(publish__endswith="社")  # __endswith 以指定字符结尾，= 号后面为字符串。
    # books = models.app01_book.objects.filter(pub_date__year=2010).count()   # __year 是 DateField 数据类型的年份，= 号后面为数字。
    # books = models.app01_book.objects.filter(pub_date__month=9).count()  # __month 是DateField 数据类型的月份，= 号后面为数字。
    books = models.app01_book.objects.filter(pub_date__day=9).count()  # __day 是DateField 数据类型的天数，= 号后面为数字。
    return HttpResponse(books)

def delete_book(request):
    # 方式一：使用模型类的 对象.delete()。
    # 返回值：元组，第一个元素为受影响的行数。
    # books = models.app01_book.objects.filter(pk=3).first().delete()
    # return HttpResponse(books)

    # 方式二：使用 QuerySet 类型数据.delete()(推荐)
    # 返回值：元组，第一个元素为受影响的行数。
    books = models.app01_book.objects.filter(pk__in=[1,2]).delete()
    return HttpResponse(books)

    #     a. Django 删除数据时，会模仿 SQL约束 ON DELETE CASCADE 的行为，也就是删除一个对象时也会删除与它相关联的外键对象。
    #     b. delete() 方法是 QuerySet 数据类型的方法，但并不适用于 Manager 本身。也就是想要删除所有数据，必须写all。

def update_book(request):
    # 方式一：
    # 模型类的对象.属性 = 更改的属性值
    # 模型类的对象.save()
    # 返回值：编辑的模型类的对象。
    # books = models.app01_book.objects.filter(pk=4).first()
    # books.price = 400
    # books.save()
    # return HttpResponse(books)

    # 方式二：QuerySet 类型数据.update(字段名=更改的数据)（推荐）
    # 返回值：整数，受影响的行数
    books = models.app01_book.objects.filter(pk__in=[5,6]).update(price=888)
    return HttpResponse(books)


def add_book_double(request):

    # 方式一：
    # pub_obj = models.Publish.objects.filter(pk=1).first()
    # # #  给书籍的出版社属性publish传出版社对象
    # book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    # print (book,type(book))
    # return HttpResponse(book)

    # 方式二：
    #一对多中，设置外键属性的类(多的表)中，MySQL 中显示的字段名是:外键属性名_id。
    # 返回值的数据类型是对象，书籍对象。
    #  获取出版社对象
    # pub_obj = models.Publish.objects.filter(pk=1).first()
    # #  获取出版社对象的id
    # pk = pub_obj.pk
    # #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    # book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
    # print (book, type(book))
    # return HttpResponse(book)

    # 多对多(ManyToManyField)：在第三张关系表中新增数据
    #  方式一：获取作者对象
    # chong = models.Author.objects.filter(name="令狐冲").first()
    # ying = models.Author.objects.filter(name="任盈盈").first()
    # #  获取书籍对象
    # book = models.Book.objects.filter(title="菜鸟教程").first()
    # #  给书籍对象的 authors 属性用 add 方法传作者对象
    # book.authors.add(chong, ying)
    # return HttpResponse(book)

    # 方式二：传对象id形式，无返回值。
    # chong = models.Author.objects.filter(name="令狐冲").first()
    # pk = chong.pk
    # book = models.Book.objects.filter(title="冲灵剑法").first()
    # book.authors.add(pk)
    # return HttpResponse(book)




    # 关联管理器（对象调用）
    # book_obj = models.Book.objects.get(id=1)
    # author_list = models.Author.objects.filter(id__gt=2)
    # book_obj.authors.add(*author_list)
    # return HttpResponse("ok")


    # 一对多
    # ying = models.Author.objects.filter(name="任盈盈").first()
    # book = models.Book.objects.filter(title="冲灵剑法").first()
    # ying.book_set.add(book)
    # return HttpResponse("ok")


    # create()创建一个新的对象，并同时将它添加到关联对象集之中。
    # 返回新创建的对象。
    # pub = models.Publish.objects.filter(name="明教出版社").first()
    # wo = models.Author.objects.filter(name="任我行").first()
    # book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)
    # print(book, type(book))
    # return HttpResponse("ok")


    # remove()：从关联对象集中移除执行的模型对象。
    # 对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在，无返回值。
    # author_obj = models.Author.objects.get(id=1)
    # book_obj = models.Book.objects.get(id=2)
    # author_obj.book_set.remove(book_obj)
    # return HttpResponse("ok")


    # clear()：从关联对象集中移除一切对象，删除关联，不会删除对象。
    #
    # 对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在。
    # 无返回值。
    #  清空独孤九剑关联的所有作者
    book = models.Book.objects.filter(title="菜鸟教程").first()
    book.authors.clear()
    return HttpResponse("ok")

def get_book_double(request):
    '''
    查询
    :param request:
    :return:
    '''
    '''
    ORM查找
    正向查找：属性
    反向：小写类名_set
    '''
    # 一对多--正向
    # book = models.Book.objects.filter(pk=1).first()
    # res = book.publish.city
    # print(res,type(res))
    # return HttpResponse("ok")

    # 一对多--反向
    # pub = models.Publish.objects.filter(name="明教出版社").first()
    # res = pub.book_set.all()
    # for i in res:
    #     print(i.title)
    # return HttpResponse("ok")

    # 一对一：正向
    # # 查询令狐冲的电话；正向：对象.属性 (author.au_detail) 可以跳转到关联的表(作者详情表)
    # author = models.Author.objects.filter(name="令狐冲").first()
    # res = author.au_detail.tel
    # print(res,type(res))
    # return HttpResponse(res)

    # 一对一的反向，用对象.小写类名即可，不用加_set。
    # 反向：对象.小写类名(addr.author)可以跳转到关联的表(作者表)。
    # addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
    # res = addr.author.name
    # print (res,type(res))
    # return HttpResponse(res)

    # 多对多
    # 菜鸟教程所有作者的名字以及手机号（正向）
    # 正向：对象.属性(book.authors)可以跳转到关联的表(作者表)。
    # 作者表里没有作者电话，因此再次通过对象.属性(i.au_detail)跳转到关联的表（作者详情表）。
    # book = models.Book.objects.filter(title="菜鸟教程").first()
    # res = book.authors.all()
    # for i in res:
    #     print(i.name,i.au_detail.tel)
    # return HttpResponse("ok")

    # 反向
    # author = models.Author.objects.filter(name="任我行").first()
    # res = author.book_set.all()
    # for i in res:
    #     print(i.title)
    # return  HttpResponse("OK")


    # 基于双下划线的跨表查询
    # 正向：属性名称__跨表的属性名称
    # 反向：小写类名__跨表的属性名称

    # 一对多
    # 查询菜鸟出版社出版过的所有书籍的名字与价格
    # res = models.Book.objects.filter(publish__name="菜鸟出版社").values_list("title", "price")
    # print(res,type(res))
    # return HttpResponse("ok")

    # 反向：通过小写类名__跨表的属性名称（book__title，book__price） 跨表获取数据。
    # res = models.Publish.objects.filter(name="华山出版社").values_list("book__title", "book__price")
    # return HttpResponse(res)

    # 多对多
    # 查询任我行出过的所有书籍的名字。
    # 正向：通过属性名称__跨表的属性名称(authors__name)跨表获取数据：
    # res = models.Book.objects.filter(authors__name="任我行").values_list("title")
    # return HttpResponse(res)

    # 反向：通过 小写类名__跨表的属性名称（book__title） 跨表获取数据：
    # res = models.Author.objects.filter(name="任我行").values_list("book__title")
    # return HttpResponse(res)


    # 一对一

    # 查询任我行的手机号。
    # 正向：通过属性名称__跨表的属性名称(au_detail__tel)跨表获取数据。
    res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
    return HttpResponse(res)

    # 反向：通过小写类名__跨表的属性名称（author__name） 跨表获取数据。
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")
    return HttpResponse(res)


def aggregates(request):
    # res = models.Book.objects.aggregate(aa=Avg('price'))    # aa为字典的键起别名，键的名称默认是（属性名称加上__聚合函数名）
    # res = models.Book.objects.aggregate(Count("id"),Max("price"),Min('price'))

    # res = models.Publish.objects.values("name").annotate(in_price = Min("book__price")) #分组查询（annotate），返回QuerySet数据类型
    # res = models.Book.objects.annotate(c=Count("authors__name")).values("title", "c")   #annotate、values所在位置不同，含义也不同
    # res = models.Book.objects.filter(title__startswith="菜").annotate(c=Count("authors__name")).values("title", "c")
    # res = models.Book.objects.annotate(c=Count("authors__name")).filter(c__gt=0).values("title", "c")
    # res = models.Book.objects.annotate(c=Count("authors__name")).order_by("-c").values("title", "c")
    # res = models.Author.objects.annotate(all=Sum("book__price")).values("name", "all")

    # F() 查询,之前构造的过滤器都只是将字段值与某个常量做比较，如果想要对两个字段的值做比较，就需要用到 F()。用法：F("字段名称")
    # book = models.Emp.objects.filter(salary__gt=F("age")).values("name", "age")
    # res = models.Book.objects.update(price=F("price") + 100)

    # Q() 查询,用法：Q(条件判断)
    # 之前构造的过滤器里的多个条件的关系都是 and，如果需要执行更复杂的查询（例如 or 语句），就可以使用 Q 。
    # Q 对象可以使用 & | ~ （与 或 非）操作符进行组合。优先级从高到低：~ & |。可以混合使用 Q 对象和关键字参数，Q 对象和关键字参数是用"and"拼在一起的（即将逗号看成 and ），
    # 但是 Q 对象必须位于所有关键字参数的前面。
    # res = models.Book.objects.filter(Q(price__gt=350) | Q(title__startswith="菜")).values("title", "price")
    # res = models.Book.objects.filter(Q(title__endswith="菜") | ~Q(Q(pub_date__year=2010) & Q(pub_date__month=10))) # 查询以"菜"结尾或者不是 2010 年 10 月份的书籍:
    res = models.Book.objects.filter(Q(pub_date__year=2004) | Q(pub_date__year=1999), title__contains="菜")
    print(res)

    return HttpResponse(res)
