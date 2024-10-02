from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
def read_user_info(username: Optional[str] = None, age: Optional[int] = None):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
