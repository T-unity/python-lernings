# coding: UTF-8
import asyncio
import time

async def lazy_process(process1, process2, final, sec):
  print(f'{process1}')
  await asyncio.sleep(sec)
  print(f'{process2}')
  return f'{final}/{sec}'

# print(lazy_process('hey', 5))

start = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
  lazy_process('GO!!!', 'Finished!!!', 'success!!!', 5)
)
end = time.time()

print(result)
print(f'Process Time: {end - start}')
