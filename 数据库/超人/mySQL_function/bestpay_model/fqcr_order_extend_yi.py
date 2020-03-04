# coding: utf-8
from sqlalchemy import Column, DECIMAL, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OrderExtendYi(Base):
    __tablename__ = 'order_extend_yi'

    id = Column(INTEGER(11), primary_key=True)
    orderid = Column(String(255), index=True, server_default=text("''"))
    orderid_yi = Column(String(255), index=True, server_default=text("''"))
    user_extend_yi_id = Column(INTEGER(11), server_default=text("'0'"))
    p2p_user_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    user_id_yi = Column(String(50), index=True, server_default=text("''"))
    apply_no = Column(String(100), index=True, server_default=text("''"))
    auto_audit_version = Column(String(10), index=True, server_default=text("''"))
    manager_name = Column(String(255), server_default=text("''"))
    manager_mobile = Column(String(255), server_default=text("''"))
    user_main_id = Column(INTEGER(11), server_default=text("'0'"))
    install_count = Column(INTEGER(11), server_default=text("'0'"))
    goods_name = Column(String(255), server_default=text("''"))
    goods_price = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    pack_name = Column(String(255), server_default=text("''"))
    pack_price = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    total_money = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    telfare_principal = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    phone_principal = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    province = Column(String(255), server_default=text("''"))
    city = Column(String(255), server_default=text("''"))
    submit_data = Column(INTEGER(11), server_default=text("'0'"))
    id_number = Column(String(255), server_default=text("''"))
    user_name = Column(String(255), server_default=text("''"))
    mobile = Column(String(20), server_default=text("''"))
    contract_mobile = Column(String(20), server_default=text("''"))
    department = Column(String(255), server_default=text("''"))
    imei = Column(String(255), server_default=text("''"))
    state = Column(TINYINT(2), server_default=text("'1'"))
    type = Column(TINYINT(2), server_default=text("'1'"))
    staging_type = Column(TINYINT(2), nullable=False, server_default=text("'0'"))
    is_test = Column(TINYINT(4), server_default=text("'0'"))
    add_time = Column(INTEGER(11), server_default=text("'0'"))
    pack_id = Column(String(255), server_default=text("''"))
    goods_type = Column(String(255), server_default=text("''"))
    goods_num = Column(INTEGER(11), server_default=text("'0'"))
    goods_depict = Column(String(255), server_default=text("''"))
    order_depict = Column(String(255), server_default=text("''"))
    phone_operator = Column(String(255), server_default=text("''"))
    phone_maker = Column(String(255), server_default=text("''"))
    phone_type = Column(String(255), server_default=text("''"))
    phone_sys = Column(String(255), server_default=text("''"))
    llq_type = Column(String(255), server_default=text("''"))
    llq_version = Column(String(255), server_default=text("''"))
    score = Column(String(255), server_default=text("''"))
    wifi_type = Column(String(255), server_default=text("''"))
    wifi_ip = Column(String(255), server_default=text("''"))
    sales_lon = Column(String(255), server_default=text("''"))
    sales_lat = Column(String(255))
    store_address = Column(String(255), server_default=text("''"))
    seller_store_province = Column(String(255), nullable=False, server_default=text("''"))
    seller_store_city = Column(String(255), nullable=False, server_default=text("''"))
    seller_store_no = Column(String(100), nullable=False, server_default=text("''"))
    agent_name = Column(String(100), nullable=False, server_default=text("''"))
    agent_no = Column(String(100), nullable=False, server_default=text("''"))
    photo_id = Column(String(255), server_default=text("''"))
    pdf_id = Column(String(255), server_default=text("''"))
    bind_mobile = Column(String(20), nullable=False, server_default=text("''"))
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json