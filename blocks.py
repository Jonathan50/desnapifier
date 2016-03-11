# Copyright (C) 2016 Jeandre Kruger
#
# This file is part of screchifier.
#
# screchifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# screchifier is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with screchifier.  If not, see <http://www.gnu.org/licenses/>.

blocks = {
    # motion
    "forward":    [ "forward:", 1 ],

    # looks
    "doSayFor":   [ "say:duration:elapsed:from:", 2 ],
    "doThinkFor": [ "think:duration:elapsed:from:", 2 ],

    # control/events
    "receiveGo":  [ "whenGreenFlag", 0 ],
    "doWait":     [ "wait:elapsed:from:", 1 ]
}
