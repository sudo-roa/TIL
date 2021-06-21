#!/bin/sh

#check git account
name=`git config user.name`
echo '現在のアカウントは'"$name"'です。'

#select operation
while
	echo \
'githubリポジトリをクローンしますか？
1) yes
2) no
3) changeUsername' 

read -p '> ' cmd 
do
	case $cmd in
		1)
			echo 'クローンに移行します'
			break;;
		2)
			echo 'クローンを中止します'
			exit 0;;
		3)
			echo 'gitのアカウントを変更します'
			read -p 'user name > ' uname
			read -p 'user email > ' uemail
			git config --global user.name ""$uname""
			git config --global user.email ""$uemail""
			git config user.name
			git config user.email
			echo '変更しました';;
	esac
done

#input owner name and repository name of the repository you want to clone 
read -p 'user name > ' user
read -p 'repository name > ' repository
git clone https://github.com/"$user"/"$repository".git
