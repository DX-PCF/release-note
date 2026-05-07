
# Title: May 06, 2026 
Link: https://docs.cloud.google.com/release-notes#May_06_2026<br>
Google Cloud インフラエンジニアとして、お問い合わせいただいたリリースノートについて、既存サービスへの影響調査結果を報告いたします。

---

# BigQuery
## Breaking
原文:
Starting June 1, 2026, due to changes in Google Ads data retention policies,
the BigQuery Data Transfer Service connectors for Google
Ads, Search Ads
360, and Google Analytics
4 will stop populating
data for backfill runs with dates earlier than 37 months from the current date.

[Google
Ads](https://docs.cloud.google.com/bigquery/docs/transfer-changes#June01-google-ads)
[Search Ads
360](https://docs.cloud.google.com/bigquery/docs/transfer-changes#June01-search-ads)
[Google Analytics
4](https://docs.cloud.google.com/bigquery/docs/transfer-changes#June01-ga4)
For more information about the changes to the Google Ads data retention
policies, see New Data Retention Policy for Google Ads starting June 1,
2026.

[New Data Retention Policy for Google Ads starting June 1,
2026](https://ads-developers.googleblog.com/2026/05/new-data-retention-policy-for-google.html)

説明：
2026年6月1日より、Google Adsのデータ保持ポリシー変更に伴い、BigQuery Data Transfer Serviceのコネクタ（Google Ads, Search Ads 360, Google Analytics 4向け）が、現在の日付から37ヶ月以上前の日付のデータに対してバックフィルを実行しなくなります。

影響有無：
**影響あり（ただし、将来的な影響）**
BigQuery Data Transfer Serviceを利用してGoogle Ads、Search Ads 360、またはGoogle Analytics 4のデータをBigQueryに転送している場合、2026年6月1日以降、37ヶ月以上前のデータのバックフィルが制限されます。現在稼働中のComposer環境 (Composer version 2.7.1, Airflow version 2.7.3) はBigQuery Data Transfer Serviceと直接連携する可能性がありますが、この変更はBigQuery Data Transfer Service自体の挙動変更であり、Composerのバージョンには依存しません。
日次運用でのデータ転送には影響ありませんが、過去のデータを再ロードするなどのバックフィル操作において、37ヶ月以上前のデータが必要となるシナリオがある場合は影響を受けます。

対処方法：
1.  **利用状況の確認**: BigQuery Data Transfer ServiceでGoogle Ads, Search Ads 360, Google Analytics 4のデータを転送しているか確認してください。
2.  **影響範囲の特定**: もし転送している場合、37ヶ月以上前のデータのバックフィルが必要となる運用（例: 大規模なデータ再構築、監査、法規制対応など）があるかを検討してください。
3.  **事前データ取得の検討**: 2026年6月1日より前に、必要となる可能性のある37ヶ月以上前のデータを、他の方法（例: 各サービスのAPI経由での直接エクスポート、レポート機能など）で取得し、別途安全な場所に保存することを検討してください。
4.  **ポリシー更新の監視**: Google Adsのデータ保持ポリシーに関する今後の更新や、代替となるデータ取得手段について、Google CloudおよびGoogle Adsの公式ドキュメントを引き続き監視してください。

用語説明：
*   **BigQuery Data Transfer Service**: Google Cloud のフルマネージドサービスで、Google Ads、Google Analytics、SalesforceなどのSaaSアプリケーションや、その他のクラウドストレージサービスからBigQueryにデータを自動的に転送・ロードします。
*   **Backfill runs**: 過去の特定の期間を指定して、その期間のデータをBigQueryに再転送する操作です。通常、データの欠落や修正があった場合に利用されます。
*   **Google Ads data retention policies**: Google AdsのデータをGoogleが保持する期間に関するポリシーです。このポリシーの変更がBigQuery Data Transfer Serviceのデータ転送に影響を与えます。

---

# Cloud Composer
## Announcement
原文:
Cloud Composer 2 environments can no longer be created in
Johannesburg (africa-south1). We're switching this region to
supporting only Cloud Composer 3 environments. Existing Cloud Composer 2
environments in this region aren't affected by this change.

説明：
ヨハネスブルグ（`africa-south1`）リージョンにおいて、Cloud Composer 2環境の新規作成ができなくなります。このリージョンは今後、Cloud Composer 3環境のみをサポートするよう移行されます。既存のヨハネスブルグリージョンのCloud Composer 2環境は、この変更の影響を受けません。

影響有無：
**影響なし**
現在のCloud Composer環境はComposer 2 (Composer version 2.7.1) ですが、この変更は特定のリージョン（`africa-south1`）における新規環境作成の制限です。既存のCloud Composer 2環境には影響がなく、また、現在の環境が`africa-south1`リージョンに存在しない限り、直接的な影響はありません。`africa-south1`は主にアフリカ地域向けのリージョンであり、日本からのアクセスには通常使用されません。

対処方法：
1.  **リージョンの確認**: 現在利用しているCloud Composer環境のリージョンが`africa-south1`ではないことを確認してください。
2.  **将来計画の確認**: もし将来的に`africa-south1`リージョンでCloud Composer環境を新規構築する計画がある場合は、Cloud Composer 3の利用を前提とするか、他のリージョンでのComposer 2環境の構築を検討してください。

用語説明：
*   **Cloud Composer**: Google Cloud上でApache Airflowをフルマネージドで実行するためのサービスです。複雑なデータパイプラインやワークフローのオーケストレーションに利用されます。
*   **Cloud Composer 2/3**: Cloud Composerの主要なバージョンです。Composer 3は新しいアーキテクチャや機能を提供し、Composer 2からのアップグレードが推奨されています。
*   **`africa-south1`**: Google Cloudのヨハネスブルグ（南アフリカ）リージョンの名称です。

---

# Google Kubernetes Engine
## Fixed
原文:
A fix is available for an issue that caused incomplete file reads and premature
end-of-file (EOF) errors when you used the Cloud Storage FUSE CSI driver on
ARM64 nodes that use 64 KiB page sizes, such as A4X and A4X Max instances. This
issue occurred because the kernel read-ahead mechanism triggered read requests
that exceeded the capacity of the Cloud Storage FUSE layer.

To resolve this issue, upgrade your cluster to one of the following versions:

- 1.33.11-gke.1019000 or later
- 1.34.6-gke.1154000 or later
- 1.35.2-gke.1485000 or later

説明：
ARM64ノード（A4XやA4X Maxインスタンスなど、64KiBページサイズを使用するノード）でCloud Storage FUSE CSIドライバを使用した場合に、ファイル読み込みが不完全になったり、予期せぬEOF（End-of-File）エラーが発生する問題が修正されました。この問題は、カーネルのリード・アヘッド機構がCloud Storage FUSEレイヤーの処理能力を超える読み込みリクエストをトリガーしたことに起因していました。この問題を解決するためには、GKEクラスターを特定のバージョン（1.33.11-gke.1019000以降など）にアップグレードする必要があります。

影響有無：
**影響なし**
当社のCloud Composer環境 (Composer version 2.7.1, Airflow version 2.7.3) は、Google Kubernetes Engine (GKE) 上で動作しますが、この修正は以下の特定の条件が全て揃う場合にのみ関連します。
1.  GKEクラスターを直接運用している。
2.  クラスターのノードにARM64インスタンス（A4X、A4X Maxなど）を使用している。
3.  これらのノードが64 KiBのページサイズを使用している。
4.  Cloud Storage FUSE CSIドライバをデプロイし、利用している。

Cloud Composerは通常、Googleが管理するGKEクラスター上で動作し、これらの詳細なGKE設定（特にノードのCPUアーキテクチャやページサイズ、CSIドライバの利用）をユーザーが直接制御することは稀です。また、Composer環境がデフォルトでARM64ノードとCloud Storage FUSE CSIドライバを使用する構成にはなっていません。したがって、現在のCloud Composer環境には直接的な影響はないと判断します。

対処方法：
特別な対処は不要です。
もし、Cloud Composer環境とは別に、自社で直接GKEクラスターを運用しており、上記の影響条件（ARM64ノード、64KiBページサイズ、Cloud Storage FUSE CSIドライバの利用）に該当する場合は、記載されているGKEバージョンへのクラスターアップグレードを検討してください。

用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するフルマネージドなKubernetesサービスで、コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **ARM64 ノード**: ARMアーキテクチャのCPUを搭載したGKEノードです。Intel/AMDなどのx86アーキテクチャとは異なる命令セットを持ち、特定のワークロードでコスト効率や性能のメリットがあります。
*   **Cloud Storage FUSE CSI ドライバ**: KubernetesのContainer Storage Interface (CSI) を実装したドライバで、Google Cloud StorageバケットをKubernetes Pods内のファイルシステムとしてマウントすることを可能にします。これにより、アプリケーションはCloud Storageのオブジェクトを通常のファイルのようにアクセスできます。
*   **64 KiB page sizes**: Linuxカーネルのメモリ管理におけるページサイズの一種です。一般的なx86システムでは4 KiBが主流ですが、一部のARM64システムや特定のパフォーマンス最適化のために64 KiBが使用されることがあります。
*   **EOF (End-of-File) エラー**: ファイルの読み込み中に、予期せずファイルの終端に達したことを示すエラーです。
*   **Kernel read-ahead mechanism**: オペレーティングシステムのカーネル機能の一つで、アプリケーションがまだ要求していないデータを予測してストレージから事前に読み込んでおくことで、I/O性能を向上させます。