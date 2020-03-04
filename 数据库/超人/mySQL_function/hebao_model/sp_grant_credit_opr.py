# coding: utf-8
from sqlalchemy import CHAR, Column
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CreditOpr(Base):
    __tablename__ = 'credit_opr'

    id = Column(INTEGER(11), primary_key=True)
    opr_id = Column(INTEGER(11), nullable=False)
    opr_mobile = Column(CHAR(11), nullable=False)
    reg_dt = Column(INTEGER(10), nullable=False)
    deleted_at = Column(INTEGER(10))
    # 将查询到的对象数据转字典
    def to_dict(self):
        dic = {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
        return dic
     
    # 当查询结果有多个值时转换成json的函数
    def to_json(all_vendors):
        json = [ven.to_dict() for ven in all_vendors]
        return json