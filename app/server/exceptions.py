class StatusCode:
    HTTP_500 = 500
    HTTP_200 = 200
    
def make_error_content(message) -> dict:
    return {
        "status" : StatusCode.HTTP_500,
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
        self.content = make_error_content("This url needs query parameters content or feeling")
        
class DiaryDoseNotExistExecption(APIException):
    def __init__(self,):
        self.status_code = StatusCode.HTTP_500
        self.content = make_error_content("There is no diary in this date")
        
class DiaryAlreadyExistException(APIException):
    def __init__(self):
        self.status_code = StatusCode.HTTP_500
        self.content = make_error_content("A diary arleady exists in this date")
        
class UnvalidFeelingException(APIException):
    def __init__(self):
        self.status_code = StatusCode.HTTP_500
        self.content = make_error_content("Unvalid feeling. Check the diary's feeling agian.")