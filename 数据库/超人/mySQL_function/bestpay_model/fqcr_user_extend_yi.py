# coding: utf-8
from sqlalchemy import Column, DECIMAL, Float, Index, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserExtendYi(Base):
    __tablename__ = 'user_extend_yi'
    __table_args__ = (
        Index('user_main_id', 'user_main_id', 'user_id_yi'),
    )

    id = Column(INTEGER(16), primary_key=True)
    orderid = Column(String(32), nullable=False, index=True)
    apply_no = Column(String(100))
    user_main_id = Column(INTEGER(11), nullable=False)
    phone = Column(String(20))
    user_name = Column(String(50))
    user_id_yi = Column(String(50))
    main_phone = Column(String(11), nullable=False, server_default=text("''"))
    id_number = Column(String(20), nullable=False)
    id_validity_start = Column(String(20), server_default=text("''"))
    id_validity_end = Column(String(20), server_default=text("''"))
    idcard_type = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    residence_address = Column(String(60))
    is_married = Column(TINYINT(1))
    company_telephone = Column(String(13))
    education = Column(TINYINT(1), server_default=text("'0'"))
    graduation_date = Column(INTEGER(11))
    company_name = Column(String(30))
    company_address = Column(String(255))
    industry_type = Column(TINYINT(1))
    salary = Column(TINYINT(1))
    bank_mobile_no = Column(String(13), nullable=False)
    credit_card_no = Column(String(30), nullable=False)
    bank_name = Column(String(255), nullable=False)
    bank_no = Column(String(30))
    seller_name = Column(String(60))
    seller_province = Column(String(100))
    seller_city = Column(String(100))
    seller_mobile = Column(String(13))
    department = Column(String(30))
    seller_store_address = Column(String(255), nullable=False, server_default=text("''"))
    seller_store_no = Column(String(32), nullable=False, server_default=text("''"))
    longitude = Column(String(10), server_default=text("''"))
    latitude = Column(String(10))
    address_province = Column(String(80))
    address_city = Column(String(80))
    address_county = Column(String(80))
    address_detail = Column(String(80))
    imei = Column(String(80))
    carrier = Column(String(80))
    phone_maker = Column(String(80))
    phone_model = Column(String(80))
    system_type = Column(String(10))
    browser_type = Column(String(10))
    brower_version = Column(String(10))
    security_score = Column(String(10))
    network_type = Column(String(10))
    ip = Column(String(20))
    credit_status = Column(TINYINT(1), server_default=text("'1'"))
    credit_type = Column(TINYINT(4), server_default=text("'0'"))
    credit_message = Column(Text)
    credit_result_id = Column(String(30))
    scene_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    remain_limit = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    change_scene_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    next_url = Column(String(255), server_default=text("''"))
    contract_start_date = Column(INTEGER(13))
    contract_end_date = Column(INTEGER(13))
    remark = Column(Text)
    status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    start_date = Column(INTEGER(13))
    up_date = Column(INTEGER(13))
    create_time = Column(INTEGER(11), index=True)
    callback_time = Column(INTEGER(11))
    check_id = Column(String(30))
    need_check = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    operator = Column(String(30), nullable=False, server_default=text("''"))
    seller_main_id = Column(INTEGER(11), index=True)
    seller_main_name = Column(String(255), server_default=text("''"))
    apply_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    type = Column(INTEGER(11), server_default=text("'0'"))
    tongdun_status = Column(TINYINT(1), server_default=text("'0'"))
    tongdun_res = Column(Text)
    white_knight_status = Column(TINYINT(4), server_default=text("'0'"))
    white_knight_res = Column(Text)
    face_score = Column(Float(5), server_default=text("'0.00'"))
    phone_bill_grade = Column(String(10), nullable=False, server_default=text("''"))
    network_time = Column(String(10), nullable=False, server_default=text("''"))
    has_callback = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    auto_audit_remark = Column(String(255), nullable=False, server_default=text("''"))
    manual_handling = Column(TINYINT(2), server_default=text("'0'"))
    is_test = Column(TINYINT(2), server_default=text("'0'"))
    auto_audit_version = Column(String(10), nullable=False, server_default=text("''"))
    auto_scene_amount = Column(INTEGER(10), server_default=text("'0'"))
    credit_amount_log = Column(Text)
    audit_modelb_score_remark = Column(String(255), nullable=False, server_default=text("''"))
    audit_modelb_score = Column(DECIMAL(10, 2))
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json