# coding: UTF-8

import asyncio

async def lazy_process(name, sec):
  print(f'start {name}')
  await asyncio.sleep(sec)
  print(f'end {name}')
  return f'{name}/{sec}'

print(lazy_process('hey', 5))
