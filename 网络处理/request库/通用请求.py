import requests
import json

dic = {"head":{"tranCode":"CF201060","applSeq":"2019101611150010000266859","tranDate":"2019-10-16","tranTime":"2019-10-16 11:15:00","chlresource":"832159783X","bchCde":"900000","version":"1.0"},"body":{"applseq":"4181088","time_stamp":"20191016111313.955","trade_type":"002","contents":[{"idno":"513922198907080018","custname":"唐宇鹏","chlfkseq":"A1013442071","trade_seq":"A1013442071","pay_seq":"2021042000001798","chlresource":"832159783X","loan_no":"HT90201910151900004295799001","cont_no":"HT90201910151900004295799","paymentmode":"NF","perd_no":"1","total_amt":"1313","trade_amt":"57.09","deal_amt":"57.09","balace_amt":"1255.91","norm_int_amt":"0","od_int_amt":"0","comm_int_amt":"0","fee_amt":"0","trade_dt":"2021-04-20","payment_ind":"20","result_code":"10","result_msg":""}]}}
header=dic['head']
body=dic['body']

# 晋商还款通知地址
def jingshang_message():
	url='http://api.test.fenqichaoren.com/jinshang/Apply/repayment_notify'
	# result=requests.post(url,headers=header,data=json.dumps(body))
	# result=requests.post(url,data=json.dumps(body))
	print(result.text)


if __name__ == '__main__':
	jingshang_message()