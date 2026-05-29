
# Title: May 28, 2026 
Link: https://docs.cloud.google.com/release-notes#May_28_2026<br>
# Cloud Logging
## Announcement
**原文:** You can view the available regional endpoints for the Cloud Logging API on the REST reference pages. For an example, see Method: projects.locations.buckets.list.

[Method: projects.locations.buckets.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/list?rep_location=global)

**説明:**
Cloud Logging APIのRESTリファレンスドキュメントに、利用可能なリージョンエンドポイントに関する情報が追加されたというアナウンスです。これにより、Cloud Logging APIをプログラムから利用する際に、特定のリージョン（地域）に合わせたエンドポイントを選択するための情報がより明確に提供されるようになりました。具体例として、`projects.locations.buckets.list` メソッドのドキュメントが挙げられています。

**影響有無:**
**影響なし。**
このアナウンスは、Cloud Logging APIの機能や動作そのものを変更するものではなく、既存のドキュメントに情報が追加されたことを示しています。既存のCloud Loggingの利用方法や、現在稼働しているサービスに対して直接的な影響（例：設定変更の必要、非互換性、パフォーマンス変動など）は一切ありません。これは、APIを利用する開発者やインフラエンジニアが、より最適なエンドポイントを選択するための情報提供の改善です。

**対処方法:**
既存のシステムや設定に対して、特別な対処は不要です。
今後、Cloud Logging APIをプログラムから利用する際や、パフォーマンス・データレジデンシー要件を考慮してエンドポイントを見直す際に、この新しいドキュメント情報を参考にすることが推奨されます。

**用語説明:**
*   **リージョンエンドポイント (Regional Endpoints):** クラウドサービスにアクセスするための、特定の地理的リージョン（地域）に特化したネットワークアドレス（URL）。これにより、データの物理的な場所を指定したり、ネットワークのレイテンシを最適化したりすることが可能になります。
*   **RESTリファレンス (REST Reference):** RESTful APIの使用方法を詳細に説明した公式ドキュメントのこと。APIの各メソッド（機能）のURI、HTTPメソッド、リクエストやレスポンスの形式、必須パラメータなどが記載されています。
*   **`projects.locations.buckets.list`:** Cloud Logging APIにおける特定のメソッド名です。これは、特定のGoogle Cloudプロジェクト内の、特定のロケーション（リージョン）に存在するログバケットの一覧を取得するために使用されます。
# Title: May 27, 2026 
Link: https://docs.cloud.google.com/release-notes#May_27_2026<br>
以下のリリースノートに基づき、各製品への影響調査結果を報告します。

---

# BigQuery
## Change
原文: An updated version of the Simba ODBC driver for BigQuery is now available.
[Simba ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_odbc_driver)

説明: BigQueryに接続するためのSimba ODBCドライバーの新しいバージョンがリリースされ、利用可能になりました。

影響有無: **影響なし（既存環境）。ポジティブな影響（更新時）。**
既存のBigQuery接続には直接的な影響はありません。この更新は、Simba ODBCドライバーを使用しているクライアントアプリケーションに対して、新機能、パフォーマンスの改善、またはバグ修正の適用機会を提供します。

対処方法:
BigQueryへのデータ接続にSimba ODBCドライバーを使用している場合、最新の機能や修正を利用するためにドライバーの更新を検討してください。更新を行う際は、本番環境に適用する前に開発・ステージング環境で互換性テストを実施し、アプリケーションへの影響がないことを確認することを強く推奨します。

用語説明:
*   **ODBC (Open Database Connectivity):** データベースへのアクセスを標準化するためのAPI（Application Programming Interface）。異なるデータベースシステムに対して、統一された方法でデータアクセスを可能にします。
*   **Simba ODBC driver:** Simba Technologiesが開発・提供する、特定のデータソース（この場合はBigQuery）に接続するためのODBCドライバー。

---

# Cloud SDK
## Change
原文:

説明: Cloud SDKに関する変更がアナウンスされていますが、リリースノートの原文には具体的な内容が記載されていません。これは通常、リリースノートのフォーマット上のプレースホルダーであるか、詳細が別途公開される前の予備情報である可能性があります。

影響有無: **不明。**
現時点では具体的な変更内容が不明であるため、影響の有無も判断できません。

対処方法:
今後のCloud SDKのリリースノートや公式ドキュメントで詳細な情報が公開される可能性がありますので、引き続き注視してください。現時点では特別な対処は不要です。

用語説明:
*   **Cloud SDK:** Google Cloudとプログラムでやり取りするためのツールセットです。コマンドラインインターフェース（`gcloud`コマンドなど）、クライアントライブラリ、およびツールが含まれます。

---

# Google Kubernetes Engine
## Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明: Google Kubernetes Engine (GKE) クラスタの新しいバージョンがリリースされ、新規クラスタ作成および既存クラスタの手動アップグレード（コントロールプレーンとノード）で利用可能になりました。

影響有無: **影響なし（既存環境）。ポジティブな影響（新規・アップグレード時）。**
既存のGKEクラスタが自動アップグレードの対象となっている場合でも、即座にバージョンが変更されるわけではありません。新しいバージョンは、Kubernetesの機能改善、バグ修正、パフォーマンス向上などを含んでいます。

対処方法:
運用中のGKEクラスタに影響はありませんが、最新の機能や改善を利用するため、計画的にクラスタのバージョンアップグレードを検討してください。アップグレード戦略（自動アップグレードチャネル、メンテナンスウィンドウ）を確認し、新しいバージョンでのアプリケーションの互換性テストを実施することを推奨します。

