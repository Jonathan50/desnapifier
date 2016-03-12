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
import scripts

def report_block(snap_block):
    script = []
    args = scripts.get_args(snap_block)
    scripts.check_args("doReport", 1, len(args))
    script.append(kurt.Block("insert:at:ofList:", args[0], 1, "return stack"))
    script.append(kurt.Block("stopScripts", "this script"))
    return script

blocks = {
    # motion
    "forward":                    [ "forward:", 1, None ],
    "turn":                       [ "turnRight:", 1, None ],
    "turnLeft":                   [ "turnLeft:",  1, None ],
    "setHeading":                 [ "heading:", 1, None ],
    "doFaceTowards":              [ "pointTowards:", 1, None ],
    "gotoXY":                     [ "gotoX:y:", 2, None ],
    "doGotoObject":               [ "gotoSpriteOrMouse:", 1, None ],
    "doGlide":                    [ "glideSecs:toX:y:elapsed:from:", 4, None ],
    "changeXPosition":            [ "changeXposBy:", 1, None ],
    "setXPosition":               [ "xpos:", 1, None ],
    "changeYPosition":            [ "changeYposBy:", 1, None ],
    "setYPosition":               [ "ypos:", 1, None ],
    "bounceOffEdge":              [ "bounceOffEdge", 0, None ],
    "xPosition":                  [ "xpos", 0, None ],
    "yPosition":                  [ "ypos", 0, None ],
    "direction":                  [ "heading", 0, None ],

    # looks
    "doSayFor":                   [ "say:duration:elapsed:from:", 2, None ],
    "bubble":                     [ "say:", 1, None ],
    "doThinkFor":                 [ "think:duration:elapsed:from:", 2, None ],
    "doThink":                    [ "think:", 1, None ],
    "show":                       [ "show", 0, None ],
    "hide":                       [ "hide", 0, None ],
    "doSwitchToCostume":          [ "lookLike:", 1, None ],
    "doWearNextCostume":          [ "nextCostume", 0, None ],
    "changeEffect":               [ "changeGraphicEffect:by:", 2, None ],
    "setEffect":                  [ "setGraphicEffect:to:", 2, None ],
    "clearEffects":               [ "filterReset", 0, None ],
    "changeScale":                [ "changeSizeBy:", 1, None ],
    "setScale":                   [ "setSizeTo:", 1, None ],
    "comeToFront":                [ "comeToFront", 0, None ],
    "goBack":                     [ "goBackByLayers:", 1, None ],
    "getCostumeIdx":              [ "costumeIndex", 0, None ],
    "getScale":                   [ "scale", 0, None ],

    # sounds
    "playSound":                  [ "playSound:", 1, None ],
    "doPlaySoundUntilDone":       [ "doPlaySoundAndWait", 1, None ],
    "doStopAllSounds":            [ "stopAllSounds", 0, None ],
    "doRest":                     [ "rest:elapsed:from:", 1, None ],
    "doPlayNote":                 [ "noteOn:duration:elapsed:from:", 2, None ],
    "doChangeTempo":              [ "changeTempoBy:", 1, None ],
    "doSetTempo":                 [ "setTempoTo:", 1, None ],
    "getTempo":                   [ "tempo", 0, None ],

    # pen
    "clear":                      [ "clearPenTrails", 0, None ],
    "doStamp":                    [ "stampCostume", 0, None ],
    "down":                       [ "putPenDown", 0, None ],
    "up":                         [ "putPenUp", 0, None ],
    "setColor":                   [ "penColor:", 1, None ],
    "changeHue":                  [ "changePenHueBy:", 1, None ],
    "setHue":                     [ "setPenHueTo:", 1, None ],
    "changeBrightness":           [ "changePenShadeBy:", 1, None ],
    "setBrightness":              [ "setPenShadeTo:", 1, None ],
    "changeSize":                 [ "changePenSizeBy:", 1, None ],
    "setSize":                    [ "penSize:", 1, None ],

    # control/events
    "receiveGo":                  [ "whenGreenFlag", 0, None ],
    "receiveKey":                 [ "whenKeyPressed", 0, None ],
    "receiveMessage":             [ "whenIReceive", 0, None ],
    "doBroadcast":                [ "broadcast:", 1, None ],
    "doBroadcastAndWait":         [ "doBroadcastAndWait", 0, None ],
    "doWait":                     [ "wait:elapsed:from:", 1, None ],
    "doRepeat":                   [ "doRepeat", 2, None ],
    "doForever":                  [ "doForever", 1, None ],
    "doIf":                       [ "doIf", 2, None ],
    "doIfElse":                   [ "doIfElse", 3, None ],
    "doWaitUntil":                [ "doWaitUntil", 1, None ],
    "doUntil":                    [ "doUntil", 2, None ],
    "doStop":                     [ "stopScripts", 1, None ],
    "receiveOnClone":             [ "whenCloned", 0, None ],
    "createClone":                [ "createCloneOf:", 1, None ],
    "removeClone":                [ "deleteClone", 0, None ],
    "doReport":                   [ None, 1, report_block ],

    # sensing
    "reportTouchingObject":       [ "touching:", 1, None ],
    "reportTouchingColor":        [ "touchingColor:", 1, None ],
    "reportColorIsTouchingColor": [ "color:sees:", 1, None ],
    "reportDistanceTo":           [ "distanceTo:", 1, None ],
    "doAsk":                      [ "doAsk", 1, None ],
    "reportLastAnswer":           [ "answer", 0, None ],
    "reportKeyPressed":           [ "keyPressed:", 1, None ],
    "reportMouseDown":            [ "mousePressed", 0, None ],
    "reportMouseX":               [ "mouseX", 0, None ],
    "reportMouseY":               [ "mouseY", 0, None ],
    "reportTimer":                [ "timer", 0, None ],
    "doResetTimer":               [ "timerReset", 0, None ],
    "reportAttributeOf":          [ "getAttribute:of:", 2, None ],
    "reportDate":                 [ "timeAndDate", 0, None ],

    # operators
    "reportSum":                  [ "+", 2, None ],
    "reportDifference":           [ "-", 2, None ],
    "reportProduct":              [ "*", 2, None ],
    "reportQuotient":             [ "/", 2, None ],
    "reportRandom":               [ "randomFrom:to:", 2, None ],
    "reportLessThan":             [ "<", 2, None ],
    "reportEquals":               [ "=", 2, None ],
    "reportGreaterThan":          [ ">", 2, None ],
    "reportAnd":                  [ "&", 2, None ],
    "reportOr":                   [ "|", 2, None ],
    "reportNot":                  [ "not", 2, None ],
    "reportJoinWords":            [ "concatenate:with:", 2, None ],
    "reportLetter":               [ "letter:of:", 2, None ],
    "reportStringSize":           [ "stringLength:", 1, None ],
    "reportMonadic":              [ "computeFunction:of:", 2, None ],
    "reportTrue":                 [ None, 0, lambda b: [ kurt.Block("=", 1, 1) ] ],
    "reportFalse":                [ None, 0, lambda b: [ kurt.Block("=", 1, 0) ] ],

    # variables
    "doSetVar":                   [ "setVar:to:", 2, None ],
    "doChangeVar":                [ "changeVar:by:", 2, None ],
    "doShowVar":                  [ "showVariable:", 1, None ],
    "doHideVar":                  [ "hideVariable:", 1, None ]
}
