import asyncio


async def request1():
    print("Before executing the function request")
    await asyncio.sleep(30)
    print("Event loop executed my function request")


async def request2():
    await asyncio.sleep(20)
    print("Event loop executed my function")


async def request3():
    await asyncio.sleep(10)
    print("Event loop executed mine before 2nd request")


async def main():
    t1 = asyncio.create_task(request1())
    t2 = asyncio.create_task(request2())
    t3 = asyncio.create_task(request3())

    tasks = [t1, t2, t3]
    await asyncio.gather(*tasks)

asyncio.run(main())
