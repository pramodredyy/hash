import hashlib
import time

counter = 1

md5_pass = input("enter the password:")
md5_file = input("enter the word list location:")


try:
    md5_file = open(md5_file,'r')

except:
    print("\n file not found")
    quit()


for password in md5_file:
    hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    start = time.time()
    print("password trying %d----> %s" % (counter, password.strip()))
    counter += 1
    end = time.time()
    t_time = end - start

    if hash_obj == md5_pass:
        print("password found...!!!!  password is: %s" % password )
        print("time taken", t_time, "seconds")
        time.sleep(10)
        break

else:
    print("file not found")