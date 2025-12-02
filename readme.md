1. app/main.py を作成して、以下のような FastAPI アプリケーションを実装してください
### 1. ヘルスチェック API
HTTP メソッド: GET
パス: /health
レスポンス:
{ "status": "ok" }
### 2. 挨拶 API
HTTP メソッド: GET
パス: /greet
クエリパラメータ: name（任意）
仕様:
name が指定されていれば Hello, {name}!
指定されていなければ Hello, anonymous!
### 3. TODO 作成 API
HTTP メソッド: POST
パス: /todos
リクエストボディ(JSON):
{
  "title": "string",
  "done": false
}
レスポンス例
{
  "id": 1,
  "title": "Buy milk",
  "done": false
}

### 4. TODO 一覧表示 API
HTTP メソッド: GET
パス: /todos
レスポンス例:
[
  {
    "id": 1,
    "title": "Buy milk",
    "done": false
  },
  {
    "id": 2,
    "title": "Study Python",
    "done": true
  }
]

### 5. TODO 削除 API
HTTP メソッド: DELETE
パス: /todos/{todo_id}
パスパラメータ: todo_id（整数）
レスポンス例:
{
  "message": "Deleted"
}
エラーレスポンス例（存在しないID）:
{
  "detail": "Todo not found"
}




2. それぞれテストコードも書いてください。(pytest あたりを install すると良いです) (edited) 