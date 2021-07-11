# init_setting

自身がOSインストール後に行う設定について

## OSインストール後によくする設定（ろあ版）

手元のパソコンのOSをインストールした後、VM等でOSをインストールした後

```
#インストールしているパッケージの更新
$ sudo apt update
$ sudo apt upgrade

#新たに追加
#openssh-server
$ sudo apt install openssh-server
$ sudo systemctl status sshd
$ sudo systemctl is-enable sshd
$ sudo systemctl enable sshd

#ifconfig
$ sudo apt install net-tools

# vim
$ sudo apt install vim

#locate
$ sudo apt install mlocate

#screen
$ sudo apt install screen

#apache
$ sudo apt install httpdirfs apache2
$ sudo systemctl status apache2
$ sudo systemctl is-enabled apache2
$ sudo systemctl disable apache2
$ sudo systemctl is-enabled apache2

#VScode
$ sudo apt install ./code_1.57.0-1623259737_amd64.deb
$ code -v

#git
$ sudo apt install git
$ git --version

#VirtualBox
$ sudo apt install ./virtualbox-6.1_6.1.22-144080~Ubuntu~eoan_amd64.deb
$ VBoxManage --version
$ sudo gpasswd -a YOUR_USERNAME vboxusers

#gparted
$ sudo apt install gparted

#remote desktop by vnc-server
$ gsettings set org.gnome.Vino require-encryption false
$ sudo ufw status

#plantuml
$ sudo apt install plantuml
$ sudo apt install openjdk-16-jre
$ sudo apt install doxygen

#tree
$ sudo apt install tree

#traceroute
$ sudo apt install traceroute

```


## さくらVPSの場合
ユーザ名をデフォルトから変更し、鍵認証をしたクライアントしかssh接続できないようにする。
<br>さくらVPSで最初に登録されているユーザはubuntu20.04ならubuntu
<br>新たなユーザを作成して、sudoグループに入れたのち、初期ユーザは消去するべき（セキュリティ上）

```
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

<br>sshkeyの追加
<br>まず下記のどちらかを実行

```
#.sshがない
$ install -m 0700 -d ~/.ssh 
#.sshがある
$ chmod 700 .ssh
```

<br>公開鍵の内容をコピペ

```
$ cd ~/.ssh
$ vim authorized_keys　 
$ chmod 600 authorized_keys 
```

<br>パスワード認証の無効化

```
# /etc/ssh/sshd_configを変更
$ vim ssh_config
    PasswordAuthentication no
$ diff sshd_config.origin sshd_iconfig
> # add 20210711
> PasswordAuthentication no
> 
> # add 20210704
> PermitRootLogin no

$ sudo systemctl restart sshd
```

<br>ファイアウォールの設定

```
$ sudo ufw status
status: inactive
$ sudo ufw enable

$ sudo ufw allow 22
Skipping adding existing rule
Skipping adding existing rule (v6)
$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere                  
22 (v6)                    ALLOW       Anywhere (v6) 
```
