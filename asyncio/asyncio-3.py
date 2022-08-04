import asyncio


async def square(num):
    await asyncio.sleep(num)
    # print(f"tasks {num} compute value is {num * num}")
    return num


async def main():
    tasks = []
    for i in range(10, 0, -1):
        t1 = asyncio.create_task(square(i))
        tasks.append(t1)

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
