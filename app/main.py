import asyncio

from app.gpt import run_matching
from app.logs import logger
from app.telegram import send_proposals, start_bot


async def run_matching_periodically(seconds_to_wait):
    logger.info(f"Periodical matching is set up to run once in {seconds_to_wait} seconds")
    while True:
        await asyncio.sleep(seconds_to_wait)
        await run_matching()
        logger.info("Matching finished successfully")
        await send_proposals()
        logger.info("Proposals were sent to users")


async def main():
    logger.info("Starting periodical matching...")
    matcher = asyncio.create_task(run_matching_periodically(60 * 60 * 12))
    logger.info("Starting bot...")
    bot = asyncio.create_task(start_bot())
    await asyncio.gather(bot, matcher)


if __name__ == "__main__":
    asyncio.run(main())
