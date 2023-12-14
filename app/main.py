import asyncio

# from sqlalchemy import select
#
# from app.db import async_session
# from app.models import User
from app.telegram import start_bot

# async def main():
#     async with async_session() as session:
#         result = await session.execute(select(User))
#         for user in result.scalars():
#             print(user.__dict__)
#

if __name__ == "__main__":
    asyncio.run(start_bot())
