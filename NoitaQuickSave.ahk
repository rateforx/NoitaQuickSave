#singleInstance force

#IfWinActive, ahk_exe noita.exe

    F5::
        WinGet, executablePath, ProcessPath, ahk_exe noita.exe
        executableDir := RTrim(executablePath, "noita.exe")
        Send, !{F4}
        Process, WaitClose, noita.exe
        EnvGet, saveDir, AppData
        saveDir := StrReplace(saveDir, "Roaming", "LocalLow\Nolla_Games_Noita\save00")
        FileCopyDir, %saveDir%, .\save00, true
        Run, %executablePath%, %executableDir%
        Return

    F9::
        WinGet, executablePath, ProcessPath, ahk_exe noita.exe
        executableDir := RTrim(executablePath, "noita.exe")
        Process, Close, noita.exe
        EnvGet, saveDir, AppData
        saveDir := StrReplace(saveDir, "Roaming", "LocalLow\Nolla_Games_Noita\save00")
        FileCopyDir, save00, %saveDir%, true
        Run, %executablePath%, %executableDir%
        Return
