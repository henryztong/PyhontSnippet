# coding: utf-8
from sqlalchemy import CHAR, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserContact(Base):
    __tablename__ = 'user_contacts'

    id = Column(INTEGER(10), primary_key=True)
    credit_id = Column(INTEGER(10), nullable=False)
    partner_uid = Column(String(128), nullable=False, server_default=text("''"))
    user_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    relation_ship = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    contact_name = Column(String(50), nullable=False, server_default=text("''"))
    contact_mobile = Column(CHAR(11), nullable=False, server_default=text("''"))
    network_status = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    attribution = Column(String(50), nullable=False, server_default=text("''"))
    conformity = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    type = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    deleted_at = Column(INTEGER(10))
    created = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json

