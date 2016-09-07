toggle = 0
#MaxThreadsPerHotkey 2
SetKeyDelay, 0, 30

global originalPB := "", originalMM := "", originalEM := "", originalSE := ""

FileRead, Contents, C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\60-419 Experimental Game Design\powerball.txt
if not ErrorLevel  ; Successfully loaded.
{
    originalPB := Contents
}
FileRead, Contents, C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\60-419 Experimental Game Design\mega.txt
if not ErrorLevel  ; Successfully loaded.
{
    originalMM := Contents
}
FileRead, Contents, C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\60-419 Experimental Game Design\euro.txt
if not ErrorLevel  ; Successfully loaded.
{
    originalEM := Contents
}
FileRead, Contents, C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\60-419 Experimental Game Design\enalotto.txt
if not ErrorLevel  ; Successfully loaded.
{
    originalSE := Contents
}

global powerballNums := originalPB, megaMillionNums := originalMM, euroMillionNums := originalEM, superEnalottoNums := originalSE
global time := 0

global powerDisplay := "", megaDisplay := "", euroDisplay := "", enalottoDisplay := ""
global powerCount := 6, megaCount := 6, euroCount := 6, enalottoCount := 8


F8::
    Toggle := !Toggle
     While Toggle{
        ticketString := powerDisplay . getNextTicket(1, powerCount) . "`r`n" . megaDisplay . getNextTicket(2, megaCount) . "`r`n" . euroDisplay . getNextTicket(3, euroCount) . "`r`n" . enalottoDisplay . getNextTicket(4, enalottoCount)
        file := FileOpen("C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\60-419 Experimental Game Design\currentNumbers.txt", "w")
        file.Write(ticketString)
        file.Close()

        powerDisplay := powerDisplay . getNextButton(1)
        powerCount -= 1
        megaDisplay := megaDisplay . getNextButton(2)
        megaCount -= 1
        euroDisplay := euroDisplay . getNextButton(3)
        euroCount -= 1
        enalottoDisplay := enalottoDisplay . getNextButton(4)
        enalottoCount -= 1

        if powerCount < 0
        {
            powerCount := 6
            powerDisplay := ""
        }
        if megaCount < 0
        {
            megaCount := 6
            megaDisplay := ""
        }
        if euroCount < 0
        {
            euroCount := 6
            euroDisplay := ""
        }
        if enalottoCount < 0
        {
            enalottoCount := 8
            enalottoDisplay := ""
        }

        input1 := getNextInput(1)
        Send {%input1% down}
        input2 := getNextInput(2)
        Send {%input2% down}
        input3 := getNextInput(3)
        Send {%input3% down}
        input4 := getNextInput(4)
        Send {%input4% down}
        Sleep 200

        Send {%input1% up}
        Send {%input2% up}
        Send {%input3% up}
        Send {%input4% up}

        ticketString := powerDisplay . getNextTicket(1, powerCount) . "`r`n" . megaDisplay . getNextTicket(2, megaCount) . "`r`n" . euroDisplay . getNextTicket(3, euroCount) . "`r`n" . enalottoDisplay . getNextTicket(4, enalottoCount)
        file := FileOpen("C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\60-419 Experimental Game Design\currentNumbers.txt", "w")
        file.Write(ticketString)
        file.Close()

        Sleep 100
    }
return

F1::
    ticketString := powerDisplay . getNextTicket(1, powerCount) . "`r`n" . megaDisplay . getNextTicket(2, megaCount) . "`r`n" . euroDisplay . getNextTicket(3, euroCount) . "`r`n" . enalottoDisplay . getNextTicket(4, enalottoCount)
    powerDisplay = getNextButton(1)
    powerCount -= 1
    if powerCount == 0
        powerCount := 6
        powerDisplay := ""
    Msgbox, %ticketString%
    Msgbox, %powerballNums%


    file := FileOpen("C:\Users\Roger Liu\Documents\CMU\Senior Year\Fall Semester\60-419 Experimental Game Design\currentNumbers.txt", "w")
    TestString := "10 10 10 10 a"
    file.Write(TestString)
    file.Close()
    
