import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def make_url(info):
    db=info.get('db')
    driver=info.get('driver')
    user=info.get('username')
    pwd=info.get('pwd')
    host=info.get('host')
    port=info.get('port')
    name=info.get('name')
    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,user,pwd,host,port,name)



class Config():

    DEBUG=False
    SETING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY="MRqu"

class DevelopConfig(Config):
    DEBUG = True
    info={
        'db':'mysql',
        'driver':'pymysql',
        'username':'root',
        'pwd':'0118',
        'host':'localhost',
        'port':'3306',
        'name':'flaskTpp',
    }
    SQLALCHEMY_DATABASE_URI=make_url(info)


envs = {
    "develop": DevelopConfig,
    "defualt": DevelopConfig
}

ADMIN=['Tom','Rose']
FILE_PATH_PRIFIX='App/static/uploads/icon'
UPLOADS_DIR=os.path.join(BASE_DIR,'App/static/uploads/icon')


APP_PRIVATE_KEY=open(os.path.join(BASE_DIR,'alipay_config/app_rsa_private_key.txt'),'r').read()
ALYPAY_PUBLIC_KEY=open(os.path.join(BASE_DIR,'alipay_config/alipay_rsa_public_key.txt'),'r').read()
ALIPAY_APPID="2016101800715675"