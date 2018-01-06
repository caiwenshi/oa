from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
import mysql.connector
import json
#import WXBizDataCrypt
import requests
import base64
import json
from Crypto.Cipher import AES
import datetime
from OA.models import *
from django.forms.models import model_to_dict
"""
config = {
  'user': 'root',
  'password': 'root123',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,
}
DB_NAME = 'meritco_oa_db'
"""

########################################################################################################################
# /oa/api/v1/loginapp
# mobile
# appswd

# https://m2.meritco-group.com/oa/api/v1/loginapp?mobile=15210772908&&appswd=370983199110135315

# { 'data': [{}, {}],
#   'response': '200' }


def loginapp(request):
    r_mobile = request.GET.get('mobile')
    r_appswd = request.GET.get('appswd')

    result = dict()
    try:
        emp = Employee.objects.get(mobile=r_mobile)
        if r_mobile == emp.mobile and r_appswd == emp.id1:
            result['data'] = [model_to_dict(emp)]
            result['response'] = '200'
        else:
            result['response'] = '404'
    except:
        result['data'] = []
        result['response'] = '404'

    return JsonResponse(result, safe=False)


########################################################################################################################
# v1
def login(request):
    appid = 'wxe6b82ce1d6d461fe'
    secret = 'a460a450eda21f5d6ee4e5c577a0669b'
    encryptedData = request.GET.get('encryptedData')
    iv = request.GET.get('iv')
    js_code = request.GET.get('js_code')
    data = {}
    print(js_code)
    print(iv)
    print(encryptedData)
    r = requestWeixinSessionKey(appid, secret, js_code)
    if r.status_code == requests.codes.ok:
        if json.loads(r.text).__contains__('errcode'):
            data = json.loads(r.text)
        else:
            print(r.text)
            open_id = json.loads(r.text)['openid']
            r = decrypt_(json.loads(r.text)['session_key'], encryptedData, iv)
            print(r)
            data = getEmployeeWorkingState(r['purePhoneNumber'], open_id)
    else:
        data["result"] = "获取session key失败!"
        data["errcode"] = "40000"
        print(r.status_code)
    #r = decrypt(session_key, encryptedData, iv)
    #phone = r['purePhoneNumber']
    #print(phone)
    #data = getEmployeeWorkingState(phone)
    #data = {"result": "ok"}
    return JsonResponse(data, safe=False)

def requestWeixinSessionKey(appid, secret, js_code):
    params = {'appid':appid, 'secret':secret, 'js_code':js_code, 'grant_type':'authorization_code'}
    r = requests.get('https://api.weixin.qq.com/sns/jscode2session', params)
    print(r.url)
    print(r.text)
    return r

def decrypt_(sessionKey, encryptedData, iv):
    appId = 'wxe6b82ce1d6d461fe'
    #pc = WXBizDataCrypt(appId, sessionKey)
    return decrypt(appId, sessionKey, encryptedData, iv)


