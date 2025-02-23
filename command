Sub RunTypeCommandAndSaveOutput()
    Dim folderPath As String
    Dim outputPath As String
    Dim command As String
    Dim result As Integer

    ' コマンドを実行するフォルダのパスを指定してください
    folderPath = "C:\Your\Folder\Path\Here"
    
    ' 結果を保存するテキストファイルのパスを指定してください
    outputPath = "C:\Your\Folder\Path\Here\all.txt"
    
    ' コマンドを作成
    command = "cmd.exe /c type """ & folderPath & "*.csv"" > """ & outputPath & """"
    
    ' コマンドを実行
    result = Shell(command, vbNormalFocus)
    
    ' 実行結果の確認（エラーハンドリングを追加することもできます）
    If result = 0 Then
        MsgBox "コマンドの実行に失敗しました。", vbExclamation
    Else
        MsgBox "コマンドが正常に実行されました。", vbInformation
    End If
End Sub
