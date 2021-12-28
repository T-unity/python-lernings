# coding: UTF-8

context = 'グローバル'

def check_scope_parent():
  context = '親の関数'

  def check_scope_child():
    # context = '子の関数'
    return context

  return check_scope_child()

print(check_scope_parent())
