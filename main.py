import base64


def decode_b64(base64_code):
    b = b''
    while 1:
        if len(base64_code) > 4:
            b += base64.urlsafe_b64decode(base64_code[:4])
            base64_code = base64_code[4:]
        else:
            if isinstance(base64_code, bytes):
                base64_code += b'==='
            else:
                base64_code += '==='
            b += base64.urlsafe_b64decode(base64_code[:4])
            break
    return str(b, encoding='utf8')
