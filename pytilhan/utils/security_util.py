import hashlib


# 암호화 처리
def sha256_encoding(txt):
    return hashlib.sha256(txt.encode('utf-8')).hexdigest();


# sha256 암호화 텍스트 비고
def compare_sha256(sha256_txt, txt):
    if sha256_txt == sha256_encoding(txt):
        return True
    else:
        return False