def decrypt(appId, sessionKey, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

        decrypted = json.loads(_unpad(cipher.decrypt(encryptedData).decode('utf-8')))

        if decrypted['watermark']['appid'] != appId:
            raise Exception('Invalid Buffer')

        return decrypted

def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

def process_get_employee_info(request, param1):
     data = {}
     user = get_employee_info_by_id(param1)
     data['user'] = user
     #getEmpProjectInfo(user['emp_id'])
     projects = []
     if user:
         projects = getEmpProjectInfo(user['emp_id'])
     data['projects']=projects
     return JsonResponse(json.dumps(data),safe=False)
   
def get_employee_info_by_id( param1):
    #try: 
        cnx = mysql.connector.connect(user='root',password='root123',database='meritco_oa_db')
        cursor = cnx.cursor()
        #query = "SELECT * FROM employees WHERE emp_id='%s'" %param1
        cursor.execute("SELECT * FROM OA_Employees WHERE emp_id=%s", (param1,))
        #data = cnx.get_row()
        #print(param1)
        result = {}
        for (row) in cursor:
            result['emp_id'] = row[0]
            result['working_state'] = row[1]
            result['name'] = row[2]
            result['gender'] = row[3]
            result['mbti'] = row[4]
            result['birthday'] = row[5]
            result['mobile'] = row[6]
            education = row[8]
            result['hire_date'] = row[7]
            if education is None:
                education="{\"edu experience\":{}}"
            result['education'] = json.loads(education)
            work_exp = row[9]
            if work_exp is None:
                work_exp="{\"work_exp\":{}}"
            result['work_exp'] = json.loads(work_exp)
            result['tenure'] = row[10]
            result['recruited'] = row[11]
            promotion = row[12]
            if promotion is None:
                promotion="{\"promotion\":{}}"
            result['promotion'] = json.loads(promotion)
            result['about'] = row[13]
            result['professional_aspirations'] = row[14]
            result['user_guide'] = row[15]
            result['favorites'] = row[16]
            result['training_sessions'] = row[17]
            result['name_cn'] = row[18]
            result['id1'] = row[19]
            result['id2'] = row[20]
            result['join_date'] = row[21]
            result['level'] = row[22]
            result['loc'] = row[23]
            result['module'] = row[24]
            result['ra_ten'] = row[25]
            result['a_ten'] = row[26]
            result['sa_ten'] = row[27]
            result['asc_w_ten'] = row[28]
            result['asc_ten'] = row[29]
            result['login_mobile'] = row[30]
            #result['openid'] = row[31]
        cursor.close()
        cnx.close()  
        return result
    #except:
       # print 'MySQL connect fail....'
    #else:

def get_employee_info_by_name( param1):
    #try: 
        cnx = mysql.connector.connect(user='root', password='root123', database='meritco_oa_db')
        cursor = cnx.cursor()
        #query = "SELECT * FROM employees WHERE emp_id='%s'" %param1
        cursor.execute("SELECT * FROM OA_Employees WHERE name=%s", (param1,))
        #data = cnx.get_row()
        #print(param1)
        result = {}
        for (row) in cursor:
            result['emp_id'] = row[0]
            result['working_state'] = row[1]
            result['name'] = row[2]
            result['gender'] = row[3]
            result['mbti'] = row[4]
            result['birthday'] = row[5]
            result['mobile'] = row[6]
            education = row[8]
            result['hire_date'] = row[7]
            if education is None:
                education="{\"edu experience\":{}}"
            result['education'] = json.loads(education)
            work_exp = row[9]
            if work_exp is None:
                work_exp="{\"work_exp\":{}}"
            result['work_exp'] = json.loads(work_exp)
            result['tenure'] = row[10]
            result['recruited'] = row[11]
            promotion = row[12]
            if promotion is None:
                promotion="{\"promotion\":{}}"
            result['promotion'] = json.loads(promotion)
            result['about'] = row[13]
            result['professional_aspirations'] = row[14]
            result['user_guide'] = row[15]
            result['favorites'] = row[16]
            result['training_sessions'] = row[17]
            result['name_cn'] = row[18]
            result['id1'] = row[19]
            result['id2'] = row[20]
            result['join_date'] = row[21]
            result['level'] = row[22]
            result['loc'] = row[23]
            result['module'] = row[24]
            result['ra_ten'] = row[25]
            result['a_ten'] = row[26]
            result['sa_ten'] = row[27]
            result['asc_w_ten'] = row[28]
            result['asc_ten'] = row[29]
            result['login_mobile'] = row[30]
            #result['openid'] = row[31]
        cursor.close()
        cnx.close()  
        return result
    #except:
       # print 'MySQL connect fail....'
    #else:



def process_get_project_info(request, param):
    result ={}
    obj = Projects.objects.get(id=param)
    obj.__dict__.pop("_state")
    #result.append(obj.__dict__)
    data = {}
    users = []
    data['project'] = obj.__dict__
    data['users'] = {}
    team = obj.__dict__['team']
    emp_pros = Employees_Projects.objects.filter(pro_id=param)
    for p in emp_pros:
        obj = get_employee_info_by_id(p.emp_id)
        if not obj:
            #obj.__dict__.pop("_state")
            obj = "{\"emp_id\":\"" + p.emp_id + "\", \"name\":\"" + p.emp_name + "\", \"working_state\":\"leave\"}"
            obj = json.loads(obj)
        users.append(obj)
    #if team == '-' or team is None:
    #    print("No team for project")
    #else:
    #    strs = {}
    #    s = team.find(",")
    #    if s:
    #        strs = team.split(",")
    #    else:
    #        strs={team}
    #    for per in strs:
    #        r = get_employee_info_by_name(per.strip())
    #        users.append(r)
    #print(result)
    data['users']=users
    return JsonResponse(json.dumps(data),safe=False)

def getEmployeeWorkingState(param, open_id):
    #param="18018683251"
    cnx = mysql.connector.connect(user='root',password='root123',database='meritco_oa_db')
    cursor = cnx.cursor()
    cursor.execute("SELECT emp_id, working_state FROM OA_Employees WHERE mobile=%s", (param,))
    result={}
    result["result"]="ok"
    result["user"]={}
    emp_id = ""
    for (row) in cursor:
        print(row)
        emp_id=row[0]
        #result["user"]["emp_id"] = row[0]
        #result["user"]["working_state"] = row[1]
    cursor.close()
    cnx.close()
    print(result)
    userinfo = get_employee_info_by_id(emp_id) 
    userinfo["openid"]=open_id
    result["user"]=userinfo
    return json.dumps(result)

def getEmpPrjojectId(param1):
    cnx = mysql.connector.connect(user='root',password='root123',database='meritco_oa_db')
    cursor = cnx.cursor()
    cursor.execute("SELECT pro_id FROM OA_Employees_Projects WHERE emp_id=%s", (param1,))
    result=[]
    for (pro_id) in cursor:
        result.append(pro_id)
    cursor.close()
    cnx.close()
    return result

""" 根据emp_id获取people关联的项目信息"""
def getEmpProjectInfo(param):
    #cnx = mysql.connector.connect(user='root',password='root123',database='meritco_oa_db')
    #cursor = cnx.cursor()
    #cursor.execute("SELECT * FROM projects WHERE pro_id=%s", (param1,))
    #for row in cursor:
        
    #cursor.close()
    #cnx.close()
    result =[]
    emp_pros = Employees_Projects.objects.filter(emp_id=param)
    for p in emp_pros:
        obj = Projects.objects.get(id=p.pro_id)
        obj.__dict__.pop("_state")
        result.append(obj.__dict__)
    #result.sort(key=lambda x: x["start_date"]) 
    result = date_sort(result)
    print(result)
    return result
    #print(pro_ids)


def date_sort(x):
    ls=list(x)
    #用了冒泡排序来排序，其他方法效果一样
    for j in range(len(ls)-1):
        for i in range(len(ls)-j-1):
            lower=datetime.datetime.strptime(ls[i]['start_date'], '%Y-%m-%d')
            upper=datetime.datetime.strptime(ls[i+1]['start_date'], '%Y-%m-%d')
            if lower<upper:
                ls[i],ls[i+1]=ls[i+1],ls[i]
    return ls
