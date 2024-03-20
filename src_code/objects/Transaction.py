####
# An object representing the transactions of our wares inside the Warehouse system
# - CLY 18-03-24 -
####
# Imports
from sqlalchemy import Column, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src_code.db.Database import Base
from datetime import datetime
from src_code.objects.Ware import Ware
# Globals
# Get Base and Session from Database
# Class
class Transaction(Base):
    __tablename__ = 'transactions'

    TransactionID = Column(Integer, primary_key=True, autoincrement=True)
    WareID = Column(Integer, ForeignKey('wares.wareId'))
    TransactionType = Column(Enum('IN', 'OUT'))
    Quantity = Column(Integer)
    TransactionDate = Column(DateTime, default=datetime.now)

    ware = relationship(Ware, back_populates="transactions")

    def __repr__(self):
        return str(self.as_dict())
    
    def as_dict(self):
        return {
            "TransactionID": self.TransactionID,
            "WareID": self.WareID,
            "Quantity": self.Quantity,
            "TransactionType": self.TransactionType,
            "TransactionDate": self.TransactionDate.strftime('%Y-%m-%d %H:%M:%S')
        }

    @classmethod
    def create(cls, session, ware_id, quantity, transaction_type, transaction_date):
        try:
            new_transaction = cls(
                WareID=ware_id,
                Quantity=quantity,
                TransactionType=transaction_type,
                TransactionDate=transaction_date
            )
            session.add(new_transaction)
            session.commit()
            print("Transaction added successfully!")
            return new_transaction
        except Exception as e:
            print(f"Error adding transaction: {e}")
            session.rollback()

    @classmethod
    def read(cls, session, transaction_id):
        try:
            transaction = session.query(cls).filter_by(TransactionID=transaction_id).first()
            return transaction
        except Exception as e:
            print(f"Error reading transaction: {e}")

    @classmethod
    def update(cls, session, transaction_id, ware_id=None, transaction_type=None, quantity=None):
        try:
            transaction = session.query(cls).filter_by(TransactionID=transaction_id).first()
            if transaction:
                if ware_id:
                    transaction.WareID = ware_id
                if transaction_type:
                    transaction.TransactionType = transaction_type
                if quantity:
                    transaction.Quantity = quantity
                session.commit()
                print("Transaction updated successfully!")
        except Exception as e:
            print(f"Error updating transaction: {e}")
            session.rollback()

    @classmethod
    def delete(cls, session, transaction_id):
        try:
            transaction = session.query(cls).filter_by(TransactionID=transaction_id).first()
            if transaction:
                session.delete(transaction)
                session.commit()
                print("Transaction deleted successfully!")
        except Exception as e:
            print(f"Error deleting transaction: {e}")
            session.rollback()

    @classmethod
    def report(cls, session, start_date=None, end_date=None, transaction_type=None):
        try:
            query = session.query(cls)
            if start_date:
                query = query.filter(cls.TransactionDate >= start_date)
            if end_date:
                query = query.filter(cls.TransactionDate <= end_date)
            if transaction_type:
                query = query.filter_by(TransactionType=transaction_type)
            transactions = query.all()
            return transactions
        except Exception as e:
            print(f"Error generating transaction report: {e}")