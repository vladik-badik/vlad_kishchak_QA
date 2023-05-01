def skip(condition, reason):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print(reason)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@skip(condition=True, reason="Skipped because of JIRA-123 bug")
def test_two_plus_two_failure():
    assert 2 + 2 == 5
test_two_plus_two_failure()

@skip(condition=False, reason="Function is skipped")
def test_two_plus_two_success():
    print(2+2)

test_two_plus_two_success()