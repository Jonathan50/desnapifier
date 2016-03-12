# Copyright (C) 2016 Jeandre Kruger
#
# This file is part of desnapifier.
#
# desnapifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# desnapifier is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with desnapifier.  If not, see <http://www.gnu.org/licenses/>.

import os, zipfile
from desnapifier import project

def test_is_zipfile():
    test_file = open("test_is_zipfile.xml", "w")
    test_file.write("""<project name="test" app="Snap! 4.0, http://snap.berkeley.edu" version="1"><notes></notes><thumbnail></thumbnail><stage name="Stage" width="480" height="360" costume="0" tempo="60" threadsafe="false" lines="round" codify="false" inheritance="false" scheduled="false" id="1"><pentrails></pentrails><costumes><list id="2"></list></costumes><sounds><list id="3"></list></sounds><variables></variables><blocks></blocks><scripts></scripts><sprites><sprite name="Sprite" idx="1" x="0" y="0" heading="90" scale="1" rotation="1" draggable="true" costume="0" color="80,80,80" pen="tip" id="8"><costumes><list id="9"></list></costumes><sounds><list id="10"></list></sounds><variables></variables><blocks></blocks><scripts></scripts></sprite></sprites></stage><hidden></hidden><headers></headers><code></code><blocks></blocks><variables></variables></project>""")
    test_file.close()

    project.convert_project("test_is_zipfile.xml", "test_is_zipfile.sb2")

    assert zipfile.is_zipfile("test_is_zipfile.sb2")

    os.remove("test_is_zipfile.xml")
    os.remove("test_is_zipfile.sb2")
