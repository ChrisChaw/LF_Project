from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from api.utils.serializer import course, degree
from api import models
from rest_framework.response import Response
from api.utils.response import BaseResponse
from django.http import JsonResponse
import json

shopping_car = {}


class DegreeCourse(APIView):
    """
        学位课
    """

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            # a.查看所有学位课并打印学位课名称以及授课老师
            queryset = models.DegreeCourse.objects.all()
            # b.查看所有学位课并打印学位课名称以及学位课的奖学金
            # 见序列化类
            ser = degree.DegreeCourseSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 0
            ret.errors = "数据获取失败"
        return Response(ret.dict)

    def post(self, request, *args, **kwargs):
        response = BaseResponse()
        try:
            data = request.body
            dict_data = json.loads(data)
            pid = dict_data.get("pid", None)
            cid = dict_data.get("cid", None)
            price = dict_data.get("price", None)
            period = dict_data.get("_period", None)
            # 获取价策略对象,当校验出错则会被异常补捉
            models.PricePolicy.objects.get(id=pid,object_id=cid,price=price,valid_period=period)
            if "1" in shopping_car:
                shopping_car["1"].append(
                    {
                        "cid": cid,
                        "pid": pid
                    }
                )
            else:
                shopping_car["1"] = [
                    {
                    "cid":cid,
                    "pid":pid
                    }
                ]
            print(shopping_car)
            # shopping_car.update({
            #     "1":{
            #         {
            #             'pid':pid,
            #             'cid':cid
            #         }
            #     }
            # })
        except Exception as e:
            response.code = 0
            response.errors = "价格策略校验错误"
            print(e)
        return Response(response.dict)


class DegreeCourseDetail(APIView):
    """
        学位课详情
    """

    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            # d 查看id=1的学位课对应的所有模块名称
            queryset = models.DegreeCourse.objects.filter(id=pk)
            ser = degree.DegreeCourseSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 0
            ret.errors = "数据获取失败"
        return Response(ret.dict)

    def put(self, request, pk, *args, **kwargs):
        return HttpResponse("ok")

    def delete(self, request, pk, *args, **kwargs):
        return HttpResponse("ok")


class Course(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("ok")

    def post(self, request, *args, **kwargs):
        return HttpResponse("ok")


class CourseDetail(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        """
        # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

		# f.获取id = 1的专题课，并打印该课程相关的所有常见问题

		# g.获取id = 1的专题课，并打印该课程相关的课程大纲

		# h.获取id = 1的专题课，并打印该课程相关的所有章节
        """
        try:
            queryset = models.Course.objects.filter(id=pk, degree_course__isnull=True)
            ser = course.CourseSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 0
            ret.errors = "数据获取失败"
        return Response(ret.dict)

    def put(self, request, *args, **kwargs):
        return HttpResponse("ok")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("ok")
