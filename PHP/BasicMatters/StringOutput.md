# 文字列の出力

PHPでの文字列の出力に関して

## 文字列を出力する関数
- print()
  <br>文字列を出力
- echo() 
  <br>1つ以上の文字列を出力
  
<br>※print,echoは厳密には関数ではなく言語構造らしい…

## print()
### 基本的な使い方
- ' もしくわ " で出力する文字列をくくる
- 引数は文字列を生成するあらゆる式を指定することができる
```
print 'hello world';
print "hello world";
print('hello world');
print("hello world");
```

### 1つ以上の文字列を連結する場合
printは引数を一つしかとらないので、.を使って文字列を連結していく。
```
print("hello"."world");
```

### 文字列内で', "を使いたい場合
使いたい記号で括らないか、エスケープシーケンスを使う
```
print("これで'が出力できる");
print('これで"が出力できる');
print('これでも\'が出力できる');
print("これでも\"が出力できる");
```

## echo()
### 基本的な使い方
- ' もしくわ " で出力する文字列をくくる
- 引数は文字列を生成するあらゆる式を指定することができる
```
echo 'hello world';
echo "hello world";
echo('hello world');
echo("hello world");
```
### 1つ以上の文字列を連結する
echoは1つ以上の引数をとるので、カンマ区切りで出力したい文字列を引数として並べることで連結する
```
echo "hello", "world";
```
### 文字列内で', "を使いたい場合
使いたい記号で括らないか、エスケープシーケンスを使う
```
echo("これで'が出力できる");
echo('これで"が出力できる');
echo('これでも\'が出力できる');
echo("これでも\"が出力できる");
```
## 参考
- [print()](https://www.php.net/manual/ja/function.print.php)
- [echo()](https://www.php.net/manual/ja/function.echo.php)
