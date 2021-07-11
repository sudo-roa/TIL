# CreateShellScript

シェルスクリプトの作成のについて

## 1 シェルの絶対パスの宣言

ファイルの先頭（一番上の行）にはシェバンと呼ばれるものを記載することで、
<br>起動してスクリプトを読み込むインタプリタを指定する

```
$ vi hello
-------------------------------------------
#!/bin/bash
echo 'Hello World'
-------------------------------------------
```
<br>#!/bin/bashの意味
<br>(/bin/bashは絶対パス（echo $SHELL）)
<br>./helloとしたとき
<br>システム内部では、「/bin/bash ./hello」というコマンドが実行されている
<br>
<br>/bin/sh以外にも...

<br>↓Perlのスクリプト
```
#!/usr/bin/perl
print "Hello World\n"
```
<br>↓awkのスクリプト(-fのオプションが必要)
```
#!/usr/bin/awk -f BEGIN {
  print "Hello World"
}
```

<br>↓tail -lを実行するスクリプトであることを明示
```
#!/usr/bin/tail -l     Hello World
```

<br>#!にはバイナリファイルを指定すれば実行される


## 2 実行ファイルとして実行する場合の処理（権限付与）

```
$ ls -l
-rw-rw-r-- 1 user-name 32 Jun 14 11:06 hello
$ chmod +x hello
$ ls -l
-rwxrwxr-x 1 user-name 32 Jun 14 11:06 hello
$ ./hello
Hello World
```

