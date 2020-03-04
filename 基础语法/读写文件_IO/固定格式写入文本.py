  def writeInto_RiskControlB(self,apply_no,txt_url):
    # 该方法作用：将自动审核RiskControlB模块需要的参数从数据库中查询出来写入到文本
    # txt_url 文本输出地址，txt_url = "../data/autoCheck_data/bestpay/RiskControlB.txt" 
    # apply_no 被查询的流水号

    # 判断要输出的文档中是否已存在内容，存在则清除
    with open(txt_url,'w+',encoding='utf-8') as config:
      if config.read():
        pass
    
    # 自动审核RiskControlB模块需要的参数
    UserExtendYi_lRiskControlB_list = ['apply_no','id_number','residence_address','company_name','company_address','bank_no','is_married','industry_type','company_telephone','education','user_name','salary']
    UserLinkmanYi_RiskControlB_list = ['contact_name','contact_mobile','contact_relation_ship']

    # 经度、纬度、公司所属行业、在职状态、商户评级
    dicts = {'applyer_type':'','sellerAssess':'','main_phone':'','email':''}

    # 查询对应表中的数据
    DB_basic= func_DataSQL_basic(self.session)
    UserExtendYi_list = DB_basic.one_table(UserExtendYi,UserExtendYi.apply_no,apply_no)
    UserLinkmanYi_list = DB_basic.two_table(UserExtendYi,UserExtendYi.id,UserLinkmanYi,UserLinkmanYi.user_extend_yi_id,UserExtendYi.apply_no,apply_no)
    # 筛选后写入文本
    self.query_filter(UserExtendYi_list,UserExtendYi_lRiskControlB_list,txt_url)
    self.query_filter(UserLinkmanYi_list,UserLinkmanYi_RiskControlB_list,txt_url)
    self.write_format(dicts,txt_url)


  def write_format(self,read_dict,txt_url):
    # 该方法作用：按照一定格式写入到文本   
    # txt_url 文本输出地址，txt_url = "./input_parameter1.txt"
    # read_dict读取要写入的值

    string = '' 
    config =open(txt_url,'a+',encoding="utf-8")# a+表示在文本结尾继续写入内容
    # print(read)
    for x in read_dict:
      string = x+':'+str(read_dict[x])+'\n'
      # print(string) 
      config.write(string)
    config.close()


  def query_filter(self,query_list,key_list,txt_url,table_name=''):   
    # 该方法作用：从数据库查询到的结果中筛选出对应的字段的值，以一定格式写入文本    
    # query_list数据库查询结果
    # key_list要筛选的字段名列表
    # table_name是加的备注信息，以便区分不同表字段名相同，调试用可不加
    # txt_url 文本输出地址

    for dict_data in query_list:  
      # 该表达式作用等于下面的for语句
      dic = {x:dict_data[x] for x in key_list if x in dict_data} 
      # dicts = {}
      # for x in key_list:
      #   # print(x)
      #   if x in dict_data:
      #     # print(x)
      #     # print(dict_data[x])
      #     key =table_name+x
      #     dicts[key]=dict_data[x]
      # print(dicts)
      self.write_format(dic,txt_url)
    # return  dic 

  def data_saved(self,apply_no):
    DB_basic= func_DataSQL_basic(self.session)
    UserExtendYi_list = DB_basic.one_table(UserExtendYi,UserExtendYi.apply_no,apply_no)
    print(UserExtendYi_list)