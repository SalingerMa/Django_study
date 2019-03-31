# # -*- coding: utf-8 -*-
# # 数据库操作
#
# from django.http import HttpResponse
# from TestModel.models import Test
#
# def testdb(request):
#     tets1 = Test(name='runoob')
#     tets1.save()
#     return HttpResponse("<p>数据添加成功！</p>")
#

# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test


# def testdb(request):
    # # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    # # test1 = Test.objects.get(id=1)
    # # test1.name = 'Google'
    # # test1.save()
    #
    # # 另外一种方式
    # # Test.objects.filter(id=1).update(name='FaceBook')
    #
    # # 修改所有的列
    # Test.objects.all().update(name='Google')
    #
    # return HttpResponse("<p>修改成功</p>")

def testdb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")