from sqlmodel import SQLModel, create_engine, Session

sqlite_url = "sqlite:///./database2.db"
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session