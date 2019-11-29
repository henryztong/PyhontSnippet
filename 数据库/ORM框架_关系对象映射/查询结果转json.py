# https://blog.csdn.net/weixin_41829272/article/details/80658586
# https://blog.csdn.net/weixin_44517681/article/details/90737617
# https://www.cnblogs.com/zishu/p/10977232.html

# coding: utf-8
from sqlalchemy import Column, Float, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Credit(Base):
    __tablename__ = 'credits'

    id = Column(INTEGER(10), primary_key=True)
    apply_no = Column(String(128), nullable=False, server_default=text("''"))
    partner_uid = Column(String(20), nullable=False, server_default=text("''"))
    user_id = Column(String(20), nullable=False, server_default=text("''"))
    channel = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    status = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    ret_msg = Column(String(32), nullable=False, server_default=text("''"))
    audit_status = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    bank_api_status = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    credit_msg = Column(String(32), nullable=False, server_default=text("''"))
    credit_amt = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    eff_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    exp_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    credit_lock_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    created = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    deleted_at = Column(INTEGER(10))
    main_phone = Column(String(60), nullable=False, server_default=text("''"))
    auto_audit_version = Column(String(30), nullable=False, server_default=text("''"))
    face_score = Column(Float(10), nullable=False, server_default=text("'0.00'"))
    auto_audit_remark = Column(String(255), nullable=False, server_default=text("''"))
    operator_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json

