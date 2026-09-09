from fastapi import HTTPException
from sqlalchemy import select

from users.user_schema import UserLogSchema
from .db_engine import get_session
from .orms import UsersORM

async def get_user(user: UserLogSchema):
    async with await get_session() as session:
        inputted_password = user.password
        queried_password = select(UsersORM.password).filter_by(email=user.email)
        res = await session.execute(queried_password)
        true_password = res.scalars().first()
        if true_password != inputted_password:
            raise HTTPException(status_code=401)