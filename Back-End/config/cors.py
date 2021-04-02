from django.http.response import responses



class CorsMiddleware(object):
    def process_response(self, req, resp):
        responses["Access-Control-Allow-Origin"] = "*"
        return responses