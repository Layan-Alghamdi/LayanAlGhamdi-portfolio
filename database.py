from sqlalchemy import create_engine, text
import os 
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)



def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from myproject"))
    myproject = []
    for row in result.all():
      myproject.append(dict(row._mapping))
    return myproject
