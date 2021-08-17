# Number
Numberに関して

## 概要
プリミティブラッパーオブジェクトで、数値表現や数値操作に使用

## Number()
文字列やその他の値をNumber型に変換する（変換できない場合はNaNを返す）

```
example = Number('4649');
console.log(example);
> 4649

example = Number('hoge');
console.log(example);
> NaN
```
