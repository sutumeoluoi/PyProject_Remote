"""Some tests that use temp data files."""
import json


def test_brian_in_portland(author_file_json):
    """A test that uses a data file."""
#    with author_file_json.open() as f:
# or
#Read doc on py.path of py library
#read conftest.py, ..\test_tmpdir.py
#author_file_json is <class 'py._path.local.LocalPath'>. to pass it to open(filename, 'w') need to convert it to str
# as below
    with open(str(author_file_json)) as f: #default open() mode is 'r'
        authors = json.load(f)
    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    """Same file is used for both tests."""
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0
