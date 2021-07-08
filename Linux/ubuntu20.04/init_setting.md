# init_setting

## OSインストール後によくする設定（ろあ版）

手元のパソコンのOSをインストールした後、VM等でOSをインストールした後

```
$ sudo apt update
$ sudo apt upgrade

$ sudo apt install openssh-server
$ sudo systemctl status sshd
$ sudo systemctl is-enable sshd
$ sudo systemctl enable sshd
$ sudo apt install net-tools
$ sudo apt install vim
$ sudo apt install mlocate
$ sudo apt install screen
$ sudo apt install httpdirfs apache2
$ sudo systemctl status apache2
$ sudo systemctl is-enabled apache2
$ sudo systemctl disable apache2
$ sudo systemctl is-enabled apache2

VScode download file
$ sudo apt install ./code_1.57.0-1623259737_amd64.deb
$ code -v

$ sudo apt install git
$ git --version

VirtualBox download file
$ sudo apt install ./virtualbox-6.1_6.1.22-144080~Ubuntu~eoan_amd64.deb
$ VBoxManage --version
$ sudo gpasswd -a YOUR_USERNAME vboxusers

$ sudo apt install gparted

use remote desktop by vnc-server
$ gsettings set org.gnome.Vino require-encryption false
$ sudo ufw status


$ sudo apt install plantuml
$ sudo apt install openjdk-16-jre
$ sudo apt install doxygen
$ sudo apt install tree
$ sudo apt install traceroute

```


さくらVPSの場合
```
# 最初に登録されているユーザはubuntu20.04ならubuntu
# 新たなユーザを作成して、sudoグループに入れたのち、初期ユーザは消去するべき（セキュリティ上）
$ sudo adduser your-username
$ gpasswd -a user_name sudo
$ sudo userdel -r init-username

# /etc/ssh/sshd_configを変更
$ cp sshddif_config sshd_config.origin
$ vim ssh_config
    PermitRootLogin no
$ diff sshd_config.origin sshd_iconfig
> 
> #   add 20210704
>     PermitRootLogin no
> 
$ sudo shutdown -r now
```
