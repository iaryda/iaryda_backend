class StatusCode:
    HTTP_500 = 500
    HTTP_200 = 200
    
def make_error_content(error_code,message) -> dict:
    return {
        "status" : error_code,
        "message" : message,
        "data" : []
    }
    
class APIException(Exception):
    status_code : int
    content: dict
        
class TestException(APIException):
    def __init__(self,):
        self.status_code = StatusCode.HTTP_500
        self.content = make_error_content(StatusCode.HTTP_500,"Unallowed Http Method")

class NoQueryException(APIException):
    def __init__(self,):
        self.status_code = StatusCode.HTTP_500
        self.content = make_error_content(StatusCode.HTTP_500,"This url needs query parameters content or feeling")