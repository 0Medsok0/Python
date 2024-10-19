import asyncio
import time

# Настраиваемые параметры
DB_QUERY_DURATION = 0.2  # Длительность запроса в БД (начальное значение – 0.2 с)
REQUEST_PROCESSING_DURATION = 0.1  # Время обработки запроса и формирование ответа (начальное значение – 0.1 с)

async def process_request_sync():
    # Имитация запроса в БД
    await asyncio.sleep(DB_QUERY_DURATION)
    # Имитация обработки запроса и формирования ответа
    await asyncio.sleep(REQUEST_PROCESSING_DURATION)

async def process_request_async():
    # Имитация асинхронного запроса в БД
    await asyncio.sleep(DB_QUERY_DURATION)
    # Имитация асинхронной обработки запроса и формирования ответа
    await asyncio.sleep(REQUEST_PROCESSING_DURATION)

async def simulate_system(num_requests, processing_func):
    tasks = []
    for _ in range(num_requests):
        task = asyncio.create_task(processing_func())
        tasks.append(task)
    await asyncio.gather(*tasks)

async def main():
    num_requests = 100000  # Количество запросов для моделирования
    start_time = time.time()

    # Моделирование синхронного взаимодействия
    await simulate_system(num_requests, process_request_sync)
    sync_time = time.time() - start_time
    print(f"Синхронное взаимодействие: {num_requests} запросов обработано за {sync_time:.2f} секунд")

    start_time = time.time()

    # Моделирование асинхронного взаимодействия
    await simulate_system(num_requests, process_request_async)
    async_time = time.time() - start_time
    print(f"Асинхронное взаимодействие: {num_requests} запросов обработано за {async_time:.2f} секунд")

    max_requests_per_second = num_requests / min(sync_time, async_time)
    print(f"Максимальное количество обработанных запросов за 10 секунд: {max_requests_per_second:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
