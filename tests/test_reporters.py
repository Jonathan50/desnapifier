import os
from desnapifier import project

def test_reporters():
    project.convert_project("tests/test_reporters.xml", "test_reporters.sb2")
    #os.remove("test_reporters.sb2")
