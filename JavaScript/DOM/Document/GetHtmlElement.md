# HTMLの要素情報の取得
- HTMLから要素の情報をJavaScriptに取り込むためのメソッド
- ParentNodeインターフェイスから継承している

## document.querySelector(‘要素名’)
- 指定したセレクタ('要素名')に一致する、文書内で最初の要素ノードを返す
- 指定した要素をHTMLの上から探して行って、最初に見つけたものをscriptに取り込む

```HTML
<script>
  const button = document.querySelector('button'); //最初のbutton要素をscriptに取り込む
  const li = document.querySelector('li'); //最初のli要素をscriptに取り込む
</script>

<ul>
  <li>ボタン１<button>１</button></li>　<!-- 取り込まれたのはこの行のbutton・li要素だけ-->
  <li>ボタン２<button>２</button></li>
  <li>ボタン３<button>３</button></li>
</ul>  
```

## document.querySelectorAll(‘要素名’)
- 指定したセレクタ('要素名')に一致する、文書内のすべての要素ノードのリストを返す
- 指定した要素をHTML全体から全部探して配列に入れてくれる

```HTML
<script>
  const button = document.querySelectorAll('button'); //全てのbutton要素をscriptに取り込む
  const li = document.querySelectorAll('li'); //全てのli要素をscriptに取り込む
</script>

<ul>
  <li>ボタン１<button>１</button></li>　<!-- この行のbutton・li要素がscriptに取り込まれた-->
  <li>ボタン２<button>２</button></li>　<!-- この行のbutton・li要素がscriptに取り込まれた-->
  <li>ボタン３<button>３</button></li>　<!-- この行のbutton・li要素がscriptに取り込まれた-->
</ul>  
```

## document.getElementById(String id)
- 特定の id を持つ要素へのオブジェクト参照を返す

```HTML
<script>
  const button-2 = document.getElementById('button-2'); //idがbutton-2であるbutton要素が取り込まれた
</script>

<ul>
  <li>ボタン１<button id="button-1">１</button></li>　  
  <li>ボタン２<button id="button-2">２</button></li> <!-- この行のbutton要素がscriptに取り込まれた-->
  <li>ボタン３<button id="button-3">３</button></li>
</ul>  
```

## document.getElementByClassName('string class')
- 特定のclassを持つ要素へのオブジェクト参照を返す

```HTML
<script>
  const button-list = document.getElementByClassName('button-list'); //classがbutton-listである要素が取り込まれた
</script>

<ul>
  <li>ボタン１<button >１</button></li>　  
  <li>ボタン２<button class="button-list">２</button></li> <!-- この行のbutton要素がscriptに取り込まれた-->
  <li>ボタン３<button class="button-list">３</button></li> <!-- この行のbutton要素がscriptに取り込まれた-->
</ul>  
```


id は HTML全体の中で必ず重複しないユニークな名前を付ける必要がある
<br>button = document.querySelector(‘#id’)
<br>button = document.getElementById(‘id’)

classはHTMLの中に同じ名前が何個あっても問題ない
<br>複数存在する前提なので、配列で帰ってくる
<br>button = document.querySelectorALL(‘.class’)
<br>button = document.getElementByClassName(‘class’)

## 参考
- [MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/API/Document)
