from kavenegar import *
from config import rules


def send_sms():
    try:
        api = KavenegarAPI('4B7547385754755949697444724233636C384B667A44677A346E36646E447942746166557579612B6F6E343D')
        params = {
            'sender': '10008663',
            'receptor': '09368688610',
            'message': 'hi'
        }
        response = api.sms_send(params)

        print(str(response))
        print(api.sms_status())

    except APIException as e:
        print(str(e))

    except HTTPException as e:
        print(str(e))