用語説明:
*   **GKE (Google Kubernetes Engine):** Google Cloudが提供するマネージドなKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **コントロールプレーン (Control Plane):** Kubernetesクラスタの管理コンポーネント群（APIサーバー、スケジューラ、コントローラーマネージャーなど）を含む部分。
*   **ノード (Node):** アプリケーションのワークロードを実行する仮想マシンまたは物理マシン。KubernetesではPodがノード上で動作します。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:
| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.30.14-gke.2558000 | cos-117-18613-613-5 | [cos-117-18613-613-5 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-613-5_) |
| 1.31.14-gke.1967000 | cos-117-18613-613-7 | [cos-117-18613-613-7 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-613-7_) |
| 1.33.12-gke.1059000 | cos-121-18867-381-125 | [cos-121-18867-381-125 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-381-125_) |
| 1.35.5-gke.1057000 | cos-125-19216-395-7 | [cos-125-19216-395-7 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-395-7_) |
| 1.36.0-gke.2459000 | cos-129-19506-120-64 | [cos-129-19506-120-64 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129#cos-129-19506-120-64_) |

説明: 新しいGKEバージョンには、セキュリティ修正が適用されたContainer-Optimized OS (COS) イメージが含まれています。これらのイメージは、前回のGKEリリース以降に公開されたCOSバージョンからのセキュリティ修正を累積的に統合しています。各COSイメージで解決された具体的な脆弱性の詳細については、提供されたリンクからリリースノートを確認できます。

影響有無: **ポジティブな影響あり。**
この更新は、GKEクラスタの基盤となるOSのセキュリティを向上させます。これにより、既知の脆弱性からクラスタが保護され、全体的なセキュリティ体制が強化されます。

対処方法:
GKEクラスタが自動アップグレードの対象である場合、ノードは自動的に更新されたCOSイメージを使用するようになります。手動でクラスタのバージョンを管理している場合は、セキュリティ向上を目的として、計画的に最新のGKEバージョンへのアップグレードを実施することを推奨します。

用語説明:
*   **Container-Optimized OS (COS):** Googleが開発した、コンテナ実行に最適化されたLinuxベースのオペレーティングシステム。GKEノードのデフォルトOSとして使用されます。
*   **セキュリティ修正:** ソフトウェアの脆弱性を解消するためのパッチやアップデート。

## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.6-gke.1307000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel: 1.33.11-gke.1074000, 1.34.7-gke.1055000
- The following versions are no longer available in the Stable channel: 1.33.10-gke.1115000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.33.10-gke.1176000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.6-gke.1154000
- 1.34.6-gke.1237000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.3-gke.1234002 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.3-gke.1389000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.32 to 1.33.11-gke.1013000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.33 to 1.33.11-gke.1013000, 1.34 to 1.34.6-gke.1307000, 1.35 to 1.35.3-gke.1389002
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)

説明: Stableリリースチャネルにおいて、GKEクラスタのバージョンが更新されました。新規クラスタ作成時のデフォルトバージョンが `1.34.6-gke.1307000` に変更され、複数の新しいバージョンが利用可能になりました。同時に、一部の古いバージョン（例: `1.33.10-gke.1115000`、`1.35.3-gke.1234002` など）は非推奨となり、90日以内またはサポート終了時に削除される予定です。また、このチャネルのクラスタに対する自動アップグレードのターゲットバージョンも更新されました。

影響有無: **潜在的に影響あり。**
*   **新規クラスタ作成:** デフォルトバージョンが変更されるため、明示的にバージョンを指定しない場合、新しいデフォルトバージョンでクラスタが作成されます。
*   **既存クラスタの自動アップグレード:** Stableチャネルを使用している既存のクラスタは、GKEによって自動的に新しいターゲットバージョンにアップグレードされる可能性があります（メンテナンスウィンドウや除外設定による）。これにより、アプリケーションの互換性問題が発生する可能性があります。
*   **非推奨バージョンを使用中のクラスタ:** 非推奨となったバージョンを使用しているクラスタは、90日以内に強制アップグレードの対象となる可能性が高いです。これは予期せぬダウンタイムやアプリケーションの動作不良を引き起こす可能性があります。

対処方法:
1.  **利用中のクラスタバージョンの確認:** 現在運用しているGKEクラスタのバージョンが、非推奨リストに含まれていないか確認します。
2.  **計画的なアップグレードの実施:** 非推奨バージョンを使用している場合は、速やかにアプリケーションの互換性を確認し、計画的なアップグレードを実施してください。
3.  **メンテナンスウィンドウと除外設定の確認:** 自動アップグレードが予期せぬタイミングで実行されないよう、メンテナンスウィンドウや除外設定が適切に構成されていることを確認します。
4.  **互換性テストの実施:** 新しいGKEバージョンにおける非推奨APIや変更点をアプリケーションが適切に扱えるか、アップグレード前に十分な互換性テストを実施してください。
5.  **新規クラスタ作成時のバージョン指定:** 新規クラスタを作成する際は、意図するバージョンを明示的に指定することを検討してください。

用語説明:
*   **リリースチャネル (Release Channel):** GKEクラスタの自動アップグレードの頻度と安定性を選択するメカニズム。Stable、Regular、Rapid、Extendedなどがあります。
*   **デフォルトバージョン:** 新規クラスタ作成時に、バージョンを明示的に指定しない場合に適用されるバージョン。
*   **非推奨 (Deprecated):** 将来的にサポートが終了し、利用できなくなる予定の機能やバージョン。

## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.3-gke.1389002 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel: 1.33.11-gke.1197000, 1.34.7-gke.1499000, 1.35.3-gke.2190000
- The following versions are no longer available in the Regular channel: 1.33.11-gke.1013000, 1.34.6-gke.1307000, 1.35.3-gke.1389000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.32 to