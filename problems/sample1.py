st="This is python program and i am the best means chanda is best"
new_st=st.split()
d={}
for i in new_st:
    d[i.strip()]=0
print(d)
for i,j in d.items():
    cnt=0
    for k in new_st:
        if i.strip()==k.strip():
            cnt+=1
    d[i]=cnt
print(d)
# top
# lsblk
#
# curl -x GET http://10.190.2.1/option
#
# try:
#     pass
# except Exception as e:
#     pass
# finally:
#
# @abstratmethod
# def static_ex(args,args1):
#     pass
#
