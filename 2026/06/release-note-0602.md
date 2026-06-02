
# Title: June 01, 2026 
Link: https://docs.cloud.google.com/release-notes#June_01_2026<br>
# BigQuery
## Change
原文: The Facebook Ads connector for the BigQuery Data Transfer Service now supports data transfers from the following Facebook Ads reports:

- `AdInsightsMMM`
- `Ads`
- `AdCreatives`
- `AdSets`
- `Campaigns`
- `AdImages`
- `AdLabels`
- `Businesses`
- `CustomAudiences`

説明:
BigQuery Data Transfer ServiceのFacebook Adsコネクタが、新たに9種類のFacebook Adsレポート（`AdInsightsMMM`、`Ads`、`AdCreatives`、`AdSets`、`Campaigns`、`AdImages`、`AdLabels`、`Businesses`、`CustomAudiences`）からのデータ転送をサポートするようになりました。これにより、より詳細なFacebook広告関連データをBigQueryに自動で取り込むことが可能になります。

影響有無:
*   **直接的な影響はありません。** 現在、BigQuery Data Transfer ServiceのFacebook Adsコネクタを利用していない場合、または利用していてもこれらの新しいレポートタイプのデータに興味がない場合は、既存のシステム運用に影響はありません。
*   **ポジティブな影響があります。** 既存でBigQuery Data Transfer ServiceのFacebook Adsコネクタを利用しており、追加されたこれらのレポートからのデータ転送を必要としていた場合は、データ分析の幅が広がり、より深いインサイトを得られる機会が増えます。
*   本変更は、Google Cloud Composer2のバージョン（Composer version 2.7.1、Airflow version 2.7.3）に直接的な影響を与えるものではありません。Composer/AirflowはBigQueryへのデータロードや変換をオーケストレーションするために利用されることがありますが、今回の変更はBigQuery Data Transfer Service自体の機能拡張です。

対処方法:
*   既存のシステム運用に変更は発生しないため、**特別な対処は不要です。**
*   もし追加されたレポートからのデータ転送を希望する場合は、BigQuery Data Transfer Serviceで新しい転送ジョブを設定するか、既存のジョブを更新することで、これらのレポートからデータをBigQueryに取り込むことが可能です。新しいデータを取り込むことで、BigQueryのストレージ料金やクエリ料金が増加する可能性がありますので、ご注意ください。

用語説明:
*   **BigQuery Data Transfer Service (BQ DTS)**: 外部のSaaSアプリケーション（例: Google Ads, Salesforce, Facebook Adsなど）やその他のデータソースからBigQueryへ、定期的かつ自動的にデータを転送するためのフルマネージドサービスです。ETLプロセスを簡素化し、データ分析の準備を効率化します。
*   **Facebook Ads connector**: BigQuery Data Transfer ServiceがFacebook広告プラットフォームと連携し、広告データを取り込むための特定のコネクタ（接続機能）です。
*   **Facebook Ads reports**: Facebookの広告マネージャーで確認できる、広告キャンペーンのパフォーマンス、費用、クリエイティブ、ターゲットオーディエンスなどの詳細情報を含むレポートです。
# Title: May 29, 2026 
Link: https://docs.cloud.google.com/release-notes#May_29_2026<br>
## Apigee X

### Announcement

**原文:** `On May 29, 2026, we released an updated version of the Apigee UI.`

**説明:**
2026年5月29日にApigeeのユーザーインターフェース (UI) の更新版がリリースされたというアナウンスです。これはUIの外観や操作性に関する変更を示唆しています。

**影響有無:**
**影響なし**。UIの更新は通常、既存のAPIプロキシやランタイムの動作に直接的な影響を与えません。管理コンソールの視覚的な変更や機能配置の調整が主であり、APIトラフィックの処理やデータプレーンの動作に影響することはありません。

**対処方法:**
特段の対処は不要です。新しいUIの変更点についてユーザーが慣れるための期間を設ける程度で十分です。

**用語説明:**
*   **Apigee X**: Google Cloudが提供するエンタープライズ向けのAPI管理プラットフォームです。APIの設計、公開、セキュリティ、監視、分析など、APIライフサイクル全体を管理します。
*   **Apigee UI**: Apigeeプラットフォームを管理するためのウェブベースのグラフィカルユーザーインターフェースです。APIプロキシの作成、デプロイ、デベロッパーアプリの管理、APIトラフィックの監視などを行います。

---

## Google Kubernetes Engine

### Issue

**原文:** `In GKE version 1.35 and later, workloads that use Workload Identity to authenticate to Google Cloud APIs might experience transient connectivity timeouts or refused connections to the GKE metadata server immediately following node startup. For recommendations and workarounds, see Timeout errors at Pod startup.`

**説明:**
GKEバージョン1.35以降において、Workload Identityを使用してGoogle Cloud APIに認証を行うワークロードが、ノード起動直後にGKEメタデータサーバーへの一時的な接続タイムアウトや接続拒否を経験する可能性があるという既知の問題です。この問題は、Podの起動が遅延したり失敗したりする原因となる可能性があります。

**影響有無:**
**影響あり**。もし以下の条件に合致する場合、ワークロードの起動に問題が発生する可能性があります。
*   **GKEクラスターのバージョンが1.35以降である場合。**
*   **クラスター内のワークロードがWorkload Identityを使用してGoogle Cloud APIに認証を行っている場合。**

この問題が発生すると、アプリケーションの起動時（特にノードが再起動された際）にGoogle Cloud APIへのアクセスが一時的に失敗し、アプリケーションの初期化や機能に支障が出る可能性があります。

**対処方法:**
この問題に対する推奨事項と回避策については、Google Cloudドキュメントの「Timeout errors at Pod startup」を参照してください。具体的な対処方法としては、以下のようなものが考えられます。
*   **アプリケーション側でのリトライロジックの実装:** Google Cloud APIへのアクセスにおいて、指数バックオフ（Exponential Backoff）などのリトライメカニズムを実装することで、一時的な接続問題を吸収できます。
*   **ドキュメントに記載されたWorkload Identity設定の確認:** Workload Identityの設定が正しく行われているか、特にKubernetesサービスアカウントとGoogle Cloudサービスアカウントのバインドが適切かを確認します。
*   **GKEノードのOSイメージの確認:** 一部のOSイメージバージョンで特定の挙動がある場合、推奨されるOSイメージへの更新を検討します。

[Timeout errors at Pod startup](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication#troubleshoot-timeout)

**用語説明:**
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Workload Identity**: GKE PodがGoogle CloudのサービスアカウントとしてGoogle Cloud APIに認証を行うための推奨されるメカニズムです。これにより、GKE PodがGCPリソースにセキュアかつ細粒度なアクセス制御でアクセスできるようになります。
*   **GKE metadata server**: 各GKEノード上で動作する特殊なサービスで、Podが自身に関するメタデータ（Workload Identityのトークンなど）を取得するためにアクセスするローカルエンドポイントです。
*   **Transient connectivity timeouts**: 一時的な接続タイムアウトのことです。ネットワークの一時的な問題やサーバーの負荷、リソースの競合などによって、断続的に発生する接続エラーを指します。
*   **Refused connections**: 接続拒否のことです。サーバーがクライアントからの接続要求を拒否する状態を指し、ファイアウォール設定、サーバーのポートがリッスンしていない、またはサーバーの接続制限などが原因で発生することがあります。