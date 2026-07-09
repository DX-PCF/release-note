
# Title: July 07, 2026 
Link: https://docs.cloud.google.com/release-notes#July_07_2026<br>
## Cloud SDK
### Change
原文: (リリースノートの内容が提供されていません。)
説明：提供されたリリースノートにはCloud SDKに関する具体的な変更内容が記載されていません。
影響有無：具体的な変更内容が不明なため、影響の有無は判断できません。
対処方法：具体的な変更内容が発表され次第、確認と評価が必要です。
用語説明：
*   **Cloud SDK**: Google Cloudのサービスをコマンドラインから操作するためのツール群です。`gcloud` コマンドラインツール、各種APIクライアントライブラリ、エミュレータなどが含まれます。

## Google Kubernetes Engine
### Change
原文: For GKE Standard clusters, the maximum number of nodes that you can upgrade simultaneously by using surge upgrades (`maxSurge` + `maxUnavailable`) is now 100. Each of these settings can be set as high as 100, but their sum can be no higher than 100. For more information, see Surge upgrades.
説明：GKE Standard クラスタにおいて、サージアップグレード時に同時にアップグレードできるノードの最大数が100に変更されました。これは、`maxSurge` (追加で一時的に作成されるノード数) と `maxUnavailable` (アップグレード中に一時的に利用不可となるノード数) の合計が100を超える設定ができなくなったことを意味します。個々の設定 (`maxSurge` または `maxUnavailable`) はそれぞれ100まで設定可能ですが、両者の合計は100を超えてはなりません。
影響有無：
*   **影響あり（考慮が必要）**: 既存のGKE Standardクラスタでノードプールのアップグレード戦略として `maxSurge` と `maxUnavailable` を設定しており、その合計が100を超えている場合、この変更により設定が適用されなくなるか、エラーとなる可能性があります。
*   **影響なし（ポジティブな側面も）**: 通常の運用では `maxSurge` と `maxUnavailable` の合計が100を超えるような大規模な設定は稀であるため、多くのクラスタには直接的な影響はありません。むしろ、大規模なクラスタを持つユーザーにとっては、アップグレード効率を向上させるために同時にアップグレード可能なノード数の上限が実質的に緩和された（または明確化された）と捉えることができます。
対処方法：
1.  **設定の確認**: 現在運用中のGKE Standardクラスタにおいて、各ノードプールのアップグレード戦略 (`maxSurge` および `maxUnavailable` の設定) を確認してください。
2.  **設定の調整**: もし `maxSurge` と `maxUnavailable` の合計が100を超えているノードプールがあれば、アップグレード時の可用性やパフォーマンス要件を考慮し、合計が100以下になるように設定値を調整してください。
用語説明：
*   **GKE Standard clusters**: Google Kubernetes Engineのクラスタモードの一つで、ユーザーがノードの管理に関与する部分が多い、柔軟性の高い構成です。
*   **Surge upgrades**: GKEノードプールのアップグレード戦略の一つです。アップグレード中に新しいノードを追加でプロビジョニングし、既存ノードから新しいノードへワークロードを段階的に移行させることで、サービスの中断を最小限に抑えながらアップグレードを進行させます。
*   **`maxSurge`**: ノードプールアップグレード中に、一時的に追加でプロビジョニングされるノードの最大数を示します。これにより、アップグレード中のクラスタの全体的なリソース容量を維持しやすくなります。
*   **`maxUnavailable`**: ノードプールアップグレード中に、同時に利用不可となるノードの最大数を示します。この値が高いほどアップグレードは高速に進行しますが、一時的に利用可能なリソース容量が減少する可能性があります。可用性を維持するためにはこの値を低く設定します。
# Title: July 06, 2026 
Link: https://docs.cloud.google.com/release-notes#July_06_2026<br>
# BigQuery
## Changed
原文: For data transfers from Facebook Ads, support for the `AdInsightsMMM` report has been temporarily disabled. Existing data transfers from Facebook Ads that include the `AdInsightsMMM` report will continue to run, but the transfer won't include data from the `AdInsightsMMM` report.
[data transfers from Facebook Ads](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer)
This change is due to schema changes in the Facebook Ads API.
For more information, see [July 06, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#Jul06-fb-ads).

説明:
BigQuery Data Transfer ServiceのFacebook広告データ転送機能において、「AdInsightsMMM」レポートのサポートが一時的に無効化されました。既に設定されているFacebook広告からのデータ転送ジョブは引き続き実行されますが、「AdInsightsMMM」レポートに関するデータは転送に含まれなくなります。
この変更は、Facebook Ads APIのスキーマ（データ構造）の変更に起因するものです。詳細については、提供されたリンク（特に2026年7月6日付けの変更ログ）を参照してください。

影響有無:
影響あり。
BigQuery Data Transfer Serviceを利用してFacebook広告のデータを転送しており、特に `AdInsightsMMM` レポートのデータを取得しているシステムや分析がある場合、そのデータが一時的に取得できなくなります。これにより、当該レポートに依存するダッシュボード、分析、機械学習モデルなどに影響が生じる可能性があります。
既存のデータ転送ジョブ自体は停止せず実行され続けるため、他のレポートデータの転送には影響ありません。

対処方法:
1.  **影響範囲の確認**: BigQuery Data Transfer ServiceでFacebook広告の転送設定を確認し、`AdInsightsMMM` レポートを転送対象としているかどうかを特定してください。
2.  **データ欠損への対応**: もし `AdInsightsMMM` レポートのデータに依存するワークロードがある場合、そのデータが一時的に欠損することを考慮し、代替データソースの検討や、レポート・分析結果への影響度を評価してください。
3.  **情報収集**: Google CloudのリリースノートやFacebook Ads APIの変更情報を継続的に確認し、`AdInsightsMMM` レポートのサポート再開時期やFacebook Ads API側の最新のスキーマ情報を把握してください。現状では、BigQuery側でユーザーが設定変更を行う必要はありません。

用語説明:
*   **BigQuery Data Transfer Service**: Google BigQueryへ、外部データソース（SaaSアプリケーション、データウェアハウスなど）からデータを自動的にロードするサービスです。スケジュール設定や増分ロードに対応し、データ統合を簡素化します。
*   **Facebook Ads API**: Facebook広告プラットフォームのデータをプログラム的に操作するためのインターフェースです。広告キャンペーンの作成、管理、レポートの取得など、幅広い機能を提供します。
*   **スキーマ変更**: データベースやAPIにおいて、データの構造（テーブルの列、データ型、JSONオブジェクトのフィールドなど）が変更されることです。API側のスキーマ変更は、それを利用するアプリケーション側での対応が必要となる場合があります。
*   **AdInsightsMMMレポート**: Facebook広告のインサイトデータに関するレポートの一種です。MMMは「Marketing Mix Modeling」の略である可能性があり、マーケティング活動の各要素が売上などの成果にどの程度貢献しているかを分析するための指標を含む場合があります。