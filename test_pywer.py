from pywer import package_to_uri


def test_package_to_uri():
    assert package_to_uri("git://github.com/user/package.git") == "git://github.com/user/package.git"
