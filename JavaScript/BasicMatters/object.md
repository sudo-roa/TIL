# オブジェクト
JavaScriptにおけるオブジェクト

## 概要
- プロパティやキーなどと値をペアで管理する入れ物
- オブジェクトのプロパティに格納された関数はメソッドという
- 中身の定義方法
  - 名前: 値
  - 名前: 関数
  - 名前: オブジェクト
- プロパティへのアクセス方法は二種類
  - ドット記法 `obj.名前`
  - ブラケット記法 `obj['名前']`

## 一般的な定義の仕方
オブジェクトは、{}内に中身を定義していく
<br>プロパティには、値、関数、オブジェクトを定義できる
```
let obj = {
  property1: 'hoge',
  property2: function(){},
  property3:{
    a: 'huga'
  }
}
```

- オブジェクトの定義例
(オブジェクトの出力にはプロパティへのアクセスを使う)
```
let obj = {
    prop1: 'value1',
    prop2: 'value2',
    prop3: function(){
        console.log('value3')
    },
    prop4: {
        prop5: 'value5'
    }
}
console.log(obj.prop1);
//value1
console.log(obj.prop2);
//value2
obj.prop3();
//value3
console.log(obj.prop4.prop5);
//value5
```

- オブジェクトの内部をまとめて出力できる
`console.log(obj)`

## その他の定義方法


- オブジェクトのプロパティ外からの定義
```
obj.prop6 = 'value6';
console.log(obj.prop6);
//value6
```

## 参考
- [オブジェクト](https://developer.mozilla.org/ja/docs/Learn/JavaScript/Objects)
