# -*- coding: utf-8 -*-
from sphinxcontrib.httpexample.parsers import parse_request
from sphinxcontrib.httpexample.builders import build_curl_command
# from sphinxcontrib.httpexample.builders import build_httpie_command
# from sphinxcontrib.httpexample.builders import build_requests_command

from .test_parser import fixture

assert fixture


def test_curl_001(fixture):
    request = parse_request(fixture['001']['request'])
    command = build_curl_command(request)
    assert command == (
        'curl '
        '-i '
        '-X POST http://localhost:8080/Plone/folder '
        '-H "Accept: application/json" '
        '-H "Content-Type: application/json" '
        '--data-raw \'{"@type": "Document", "title": "My Document"}\' '
        '--user admin:admin '
    ).strip()


# def test_httpie_001(fixture):
#     request = parse_request(fixture['001']['request'])
#     command = build_httpie_command(request)
#     assert command == (
#         'http '
#         '-a admin:admin POST '
#         'http://localhost:8080/Plone/folder '
#         '\\@type=Document title=My Document Accept:application/json'
#     )
#
#
# def test_requests_001(fixture):
#     request = parse_request(fixture['001']['request'])
#     command = build_requests_command(request)
#     assert command == (
#         "requests.post("
#         "'http://localhost:8080/Plone/folder', "
#         "auth=('admin', 'admin'), "
#         "headers={'Accept': 'application/json'}, "
#         "json={'@type': 'Document', 'title': 'My Document'}"
#         ")"
#     )
