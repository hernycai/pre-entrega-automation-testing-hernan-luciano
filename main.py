import pytest
import sys

if __name__ == "__main__":
    args = [
        "test/",
        "-v",
        "--html=report.html",
        "--self-contained-html"
    ]
    sys.exit(pytest.main(args))