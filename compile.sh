git clone https://github.com/xxchaosxx210/DriverApp.git
mv -f ./DriverApp/*.* ./
rm -rf ./DriverApp
echo Compiling APK...
buildozer -v android debug
echo Removing previous APK...
adb uninstall org.taxicompany.taxicompany
echo Installing APK to device...
adb install ./bin/*.apk
echo Cearing logs
adb logcat -c
echo Launching APK...
adb shell monkey -p org.taxicompany.taxicompany -c android.intent.category.LAUNCHER 1
echo Running logger
adb logcat "python:I" "*:S"

