from mail_sender import MailSender, SendMailRequest, SendMailResponse
from user import User

class HttpClient:

    def post(self, base_url : str, request : SendMailRequest):

        if not isinstance(request, SendMailRequest) :
            raise ValueError(f"Invalid request: {request} is of type {type(request)} but should be of type SendMailRequest")

        if '@' not in request.recipient:
            raise ValueError(f"Invalid recipient: {request.recipient}, recipient is not a valid email")
        
        response = SendMailResponse(code=503, message=request.body) # message=request.body
        return response


def test_send_v1():
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    http_client = HttpClient()
    mail_sender = MailSender(http_client)

    
    user = User("Alice", "alice@gmail.com")
    message = "Hello!"
    
    actual = mail_sender.send_v1(user, message)

    expected = SendMailResponse(503, "New notification")

    assert actual == expected, f'Expected {expected} but got {actual}'
    
    

def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2

    http_client = HttpClient()
    mail_sender = MailSender(http_client)

    user = User("Alice", "alice@gmail.com")
    message = "Hello!"

    actual = mail_sender.send_v2(user, message)

    expected = SendMailResponse(503, message)

    assert actual == expected, f'Expected {expected} but got {actual} instead'

