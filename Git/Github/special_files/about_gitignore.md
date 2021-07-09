# about_gitignore.md
.gitignoreファイルがどのような役割を持つか

## .gitignore ファイルとは

Gitが無視すべきファイルを設定できる。
<br>無視すべきファイルというのは、例えば、作業用ディレクトリに生成されやすいファイルで、オブジェクトファイル、スクリプトからの出力等である。

## .gitignoreの例

```# Prerequisites
*.d

# Object files
*.o
*.ko
*.obj
*.elf

# Linker output
*.ilk
*.map
*.exp

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

# Debug files
*.dSYM/
*.su
*.idb
*.pdb

# Kernel Module Compile Results
*.mod*
*.cmd
.tmp_versions/
modules.order
Module.symvers
Mkfile.old
dkms.conf
```
<br>(C言語)

## .gitignoreの大文字小文字の区別

```
リポジトリ名/.git/config内の設定
ignorecase = true  
-> 大文字小文字を区別しない
ignorecase = false
-> 大文字小文字を区別する
```

## 各リポジトリ、フォルダ外からの無視設定
localのPCでgitを利用していると、ユーザのホームディレクトリ下に.gitignore_grobalというファイルが生成されていることがある。
<br>これは、どのリポジトリにも共通して無視させたいファイルを設定できる。

### Macにおける.gitignore_grobal

```
% cat ~/.gitignore_grobal
*~
.DS_Store
```

これは、MacOSでのFinder(windowsでいうエクスプローラ)の設定などを格納する一時ファイルであり、gitのリポジトリにプッシュする必要のないファイルであるので、これを一括で無視する設定になっている。

### core.excludesfileについて
ホームディレクトリ下には.gitconfigファイルが存在し、その中には
```
[core]
       excludesfile = /Users/hiroaki/.gitignore_global
```
という記述がある。
<br>これによって、.gitignore_grobalを参照している。

## 参考

[git documentation](https://git-scm.com/docs)
