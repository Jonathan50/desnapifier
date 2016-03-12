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

import kurt

blocks = {
    # motion
    "forward":           [ "forward:", 1, None ],
    "turn":              [ "turnRight:", 1, None ],
    "turnLeft":          [ "turnLeft:",  1, None ],

    # looks
    "doSayFor":          [ "say:duration:elapsed:from:", 2, None ],
    "bubble":            [ "say:", 1, None ],
    "doThinkFor":        [ "think:duration:elapsed:from:", 2, None ],
    "doThink":           [ "think:", 1, None ],
    "show":              [ "show", 0, None ],
    "hide":              [ "hide", 0, None ],

    # control/events
    "receiveGo":         [ "whenGreenFlag", 0, None ],
    "doWait":            [ "wait:elapsed:from:", 1, None ],
    "doIf":              [ "doIf", 2, None ],
    "doIfElse":          [ "doIfElse", 3, None ],

    # operators
    "reportSum":         [ "+", 2, None ],
    "reportDifference":  [ "-", 2, None ],
    "reportProduct":     [ "*", 2, None ],
    "reportQuotient":    [ "/", 2, None ],
    "reportLessThan":    [ "<", 2, None ],
    "reportEquals":      [ "=", 2, None ],
    "reportGreaterThan": [ ">", 2, None ],
    "reportTrue":        [ None, 0, lambda: kurt.Block("=", 1, 1) ],
    "reportFalse":       [ None, 0, lambda: kurt.Block("=", 1, 0) ]
}
