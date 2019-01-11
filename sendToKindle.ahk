#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#SingleInstance Force ; Allow only one running instance of script
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
  KeyWait, Control
  #InstallKeybdHook
#InstallMouseHook



Send, o
WinWaitActive, ahk_class CabinetWClass
Send, ^e
Send, type: mobi
Sleep, 1000
Send, {Enter}
Sleep, 1600
Send, {Down 2}
Send, {AppsKey}
Send, {Down 10}
Send, {Enter}
WinWaitActive, ahk_exe SendToKindle.exe, , 20
if ErrorLevel{
	MsgBox, Timed Out
	return
}
else{
	Send, {Enter}
	WinWaitClose, ahk_exe SendToKindle.exe
	Send, {^w}
}

ExitApp