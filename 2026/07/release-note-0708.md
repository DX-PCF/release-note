
# Title: July 07, 2026 
Link: https://docs.cloud.google.com/release-notes#July_07_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、各製品の変更点とサービスへの影響について調査し、簡潔に回答します。

---

# Cloud SDK
## Change
原文: (具体的な変更内容なし)
説明：リリースノートに具体的な変更内容は記載されていません。
影響有無：現時点では、具体的な変更内容が提供されていないため、サービスへの影響は不明です。
対処方法：追加の情報が公開され次第、改めて影響を確認し、必要に応じて対応を検討します。
用語説明：
*   **Cloud SDK**: Google Cloudのサービスをコマンドラインから操作するためのツールセットです。gcloudコマンド、bqコマンド、gsutilコマンドなどが含まれます。

---

# Google Kubernetes Engine
## Change
原文: For GKE Standard clusters, the maximum number of nodes that you can upgrade simultaneously by using surge upgrades (`maxSurge` + `maxUnavailable`) is now 100. Each of these settings can be set as high as 100, but their sum can be no higher than 100. For more information, see Surge upgrades.
[Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge)

説明：GKE Standardクラスタにおいて、サージアップグレード（`maxSurge` + `maxUnavailable`）を使用して同時にアップグレードできるノードの最大数が100に変更されました。`maxSurge`と`maxUnavailable`のそれぞれは最大100まで設定可能ですが、両者の合計は100を超えてはなりません。

影響有無：影響なし。
これは、GKE Standardクラスタにおけるノードの同時アップグレード数に設定できる上限が**拡大された**ことを示す変更です。既存のアップグレード戦略や設定がこの上限を超えていない限り、現在の運用に悪影響を及ぼすものではありません。むしろ、大規模なクラスタのアップグレードにおいて、より多くのノードを並行して処理できるようになり、アップグレード時間の短縮に貢献する可能性があります。

対処方法：特に対処は不要です。
もし、より迅速なアップグレードを求める場合は、ノードプールのアップグレード戦略（`maxSurge`や`maxUnavailable`）を見直し、この新しい上限を考慮して設定を調整することを検討できます。現在の設定で問題がなければ変更の必要はありません。

用語説明：
*   **GKE Standardクラスタ**: Google Kubernetes Engineで提供されるクラスタタイプの一つで、ユーザーがノードやノードプールなどのインフラをより細かく制御できるモードです。
*   **サージアップグレード (Surge upgrades)**: GKEノードプールのアップグレード戦略の一つです。新しいノードを一時的に追加（サージ）しながら古いノードを置き換えていくことで、サービスの中断を最小限に抑えながらアップグレードを実行します。これにより、アップグレード中のアプリケーションの可用性を高めます。
*   `maxSurge`: アップグレード中にノードプールが通常のサイズを超えて一時的に追加される、新しいノードの最大数。
*   `maxUnavailable`: アップグレード中に、同時に利用できなくなる（オフラインになる）ノードの最大数。これらのノードは、アップグレードが完了するまでアプリケーションのトラフィックを処理できません。
# Title: July 06, 2026 
Link: https://docs.cloud.google.com/release-notes#July_06_2026<br>
# BigQuery
## Change
原文: For data transfers from Facebook Ads, support for the `AdInsightsMMM` report has been temporarily disabled. Existing data transfers from Facebook Ads that include the `AdInsightsMMM` report will continue to run, but the transfer won't include data from the `AdInsightsMMM` report.
[data transfers from Facebook Ads](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer)
This change is due to schema changes in the Facebook Ads API.
For more information, see July 06, 2026.
[July 06, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#Jul06-fb-ads)

説明:
BigQuery Data Transfer ServiceのFacebook広告データ転送機能において、`AdInsightsMMM`レポートのデータ転送が一時的に無効化されました。この変更は、Facebook Ads API側のスキーマ変更に起因するものです。
既存のFacebook広告データ転送ジョブに`AdInsightsMMM`レポートが含まれている場合でも、転送ジョブ自体は引き続き実行されますが、当該レポートのデータは転送されなくなります。詳細については、将来の特定の日付（2026年7月6日）に更新情報が提供される可能性があります。

影響有無:
**影響あり**。
現在BigQuery Data Transfer Serviceを使用してFacebook広告からデータを転送しており、その転送設定に`AdInsightsMMM`レポートを含めている場合、当該レポートのデータはBigQueryへ転送されなくなります。これにより、`AdInsightsMMM`レポートに依存するダウンストリームの分析やレポーティングにデータ欠損の影響が生じる可能性があります。

対処方法:
1.  **データ転送設定の確認**: BigQuery Data Transfer ServiceでFacebook広告からのデータ転送ジョブが設定されているか、またそのジョブに`AdInsightsMMM`レポートが含まれているかを確認してください。
2.  **影響範囲の評価**: `AdInsightsMMM`レポートのデータが転送されないことによって、現在行われているBigQueryでのデータ分析、ダッシュボード、あるいは機械学習モデルなどにどのような影響が生じるかを評価してください。
3.  **代替データ取得方法の検討**: `AdInsightsMMM`レポートのデータが業務上必須である場合、Facebook Ads APIを直接利用してデータを取得し、BigQueryに別途ロードするなどの代替手段を検討する必要があります。この場合、BigQueryへのデータロードにはCloud Storageを介した一括ロードや、他のデータ連携サービスを利用することが考えられます。
4.  **Google CloudおよびFacebookの更新情報の継続的な監視**: この一時的な無効化が解消される時期や、Facebook Ads APIのスキーマ変更に関する追加情報について、Google CloudのリリースノートおよびFacebookの公式開発者ドキュメントを定期的に確認することを推奨します。

用語説明:
*   **BigQuery Data Transfer Service**: Google Cloudが提供するフルマネージドなサービスで、Google Ads、YouTube、Facebook AdsといったSaaSアプリケーションやクラウドストレージなどから、BigQueryへデータを自動的かつ定期的に転送する機能を提供します。データの抽出、変換、ロード（ETL）プロセスを自動化し、データウェアハウスへのデータ統合を簡素化します。
*   **Facebook Ads API**: Facebookの広告プラットフォームが提供するプログラマブルなインターフェースです。これにより、開発者は広告キャンペーンの作成、管理、レポートの取得、オーディエンスのターゲティングなど、広告関連の操作をプログラムから自動的に実行できます。
*   **`AdInsightsMMM`レポート**: Facebook Ads APIを通じて提供される可能性のあるレポートの一つであり、"Marketing Mix Modeling (MMM)"に関連する広告インサイトや指標を提供するものと推測されます。MMMは、さまざまなマーケティングチャネルの広告支出が売上や他のビジネス成果にどの程度貢献しているかを統計的に評価する分析手法です。
*   **スキーマ変更 (Schema Changes)**: データベースやAPIなどにおけるデータ構造（テーブルの列定義、データ型、リレーションシップなど）の変更を指します。APIのスキーマ変更は、そのAPIを利用するアプリケーションが期待通りにデータを解釈できなくなる原因となることがあります。非互換なスキーマ変更（Breaking Change）は、既存のアプリケーションに修正が必要となる場合があります。