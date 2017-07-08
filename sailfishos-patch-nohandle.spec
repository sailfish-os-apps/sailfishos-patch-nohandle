Name:          sailfishos-patch-nohandle
Version:       0.1
Release:       1
Summary:       No handle
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      sailfish-version >= 2.0.5, patchmanager
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
Removes the handle for the home screen and the launcher.

%files
%defattr(-,root,root,-)
/usr/share/*

%preun
patchmanager -u sailfishos-patch-nohandle

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/patchmanager/patches/sailfishos-patch-nohandle
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
patchmanager -u sailfishos-patch-nohandle
fi
fi

%changelog
* Sat Jul 8 2017 0.1
- First build.
