Name: backApp
Version: 1.0
Release: 1%{?dist}
Summary: this app uses a python script to backup files in a /backup directory
License: michael
BuildRequires: python3

%description 

%build

%install
mkdir -p %{buildroot}/opt/backup_util
install -m 755 /home/michael/Desktop/portfolio/backApp/app/backup_script.py %{buildroot}/opt/backup_util/
install -m 644 /home/michael/Desktop/portfolio/backApp/config/backup_util.conf %{buildroot}/opt/backup_util/


%files
/opt/backup_util/backup_script.py
/opt/backup_util/backup_util.conf

%post
echo "installation succeeded"

%changelog
* Tue Feb 20 2024 Michael Levy 1.0
- First version

