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

import sys, pkg_resources
import project

if "--version" in sys.argv or "-v" in sys.argv:
    print "desnapifier version 0.7.0"
    print
    print "desnapifier is free software: you can redistribute it and/or modify"
    print "it under the terms of the GNU General Public License as published by"
    print "the Free Software Foundation, either version 3 of the License, or"
    print "(at your option) any later version."
    print
    print "desnapifier is distributed in the hope that it will be useful,"
    print "but WITHOUT ANY WARRANTY; without even the implied warranty of"
    print "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
    print "GNU General Public License for more details."
    print
    print "You should have received a copy of the GNU General Public License"
    print "along with desnapifier.  If not, see <http://www.gnu.org/licenses/>."
    sys.exit()

if len(sys.argv) < 3:
    sys.stderr.write("Usage: python -m desnapifier infile.xml outfile.sb2\n")
    sys.exit()

project.convert_project(sys.argv[1], sys.argv[2])
