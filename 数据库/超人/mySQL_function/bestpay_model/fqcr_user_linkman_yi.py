# coding: utf-8
from sqlalchemy import CHAR, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserLinkmanYi(Base):
    __tablename__ = 'user_linkman_yi'

    id = Column(INTEGER(11), primary_key=True)
    user_main_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    contact_relation_ship = Column(TINYINT(4), nullable=False, server_default=text("'99'"))
    contact_name = Column(String(20), nullable=False, server_default=text("''"))
    contact_mobile = Column(CHAR(11), nullable=False, server_default=text("''"))
    network_status = Column(String(4), nullable=False, server_default=text("''"))
    attribution = Column(String(20), nullable=False, server_default=text("''"))
    user_extend_yi_id = Column(INTEGER(11), server_default=text("'0'"))
    conformity = Column(TINYINT(4), nullable=False, server_default=text("'2'"))
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json