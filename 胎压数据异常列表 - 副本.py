import os,sys,time
os.chdir("C:/TPMSlog")
log_list=os.listdir("C:/TPMSlog")
if os.path.isfile("C:/tpms_wrong/tpms_data_wrong.fuck"):
    os.remove("C:/tpms_wrong/tpms_data_wrong.fuck")
elif not os.path.exists("C:/tpms_wrong"):
    os.makedirs("C:\\tpms_wrong")
DIC_kv={}
DIC_list={}
x=0
#file time
for a in range(0,len(log_list)):
    file_time=os.stat(log_list[a]).st_mtime  
    DIC_key=log_list[a]
    DIC_value=file_time
    DIC_kv[DIC_key]=DIC_value
#print(DIC_kv["LGWEF4A53HH509896.log"])  
#user's input str 



DIC_list=sorted(DIC_kv.items(),key=lambda d:d[1],reverse=True)
for i in range(0,len(DIC_list)):
    #print "loading",i,"of",len(DIC_list)
    filename=DIC_list[i][0]
    filetime=DIC_list[i][1]
    filetime=time.localtime(filetime)
    human_time=time.strftime('%Y-%m-%d %H:%M:%S '+'星期%w ',filetime)
   
    file_open=open(filename,"r").read()
    file_split_digital=[]
    file_split_digital=file_open.split("=",2)[1]
    digital_1=file_split_digital[0:8]
    digital_2=file_split_digital[8:16]
    digital_3=file_split_digital[16:24]
    digital_4=file_split_digital[24:32]


    
    if digital_1=="00000000" or digital_2=="00000000" or digital_3=="00000000" or digital_4=="00000000":
        x=x+1
        y=str(x)
        error_open=open("C:/tpms_wrong/tpms_data_wrong.fuck","a")
        f=filename+"\n"
        t=human_time+"\n"
        number="<("+y+")>"+"\n"
        v="\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"+"\n"
        error_open.writelines(number)
        error_open.writelines(t)
        error_open.writelines(v)
        error_open.writelines(f)
        error_open.writelines(v)
        error_open.writelines(file_open+"\n")
        error_open.writelines("\n")
        error_open.close()

def usrinput(usr_input):
    if usr_input.isdigit():
        if len(usr_input)!=8:
            usrinput(usr_input=str(input("check times example:20170817>>>")))
        else:
            input_year=usr_input[0:4]
            input_month=usr_input[4:6]
            input_day=usr_input[6:8]

            
            input_time_exchange=input_year+"-"+input_month+"-"+input_day+" "+"00:00:00"
            
            usr_select_open=open("C:/tpms_wrong/tpms_data_wrong.fuck","r").read()
            usr_find_str=usr_select_open.find(input_time_exchange)

            if usr_find_str=="-1":
                print("there is not time")
                usrinput(usr_input=str(input("check times example:20170817>>>")))
            else:
                list_content=usr_select_open[0:(usr_find_str+4)]
                content_file=open("C:/tpms_wrong/tpms_data_select.select","w+")
                content_file.writelines(list_content)
            #输入时间转换为时间戳
    else:
        usrinput(usr_input=str(input("check times example:20170817>>>")))

        
usr_input=str(input("check times example:20170817>>>"))
usrinput(usr_input)



print ("amount of abnormal_data",x)
os.system("notepad C:/tpms_wrong/tpms_data_wrong.fuck")
