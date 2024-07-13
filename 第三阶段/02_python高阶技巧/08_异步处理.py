import asyncio


async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


async def main():
    # 创建多个异步任务
    task1 = asyncio.create_task(greet("Alice", 2))
    task2 = asyncio.create_task(greet("Bob", 1))
    task3 = asyncio.create_task(greet("Charlie", 3))

    # 等待所有任务完成
    await asyncio.gather(task1, task2, task3)


# 运行主协程
asyncio.run(main())
