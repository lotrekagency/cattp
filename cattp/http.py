from django.http import HttpResponse


class HttpCatResponse(HttpResponse):
    
    def __init__(self, status_code=200):
        return super(HttpResponse, self).__init__(
            '<img src="https://http.cat/{0}"/>'.format(status_code),
            status=status_code
        )