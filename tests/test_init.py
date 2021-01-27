from lambda_run import wrap_handler

py = lambda payload: {'lambdaRun': ['py', payload]}
sh = lambda payload: {'lambdaRun': ['sh', payload]}

#lambda_handler = wrap_handler(lambda ev, ctx: 'OK')

@wrap_handler
def lambda_handler(ev, ctx):
    return 'OK'


def test_event():
    rsp = lambda_handler({'some': 'event'}, None)
    assert rsp == 'OK'


def test_run_py():
    rsp = lambda_handler(py("""
print(123)
print('abc')
print("xyz")
"""), None)
    assert rsp == (0, '123\nabc\nxyz')


def test_run_sh():
    rsp = lambda_handler(sh("""
ls -1
ls -1 /
"""), None)
    stdout = rsp[1]
    assert 'setup.py' in stdout
    assert 'root' in stdout
