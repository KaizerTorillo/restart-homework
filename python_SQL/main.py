from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="DIve Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", age=34)
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()


with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")
    hero = session.exec(
        statement
    ).first()  # Returns the first result, helpful if there are multiple results and you only want the first one
    print(hero)
    # heroes = session.exec(statement).all()     #This will return all the items in the databse that match your specified hero name
    # print(heroes)
