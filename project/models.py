import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Enum, DateTime, Time, Float
from enum import Enum as UserEnum
from sqlalchemy.orm import relationship
from project import db, app
from flask_login import UserMixin
import hashlib

default_password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2
    STAFF = 3


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    fullname = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(300), default=default_password)
    avatar = Column(String(300))
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.fullname


class Airport(BaseModel):
    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class FlightSchedule(BaseModel):
    __tablename__ = 'flight_sche'

    airport_from = Column(Integer, ForeignKey(Airport.id))
    airport_to = Column(Integer, ForeignKey(Airport.id))

    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)

    time_start = Column(DateTime, nullable=False)
    time_end = Column(DateTime, nullable=False)
    quantity_ticket_1st = Column(Integer, nullable=False)
    quantity_ticket_1st_booked = Column(Integer, default=0)
    quantity_ticket_2nd = Column(Integer, nullable=False)
    quantity_ticket_2nd_booked = Column(Integer, default=0)
    price = Column(Integer, default=0)

    bw_airports = relationship('BetweenAirport', backref='flight_sche', lazy=False)

    def __str__(self):
        return str(self.id)


class BetweenAirport(BaseModel):
    __tablename__ = 'between_airport'

    airport_id = Column(Integer, ForeignKey(Airport.id))
    flight_sche_id = Column(Integer, ForeignKey(FlightSchedule.id))
    time_stay = Column(Float, nullable=False)
    note = Column(String(100))

    is_deleted = Column(Boolean, default=False)


class Customer(BaseModel):
    customer_name = Column(String(100), nullable=False)
    customer_phone = Column(String(10), nullable=False)
    customer_id = Column(String(10), nullable=False)


class Ticket(BaseModel):
    author_id = Column(Integer, ForeignKey(User.id), nullable=True)
    customer_id = Column(Integer, ForeignKey(Customer.id))
    flight_sche_id = Column(Integer, ForeignKey(FlightSchedule.id))
    ticket_price = Column(Integer, nullable=False)
    ticket_type = Column(Integer, nullable=False)
    ticket_package_price = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now())


class ADMINRules(BaseModel):
    min_time_flight_sche = Column(Float, default=0.5)
    max_between_airport_quantity = Column(Float, default=2)
    min_time_stay_airport = Column(Float, default=0.33)
    max_time_stay_airport = Column(Float, default=0.5)
    customer_time_ticket = Column(Float, default=12)
    staff_time_ticket = Column(Float, default=4)
    created_at = Column(DateTime, default=datetime.datetime.now())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        a = User(fullname='Quản trị viên', username='admin', user_role=UserRole.ADMIN, avatar='https://res.cloudinary.com/dba0vclo4/image/upload/v1704361304/user_kppyl1.png')
        s = User(fullname='Nhân viên', username='staff', user_role=UserRole.STAFF, avatar='https://res.cloudinary.com/dba0vclo4/image/upload/v1704361304/user_kppyl1.png')
        u = User(fullname='Người dùng', username='user', user_role=UserRole.USER, avatar='https://res.cloudinary.com/dba0vclo4/image/upload/v1704361304/user_kppyl1.png')
        db.session.add_all([a, s, u])
        db.session.commit()

        a1 = Airport(name="Sân bay Quốc tế Nội Bài")
        a2 = Airport(name="Sân bay Quốc tế Tân Sơn Nhất")
        a3 = Airport(name="Sân bay Quốc tế Đà Nẵng")
        a4 = Airport(name="Sân bay Quốc tế Vân Đồn")
        a5 = Airport(name="Sân bay Quốc tế Cát Bi")
        a6 = Airport(name="Sân bay Quốc tế Vinh")
        a7 = Airport(name="Sân bay Quốc tế Phú Bài")
        a8 = Airport(name="Sân bay Quốc tế Cam Ranh")
        a9 = Airport(name="Sân bay Quốc tế Liên Khương")
        a10 = Airport(name="Sân bay Quốc tế Phù Cát")
        a11 = Airport(name="Sân bay Quốc tế Cần Thơ")
        a12 = Airport(name="Sân bay Quốc tế Phú Quốc")
        a13 = Airport(name="Sân bay Quốc tế Long Thành")
        a14 = Airport(name="Sân bay Điện Biên Phủ")
        a15 = Airport(name="Sân bay Thọ Xuân")
        a16 = Airport(name="Sân bay Đồng Hới")
        a17 = Airport(name="Sân bay Chu Lai")
        a18 = Airport(name="Sân bay Tuy Hòa")
        a19 = Airport(name="Sân bay Pleiku")
        a20 = Airport(name="Sân bay Pleiku")
        a21 = Airport(name="Sân bay Rạch Giá")
        a22 = Airport(name="Sân bay Cà Mau")
        a23 = Airport(name="Sân bay Côn Đảo")

        db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23])
        db.session.commit()

        a = ADMINRules()
        db.session.add(a)
        db.session.commit()

        pass
