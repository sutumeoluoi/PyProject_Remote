''' NOTE: from hal
tmpdir: <class 'py._path.local.LocalPath'>, not a string
tmpdir_factory:  <_pytest.tmpdir.TempdirFactory object>. i.e, it is a class itself.
can't use tmpdir_factory. Need to call tmpdir_factory.mktemp() to create an object tmpdir.
Read doc on py.path of py library
<class 'py._path.local.LocalPath'> need to convert to str. to pass it to open(filename, 'w')
or use it own open/read/write method such as a_file.open('w')
'''
def test_tmpdir(tmpdir):
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join('something.txt')
    print('tmpdir: ', tmpdir)
    print(type(tmpdir))

#    base_tmpdir = tmpdir.getbasetemp()
#    print('base_tmpdir:', base_tmpdir)

    # you can create directories
    a_sub_dir = tmpdir.mkdir('anything')
#    print('sub tmpdir: ', a_sub_dir)

    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else.txt')
#    print('file in sub tmpdir: ', another_file)

    # this write creates 'something.txt'
    a_file.write('contents may settle during shipping')

    # this write creates 'anything/something_else.txt'
    another_file.write('something different')

    # you can read the files as well
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'


def test_tmpdir_factory(tmpdir_factory):
    # you should start with making a directory
    # a_dir acts like the object returned from the tmpdir fixture
    a_dir = tmpdir_factory.mktemp('mydir')

    # hal - is tmpdir_factory also a dir?
#    a_ErrDir = tmpdir_factory.mkdir('SupposeErr')
    print("tmpdir_factory: ", tmpdir_factory)

    # base_temp will be the parent dir of 'mydir'
    # you don't have to use getbasetemp()
    # using it here just to show that it's available
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # the rest of this test looks the same as the 'test_tmpdir()'
    # example except I'm using a_dir instead of tmpdir

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'
