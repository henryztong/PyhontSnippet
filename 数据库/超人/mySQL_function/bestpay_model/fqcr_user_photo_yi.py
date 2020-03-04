# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserPhotoYi(Base):
    __tablename__ = 'user_photo_yi'

    id = Column(INTEGER(11), primary_key=True)
    user_main_id = Column(INTEGER(11))
    photo_type = Column(INTEGER(3), nullable=False)
    photo_id = Column(String(20), nullable=False)
    photo_url = Column(String(100))
    user_extend_yi_id = Column(INTEGER(11))
    add_time = Column(INTEGER(11))
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json