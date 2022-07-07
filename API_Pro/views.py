import uvicorn
from database import cursor, conn
from app import app
from models import UserData


@app.get("/")
def get_all_users():
    try:
        query = 'select * from user_data'
        cursor.execute(query)
        all_user_details = []
        all_user_data = cursor.fetchall()
        for data in all_user_data:
            user_details = {
                "ID": data[0],
                "Name": data[1],
                "E-mail": data[2],
                "Place": data[3]
            }
            all_user_details.append(user_details)
        return {"User Details": all_user_details}
    except Exception as e:
        print(e)


@app.get("/user/{id}")
def get_single_user(id: int):
    query = 'select * from user_data'
    cursor.execute(query)
    all_user_data = cursor.fetchall()
    one_user_details = []
    name = ''
    for data in all_user_data:
        if id == data[0]:
            user_data = {
                "ID": data[0],
                "Name": data[1],
                "E-mail": data[2],
                "Place": data[3]
            }
            name += data[1]
            one_user_details.append(user_data)
    if len(one_user_details) >= 1:
        return {f"{name}'s Details": one_user_details}
    else:
        return {"Message": "No user found with the entered ID"}


@app.post("/userData")
def get_user_data(info: UserData):
    id = info.id
    name = info.name
    email = info.email
    place = info.place
    new_user = "insert into user_data(id, name, email, place) values(%s, %s, %s, %s)"  # noqa
    cursor.execute(new_user, (id,
                              name,
                              email,
                              place)
                   )
    conn.commit()
    return {
        "status": "SUCCESS",
        "data": info
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=False)
