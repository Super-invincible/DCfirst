#-*- encoding:utf-8 -*-
from hello import User_mode,db
judge = User_mode(name='评委老师')
manager = User_mode(name='管理员')
student = User_mode(name='学生')
proleader = User_mode(name='项目负责人')
db.session.add(judge)
db.session.add(manager)
db.session.add(student)
db.session.add(proleader)
db.session.commit()
