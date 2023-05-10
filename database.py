# import datetime
#
# from CTFd.models import db, Challenges, Users
#
#
# class DataAPIMon(db.Model):
#     __tablename__ = "DataAPIMon"
#     id = db.Column(db.Integer, primary_key=True)
#     usernumber = db.Column(db.Text)
#     date = db.Column(db.Text)
#
#     def __init__(self, usernumber, date):
#         self.usernumber = usernumber
#         self.date = date
#
#
# def add_DataAPIMon(usernumber, data):
#     now = datetime.datetime.now()
#     month = now.month
#     day = now.day
#     data = DataAPIMon(usernumber, str(month.day))
#
#
# def clear_DataAPIMon():
#     delete_query = db.session.DataAPIMon.delete()
#     db.session.execute(delete_query)
#     # 提交更改并关闭连接
#     db.session.commit()
