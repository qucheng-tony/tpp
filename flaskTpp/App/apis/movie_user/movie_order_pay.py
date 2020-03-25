from flask import request
from flask_restful import Resource
from alipay import AliPay

from App.apis.api_constant import HTTP_OK
from App.settings import APP_PRIVATE_KEY, ALYPAY_PUBLIC_KEY, ALIPAY_APPID


class MovieOrderPayResource(Resource):
    def get(self,order_id):
        alipay_client = AliPay(
            appid=ALIPAY_APPID,
            app_notify_url=None,  # 默认回调url
            app_private_key_string=APP_PRIVATE_KEY,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=ALYPAY_PUBLIC_KEY,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True,  # 默认False
        )
        subject = "用户支付"
        order_string = alipay_client.api_alipay_trade_wap_pay(
            out_trade_no=request.args.get('id'),
            total_amount=request.args.get('money'),
            subject=subject,
            return_url="https://www.baidu.com",
            notify_url="https://www.baidu.com"  # 可选, 不填则使用默认notify url
        )
        pay_url='https://openapi.alipaydev.com/gateway.do?' + order_string
        data={
            'status':HTTP_OK,
            'msg':'ok',
            'data':{
                'pay_url':pay_url,
                'appid':order_id,
            }
        }
        return data