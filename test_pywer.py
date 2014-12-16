from pywer import package_to_uri


def test_package_to_uri_git_proto():
    assert package_to_uri("git://github.com/user/package.git") == "git://github.com/user/package.git"


def test_package_to_uri_https():
    assert package_to_uri("https://example.com/script.js") == "https://example.com/script.js"


def test_package_to_uri_http():
    assert package_to_uri("http://example.com/script.js") == "http://example.com/script.js"


def test_package_to_uri_github_shortcut():
    assert package_to_uri("pouet/plop") == "https://github.com/pouet/plop"
