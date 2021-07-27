# Linuxにおけるc言語開発環境の構築


## Linuxにおける開発環境

LinuxでC言語を実行するには、プログラムをコンパイル（翻訳）するgccと呼ばれるコンパイラが必要。

## gccのインストール

### Debian(ubuntu, LinuxMint...)

Debianベースのディストリビューションでは、パッケージ管理ツール(apt)を使ってインストールする。
<br>管理者権限が必要となるので、sudoコマンドが必要となる。

```
$ sudo apt install gcc
```

### RedHat(centos)
centosではパッケージ管理ツール(yum)を使ってgccをインストールする。
<br>管理者権限が必要となるので、sudoコマンドが必要となる。

```
# sudo yum install gcc
```

## 開発環境のバージョン確認
gccのインストールが完了したら、以下のコマンドで確認をする。(今回はubuntuで実行)

```
$ gcc --vertion
gcc(Ubuntu9.3.0-17ubuntu1~20.04) 9.3.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

表示から、gcc(9.3.0)がインストールされていることがわかる。


