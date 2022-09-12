import os
import requests
from werkzeug.datastructures import FileStorage

url = 'http://127.0.0.1:5000/merge'

# in progress, issue with appending pdf blobs to form data using requests
def test_valid_merge():
    here = os.path.dirname(os.path.abspath(__file__))
    file1 = os.path.join(here, 'test-1.pdf')
    file2 = os.path.join(here, 'test-2.pdf')
    data = {
        'file1':
        FileStorage(
            stream=open(file1, "rb"),
            filename="test-1.pdf",
            content_type="application/pdf",
        ),
        'file2':
        FileStorage(
            stream=open(file2, "rb"),
            filename="test-2.pdf",
            content_type="application/pdf",
        )
    }
    r = requests.post(url, files=data)
    assert r.status_code == 200


def test_invalid_merge():
    r = requests.post(url, files=dict(file1='./test.jpg'))
    assert r.status_code == 400


def test_invalid_merge2():
    r = requests.post(url, files=dict())
    assert r.status_code == 400
