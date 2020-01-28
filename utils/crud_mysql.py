
from orm_operate.operate_curd import session
from orm_operate.operate_curd import User
class DbUtil():

    def select(self, table_name, id):
        result = session.query(table_name).filter_by(id=id).first()
        return result



if __name__ == '__main__':
    dbutil = DbUtil()
    rs = dbutil.select(User, 3)
    print(rs.age)
