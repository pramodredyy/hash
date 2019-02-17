
import hashlib

a=input("enter the word:")
c=bytes(a,'utf-8')
hash_obj=hashlib.sha224(c)    #can use sha1,sha512,sha256,sha512 in place of sha1 we can use md5
b=hash_obj.hexdigest()
print(b)
