import os, zipfile, json
from desnapifier import project

notes = "Test project notes"

def test_projectnotes():
    test_file = open("test_projectnotes.xml", "w")
    test_file.write("""<project name="test" app="Snap! 4.0, http://snap.berkeley.edu" version="1"><notes>%s</notes><thumbnail></thumbnail><stage name="Stage" width="480" height="360" costume="0" tempo="60" threadsafe="false" lines="round" codify="false" inheritance="false" scheduled="false" id="1"><pentrails></pentrails><costumes><list id="2"></list></costumes><sounds><list id="3"></list></sounds><variables></variables><blocks></blocks><scripts></scripts><sprites><sprite name="Sprite" idx="1" x="0" y="0" heading="90" scale="1" rotation="1" draggable="true" costume="0" color="80,80,80" pen="tip" id="8"><costumes><list id="9"></list></costumes><sounds><list id="10"></list></sounds><variables></variables><blocks></blocks><scripts></scripts></sprite></sprites></stage><hidden></hidden><headers></headers><code></code><blocks></blocks><variables></variables></project>""" % notes)
    test_file.close()

    project.convert_project("test_projectnotes.xml", "test_projectnotes.sb2")

    z = zipfile.ZipFile("test_projectnotes.sb2")

    p = z.open("project.json", "r")
    project_json = json.loads(p.read())

    assert project_json["info"]["comment"] == notes

    z.close()

    os.remove("test_projectnotes.xml")
    os.remove("test_projectnotes.sb2")
