# from os import getenv
#
# import pytest
#
# from core.db.db import DB
# from core.utils.helpers import get_settings
#
# settings_config = {}
# oracle_session = DB()
# postgresql_session = DB()
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionstart():
#     global settings_config, oracle_session, postgresql_session
#     settings_config = get_settings(environment=getenv('environment'))
#     if getenv('DB_POSTGRESQL_USER') != '' and getenv('DB_POSTGRESQL_PASSWORD') != '':
#         postgresql_session = DB().create_session(environment=settings_config, name='POSTGRESQL')
#     # if getenv('DB_ORACLE_USER') != '' and getenv('DB_ORACLE_PASSWORD') != '':
#     #     oracle_session = DB().create_session(environment=settings_config, name='ORACLE')
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish():
#     if getenv('DB_POSTGRESQL_USER') != '' and getenv('DB_POSTGRESQL_PASSWORD') != '':
#         oracle_session.close()
#     # if getenv('DB_ORACLE_USER') != '' and getenv('DB_ORACLE_PASSWORD') != '':
#     #     postgresql_session.close()
