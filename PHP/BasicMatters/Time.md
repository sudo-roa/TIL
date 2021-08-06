# 時間に関する表示

PHPにおける時間に関する表示方法について

## タイムゾーンに関して
php.ini内にタイムゾーンに関する設定の記述がある

```
#日本の時間に変更される
date.timezone=Asia/Tokyo
#以下の記述方法でもよい
date_default_timezone_set('Asia/Tokyo');
```
タイムゾーン一覧は参考内のリンクから

## date()
ファンクションによって日付/時刻を書式化する(手続き型)
```
date('s');
date('d');
```


## DateTime()
オブジェクトによって日付/時刻を書式化する(オブジェクト指向)

```
$today = new DateTime();
print($today->format('G時 i分 s秒'));
```


## 参考
- [タイムゾーン](https://www.php.net/manual/ja/timezones.php)
- [Date/Time_format](https://www.php.net/manual/ja/datetime.format.php)
- [date()](https://www.php.net/manual/ja/function.date.php)
- [DateTime()](https://www.php.net/manual/ja/class.datetime.php)
