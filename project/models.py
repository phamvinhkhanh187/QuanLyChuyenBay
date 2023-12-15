from project import db, app
from sqlalchemy import Column, Integer, String,Float, ForeignKey, Enum, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
import enum
import hashlib

class AccountRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2
class TicketTypeEnum(enum.Enum):
    Round_Trip = 1
    One_Way = 2

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class UserAccount(BaseModel, UserMixin):
    account_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    reg_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    phone = Column(String(10), nullable=False)
    user_role = Column(Enum(AccountRoleEnum), default=AccountRoleEnum.USER)
    ticket = relationship('Ticket', backref='useraccount', lazy=True)
    def __str__(self):
        return self.account_name

class Seat(BaseModel):
    __tablename__ = 'seats'
    seat_name = Column(String(50), nullable=False)
    airplane_id = Column(Integer, ForeignKey('airplanes.id'), nullable=False)
    airplane = relationship('Airplane', back_populates='seats')
class Airplane(BaseModel):
    __tablename__ = 'airplanes'
    airplane_name = Column(String(50), nullable=False)
    production_place = Column(String(50))
    number_of_passengers = Column(Integer, nullable=False)
    ticket = relationship('Ticket', backref='airplane', lazy=True)
    seats = relationship('Seat', back_populates='airplane', uselist=False)

class FlightRoute(BaseModel):
    route_name = Column(String(50), nullable=False)
    origin = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)

class Flight(BaseModel):
    flight_time = Column(DateTime(), nullable=False)
    landing_time = Column(DateTime(), nullable=False)
    flight_type = Column(String(50))
    flight_route_id = Column(Integer, ForeignKey(FlightRoute.id), nullable=False)
    airplane_id = Column(Integer, ForeignKey(Airplane.id), nullable=False)

class Ticket(BaseModel):
    __tablename__ = 'tickets'
    price = Column(Float, nullable=False)
    ticket_type = Column(Enum(TicketTypeEnum), nullable=False)
    buy_time = Column(DateTime(), nullable=False)
    user_account_id = Column(Integer, ForeignKey(UserAccount.id), nullable=False)
    flight_id = Column(Integer, ForeignKey(Flight.id), nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id"), nullable=False)
    seat = relationship('Seat', back_populates='ticket', uselist=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()