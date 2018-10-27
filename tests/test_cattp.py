from cattp.http import HttpCatResponse, CATTP_RESPONSE


def test_http():
    status_code = 200
    response = HttpCatResponse(status_code)
    assert "https://http.cat/200" in str(response.content)
