from django.http import HttpResponse


CATTP_RESPONSE = """
<body style="
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: black;">
    <p style="font-size: 7em;">🐱</p>
    <img src="https://http.cat/{0}"/>
    <p style="font-size: 7em;">🐱</p>
</body>
"""


class HttpCatResponse(HttpResponse):

    def __init__(self, status_code=200):
        super().__init__(
            content=CATTP_RESPONSE.format(status_code),
            status=status_code
        )
