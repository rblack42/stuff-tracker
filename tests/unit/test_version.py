import os

from catalog.__version__ import get_version


def test_version():
    """
    GIVEN: An environment variable holds the current version
    WHEN: user requests version from API
    THEN: resomsematches environment variable
    """
    version = os.environ["STAPIVER"]
    assert get_version() == version
