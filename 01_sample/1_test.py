# coding: UTF-8
import asyncio
import time

async def lazy_process(name, sec):
  print(f'start {name}')
  await asyncio.sleep(sec)
  print(f'end {name}')
  return f'{name}/{sec}'

# print(lazy_process('hey', 5))

start = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
  lazy_process('hello', 5)
)
end = time.time()

print(result)
print(f'Process Time: {end - start}')
