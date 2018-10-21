from django.utils.deprecation import MiddlewareMixin


class MyCrosMiddleware(MiddlewareMixin):

    def process_response(self,request,response):
        """
        :param request:
        :param response:
        :return:
        """
        # 为返回的每一个响应添加响应头，解除浏览器同源策略导致的跨域问题
        response['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Methods"] = "PUT,DELETE,POST"
            response["Access-Control-Allow-Headers"] = "Content-Type"
        return response