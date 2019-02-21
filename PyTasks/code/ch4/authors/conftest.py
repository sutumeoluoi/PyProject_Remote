"""Demonstrate tmpdir_factory."""

import json
import pytest


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Write some authors to a data file."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    file_ = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file_)))
    print(type(file_))

#Read doc on py.path of py library
#read test_authors.py, ..\test_tmpdir.py
#file_ is <class 'py._path.local.LocalPath'>. to pass it to open(filename, 'w') need to convert it to str
# as open(str(file_), 'w)
    another_dir = tmpdir_factory.mktemp('another')	#also return LocalPath object. Read doc on py.path of py library
    print(type(another_dir))

    with file_.open('w') as f:
#
	#with open(file_, 'w') as f:
        json.dump(python_author_data, f)
    return file_
