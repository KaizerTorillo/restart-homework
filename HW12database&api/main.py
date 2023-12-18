from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


def get_db():
    db = Session()  # Assuming you have a Session configured
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/heroes/")
def create_hero(hero: Hero, db: Depends(get_db)):
    db_hero = Hero(**hero.dict())
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero


@app.get("/heroes/{name}")
def get_hero(
    name: str, db: Depends(get_db)
) -> (
    Hero
):  # type hint that the function will return an item that belongs to the Hero class model. FastAPI will also check if the returned item mathces the HERO model
    statement = select(Hero).where(Hero.name == name)
    hero = db.exec(statement).first()
    if hero:
        return hero
    else:
        raise HTTPException(status_code=404, detail=f"Hero not found: {name}")


@app.get("/heroes/")
def get_heroes():
    statement = select(Hero)
    heroes = db.exec(statement).all()
    return heroes


# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
# hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


# engine = create_engine("sqlite:///database.db")


# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#    session.add(hero_1)
#    session.add(hero_2)
#    session.add(hero_3)
#    session.commit()

# with Session(engine) as session:
#    statement = select(Hero).where(Hero.name == "Spider-Boy")
#    heroes = session.exec(statement).all()  # returns list of all records that match
#    print(heroes)
#    print(type(heroes))
#    hero = session.exec(statement).first()  # returns only firs    print(hero)
