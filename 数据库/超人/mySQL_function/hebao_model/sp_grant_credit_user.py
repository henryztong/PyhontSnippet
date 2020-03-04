# coding: utf-8
from sqlalchemy import CHAR, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CreditUser(Base):
    __tablename__ = 'credit_user'

    id = Column(INTEGER(10), primary_key=True, server_default=text("'0'"))
    user_id = Column(String(20), nullable=False, server_default=text("'0'"))
    idname = Column(String(50), nullable=False, server_default=text("''"))
    idcard = Column(CHAR(18), nullable=False, server_default=text("''"))
    sex = Column(CHAR(1), nullable=False, server_default=text("'2'"))
    mobile = Column(String(20), nullable=False, server_default=text("''"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    idcard_type = Column(CHAR(1), nullable=False, server_default=text("'1'"))
    idcard_exp_sdt = Column(CHAR(7), nullable=False, server_default=text("''"))
    idcard_exp_edt = Column(CHAR(7), nullable=False, server_default=text("''"))
    photo_ids = Column(String(50), nullable=False, server_default=text("''"))
    contact_ids = Column(String(50), nullable=False, server_default=text("''"))
    user_star_lv1 = Column(String(50), nullable=False, server_default=text("''"))
    user_prov_no = Column(String(50), nullable=False, server_default=text("''"))
    created = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    deleted_at = Column(INTEGER(10))
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json