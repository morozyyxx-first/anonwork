from users.user_schema import UserRegSchema
from .db_engine import get_session
from .orms import UsersORM

async def add_user(new_user: UserRegSchema):
    async with await get_session() as session:
        session.add(
            UsersORM(
                username=new_user.username,
                email=new_user.email,
                password=new_user.password
            )
        )
        await session.commit()