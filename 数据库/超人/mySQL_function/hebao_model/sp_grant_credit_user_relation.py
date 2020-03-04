# coding: utf-8
from sqlalchemy import CHAR, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CreditUserRelation(Base):
    __tablename__ = 'credit_user_relation'

    id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    bank_card_no = Column(String(50), nullable=False, server_default=text("''"))
    bank_card_code = Column(String(50), nullable=False, server_default=text("''"))
    bank_card_name = Column(String(50), nullable=False, server_default=text("''"))
    bank_card_mobile = Column(CHAR(11), nullable=False, server_default=text("''"))
    province = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    city = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    area = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    zip_code = Column(CHAR(12), nullable=False, server_default=text("''"))
    address = Column(String(128), nullable=False, server_default=text("''"))
    in_come = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    user_job = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    schooling = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    socialIdentity = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    marital_sta = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    country = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    nation = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    deleted_at = Column(INTEGER(10))
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json