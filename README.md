# pytest-example

Unittest와 pytest를 사용한 Python testcode 작성법

## run
```python
python -m pytest
```

## Unittest
Unittest는 setUp, tearDown 함수를 이용하여 function, class, module 단위로 테스트에 필요한 환경을 설정할 수 있다.

## pytest
pytest는 fixture라는 pytest만의 문법을 이용하여 작성한다. pytest는 `@pytest.fixture(scope="{scope}")` 형식으로 scope를 지정할 수 있다.

## Flask API test
Flask는 `create_app()` 인스턴스 생성 후 `test_client()` 인스턴스를 생성하여 서버를 실행하지 않고도 API 테스트를 진행할 수 있다.
