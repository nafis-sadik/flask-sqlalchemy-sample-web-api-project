from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String)
    LastName = Column(String)
    UserName = Column(String)
    Password = Column(String)


if __name__ == '__main__':
    engine = create_engine('sqlite:///:database:', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
