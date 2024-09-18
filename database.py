from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database setup
Base = declarative_base()
engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
session = Session()

# task table
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    status = Column(String)

# make table
Base.metadata.create_all(engine)

# functions
def add_new_task(description):
    new_task = Task(description=description, status="incomplete")
    session.add(new_task)
    session.commit()

def delete_task_with_id(task_id):
    task = session.query(Task).filter_by(id=int(task_id)).first()
    if task:
        session.delete(task)
        session.commit()
        return True
    else:
        return False

def all_tasks():
    return session.query(Task).all()

def complete_task_with_id(task_id):
    task = session.query(Task).filter_by(id=int(task_id)).first()
    if task:
        task.status = "complete"
        session.commit()
        return True
    else:
        return False


