# coding: utf-8
from sqlalchemy import CHAR, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserPhoto(Base):
    __tablename__ = 'user_photos'

    id = Column(INTEGER(10), primary_key=True)
    credit_id = Column(INTEGER(10), nullable=False)
    partner_uid = Column(String(20), nullable=False, server_default=text("''"))
    channel = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    idcard = Column(CHAR(18), nullable=False, server_default=text("''"))
    idcard_front_id = Column(String(255), nullable=False, server_default=text("''"))
    idcard_back_id = Column(String(255), nullable=False, server_default=text("''"))
    live_picture_id = Column(String(255), nullable=False, server_default=text("''"))
    idcard_front_url = Column(String(255), nullable=False, server_default=text("''"))
    idcard_back_url = Column(String(255), nullable=False, server_default=text("''"))
    live_picture_url = Column(String(255), nullable=False, server_default=text("''"))
    live_org_num = Column(String(128), nullable=False, server_default=text("''"))
    live_org_id = Column(String(32), nullable=False, server_default=text("''"))
    live_org_score = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
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