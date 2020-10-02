from django.test import TestCase
from django.urls import reverse, resolve
from pljudge.views import *

class TestUrls(TestCase): # pljudge:index URL にアクセスした時のステータス 200 を確認するテスト
  def test_index_url_reverse(self):
    """
    - TestCaseクラス　：　Djangoに標準的に組み込まれているunittestの拡張機能。最初にインポートしておき、今後作成するテストクラスはこのTestCaseクラスを継承します。
    - reverse関数　：　引数のURLを返します。signupという名前のURLを返しています。
    - assertEqual関数　：　第一引数と第二引数の値が等しいかどうかを返す。
    """
    url = reverse('pljudge:index') # pljudge:index の URL を逆引き
    response = self.client.get(url) # url に GET request を投げた時のレスポンス
    self.assertEquals(response.status_code, 200) # ステータスコード 200 が返ってくるかを検証