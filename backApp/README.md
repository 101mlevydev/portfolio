#welcme to my backApp!

#this is an app that backs up files to your request.

#after installing via dnf, you should go into the /opt/backup_util and configure the configuration file to your needs. each line should have the full path for the file you want to backup. then run the python script.

#the file backs up /etc/hosts and /etc/resolv.conf by default

#instructions for RPM installation
#install the relevant packages
build the rpm

sudo dnf install rpm-build
sudo dnf install createrepo

cd /path/to/directory/
rpmbuild -bb backup_app.spec
 
#Create a local repository, copy the RPM package to the repository directory, and create repository metadata

sudo mkdir /myrepo
cd ~
cd rpmbuild/RPMS/x86_64/
cp PythonBackupApp-1.0-1.fc39.x86_64.rpm  /myrepo/
sudo createrepo /myrepo/

#Create a YUM repository configuration file for the local repository.

cd /etc/yum.repos.d/
sudo vim myrepo.repo

#install the package backApp from local repo
sudo dnf install backApp