getNextInput(playerNumber) {
    if (powerballNums == "")
        powerballNums := originalPB
    if (megaMillionNums == "")
        megaMillionNums := originalMM
    if (euroMillionNums == "")
        euroMillionNums := originalEM
    if (superEnalottoNums == "")
        superEnalottoNums := originalSE

    delim := " "
    if playerNumber = 1
    {
        StringGetPos, pos, powerballNums, %delim%
        number := SubStr(powerballNums, 1, pos)
        StringTrimLeft, powerballNums, powerballNums, pos+1

        number := Mod(number, 6)
        if(number = 0) 
            number = 1
        else if(number = 1)
            number = 2
        else if(number = 2) 
            number = 3
        else if(number = 3) 
            number = 4
        else if(number = 4)
            number = 5
        else if(number = 5)
            number = -
    }
    if playerNumber = 2
    {
        StringGetPos, pos, megaMillionNums, %delim%
        number := SubStr(megaMillionNums, 1, pos)
        StringTrimLeft, megaMillionNums, megaMillionNums, pos+1

        number := Mod(number, 6)
        if(number = 0) 
            number = 6
        else if(number = 1)
            number = 7
        else if(number = 2) 
            number = 8
        else if(number = 3) 
            number = 9
        else if(number = 4)
            number = 0
        else if(number = 5)
            number = =
    }
    if playerNumber = 3
    {
        StringGetPos, pos, euroMillionNums, %delim%
        number := SubStr(euroMillionNums, 1, pos)
        StringTrimLeft, euroMillionNums, euroMillionNums, pos+1
        number := Mod(number, 6)

        if(number = 0) 
            number = w
        else if(number = 1)
            number = s
        else if(number = 2) 
            number = a
        else if(number = 3) 
            number = d
        else if(number = 4)
            number = q
        else if(number = 5)
            number = e
    }
    if playerNumber = 4
    {
        StringGetPos, pos, superEnalottoNums, %delim%
        number := SubStr(superEnalottoNums, 1, pos)
        StringTrimLeft, superEnalottoNums, superEnalottoNums, pos+1

        number := Mod(number, 6)
        if(number = 0) 
            number = Up
        else if(number = 1)
            number = Down
        else if(number = 2) 
            number = Left
        else if(number = 3) 
            number = Right
        else if(number = 4)
            number = Space
        else if(number = 5)
            number = z
    }
    
    return %number%
}

getNextTicket(playerNumber, numberCount) {
    if numberCount < 1
        return ""

    delim := " "
    if playerNumber = 1
    {
        StringGetPos, pos, powerballNums, %delim%, l%numberCount%
        number := SubStr(powerballNums, 1, pos)
    }
    if playerNumber = 2
    {
        StringGetPos, pos, megaMillionNums, %delim%, l%numberCount%
        number := SubStr(megaMillionNums, 1, pos)
    }
    if playerNumber = 3
    {
        StringGetPos, pos, euroMillionNums, %delim%, l%numberCount%
        number := SubStr(euroMillionNums, 1, pos)
    }
    if playerNumber = 4
    {
        StringGetPos, pos, superEnalottoNums, %delim%, l%numberCount%
        number := SubStr(superEnalottoNums, 1, pos)
    }
    
    return %number%
}

getNextButton(playerNumber) {
    delim := " "
    if playerNumber = 1
    {
        StringGetPos, pos, powerballNums, %delim%
        number := SubStr(powerballNums, 1, pos)

        number := Mod(number, 6)
    }
    if playerNumber = 2
    {
        StringGetPos, pos, megaMillionNums, %delim%
        number := SubStr(megaMillionNums, 1, pos)

        number := Mod(number, 6)
    }
    if playerNumber = 3
    {
        StringGetPos, pos, euroMillionNums, %delim%
        number := SubStr(euroMillionNums, 1, pos)

        number := Mod(number, 6)
    }
    if playerNumber = 4
    {
        StringGetPos, pos, superEnalottoNums, %delim%
        number := SubStr(superEnalottoNums, 1, pos)

        number := Mod(number, 6)
    }
    
    if(number = 0) 
        number := "up"
    else if(number = 1)
        number := "down"
    else if(number = 2) 
        number := "left"
    else if(number = 3) 
        number := "right"
    else if(number = 4)
        number := "a"
    else if(number = 5)
        number := "b"
    
    number := number . " "

    return %number%
}