import asyncio
import time
from datetime import datetime

async def display_time():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
        await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(display_time())
    await task

if __name__ == "__main__":
    asyncio.run(main())