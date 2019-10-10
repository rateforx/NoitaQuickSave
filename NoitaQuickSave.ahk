#singleInstance force

#IfWinActive, ahk_exe noita.exe

F5::
    WinGetPos, , , w, h, ahk_exe noita.exe
    WinGet, executablePath, ProcessPath, ahk_exe noita.exe
    executableDir := RTrim(executablePath, "noita.exe")
    Send, {Esc}
    x := 0.5 * w
    y := 0.8625 * h
    Click, %x%, %y%
    Process, WaitClose, noita.exe
    RunWait, ./venv/Scripts/python.exe quickSave.py
    Run, %executablePath%, %executableDir%
    Return

F9::
    WinGet, executablePath, ProcessPath, ahk_exe noita.exe
    executableDir := RTrim(executablePath, "noita.exe")
    Process, Close, noita.exe
    RunWait, ./venv/Scripts/python.exe quickLoad.py
    Run, %executablePath%, %executableDir%
    Return
