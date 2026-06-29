
# Title: June 26, 2026 
Link: https://docs.cloud.google.com/release-notes#June_26_2026<br>
Google Cloud インフラエンジニアとして、GKE のリリースノートに基づき、構築済みのサービスへの影響有無を調査し、以下の通り回答します。

現在の環境は Google Cloud Composer 2 (Composer version 2.7.1、Airflow version 2.7.3) を利用しています。
Composer 2.7.1 は、GKE バージョン 1.27.x にマッピングされています。
今回のリリースノートに記載されている GKE バージョンは 1.30.x 以降であるため、**直接的な影響は現在ありません。**
ただし、GKE クラスタのバージョン提供状況の変更は、将来的な Composer アップグレード時に考慮すべき情報となります。

---

# Google Kubernetes Engine

## Change (GKE cluster versions have been updated - No channel (deprecated))

原文:
```
 GKE cluster versions have been updated.

 **New versions available for upgrades and new clusters.**

 The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

[GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
## No channel (deprecated)

 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.5-gke.1057002 is now the default version for cluster creation.
- The following versions are now available:

- 1.33.12-gke.1165000
- 1.33.12-gke.1208000
- 1.34.8-gke.1284000
- 1.35.5-gke.1000004
- 1.35.5-gke.1057002
- 1.35.5-gke.1163012
- 1.35.5-gke.1241004
- 1.35.5-gke.1324000
- 1.36.0-gke.3302001

- The following node versions are now available:

- 1.30.14-gke.2710000
- 1.31.14-gke.2116000
- 1.32.13-gke.1740000
- 1.33.12-gke.1165000
- 1.33.12-gke.1208000
- 1.34.8-gke.1284000
- 1.35.5-gke.1000004
- 1.35.5-gke.1057002
- 1.35.5-gke.1163012
- 1.35.5-gke.1241004
- 1.35.5-gke.1324000
- 1.36.0-gke.3302001

- The following versions are no longer available:

- 1.33.11-gke.1074000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.33.12-gke.1166000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.6-gke.1307000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.3-gke.1389002 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1057000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1163000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1241000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.3009002 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.32 to 1.33.12-gke.1059000
- 1.33 to 1.34.7-gke.1499000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.33 to 1.33.12-gke.1059000
- 1.34 to 1.34.7-gke.1499000
- 1.35 to 1.35.5-gke.1057002
```

説明：
GKEクラスタのバージョンが更新され、新しいバージョンがアップグレードや新規クラスタ作成で利用可能になりました。特に、`No channel`（非推奨）に属するクラスタに関して、バージョン 1.35.5-gke.1057002 がクラスタ作成のデフォルトバージョンとなりました。
1.30.x から 1.36.x までの複数の新しいコントロールプレーンおよびノードバージョンが利用可能です。
一方で、複数のGKEバージョン（例: 1.33.11-gke.1074000, 1.35.3-gke.1389002 など）が非推奨（deprecated）となり、90日以内またはサポート終了時に削除される予定です。
また、自動アップグレードのターゲットバージョンも更新され、メンテナンス除外や非推奨APIなどがなければ、クラスタが新しいマイナーバージョンまたはパッチバージョンに自動アップグレードされる可能性があります。

影響有無：
**影響なし。**
現在利用している Composer 2.7.1 は GKE 1.27.x を基盤としており、本リリースノートに記載されている GKE バージョン (1.30.x 以降) は直接の対象外です。`No channel` はGKEのリリースチャネルとしては推奨されておらず、通常、Composerクラスタはこのチャネルを使用していません。

対処方法：
特段の対処は不要です。将来的にComposerの基盤GKEバージョンが本リリースノート記載のバージョン帯に移行する際には、非推奨となるGKEバージョンに関する情報を参考に、アプリケーションの互換性を確認する必要が生じる可能性があります。

用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloud が提供するマネージド Kubernetes サービス。
*   **No channel (deprecated)**: GKE のリリースチャネルの一つですが、新しいクラスタ作成には推奨されておらず、手動でのバージョン管理が必要になることが多い非推奨のチャネルです。
*   **コントロールプレーン (Control Plane)**: Kubernetes クラスタの管理層で、API サーバ、スケジューラ、コントローラマネージャなどが含まれます。
*   **ノード (Node)**: Kubernetes クラスタでコンテナ化されたワークロードを実行する仮想マシンまたは物理マシンです。
*   **非推奨 (Deprecated)**: 将来的にサポートが終了する予定であることを示します。
*   **自動アップグレード (Auto-upgrade)**: GKE がクラスタのコントロールプレーンとノードを自動的に新しいバージョンにアップグレードする機能です。
*   **メンテナンス除外 (Maintenance Exclusions)**: GKE の自動メンテナンス（アップグレードなど）が実行されない期間を指定する設定です。
*   **APIの非推奨 (Deprecated APIs)**: Kubernetes の API バージョンが非推奨となり、将来のバージョンで削除されることを指します。
*   **パッチバージョン (Patch Version)**: バージョン番号の3番目の数字 (X.Y.Z の Z)。バグ修正やセキュリティアップデートなど、後方互換性のある変更が含まれます。
*   **マイナーバージョン (Minor Version)**: バージョン番号の2番目の数字 (X.Y.Z の Y)。新機能の追加や既存機能の改善など、後方互換性を持つ変更が含まれますが、API の非推奨や削除がある場合もあります。

---

## Security

原文:
```
 This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

 To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

 GKE version
Container-Optimized OS version
Details


1.30.14-gke.2608000
cos-117-18613-613-5
cos-117-18613-613-5 release notes


1.30.14-gke.2710000
cos-117-18613-613-5
cos-117-18613-613-5 release notes


1.31.14-gke.1986000
cos-117-18613-613-7
cos-117-18613-613-7 release notes


1.31.14-gke.2116000
cos-117-18613-613-7
cos-117-18613-613-7 release notes


1.32.13-gke.1657000
cos-117-18613-534-110
cos-117-18613-534-110 release notes


1.32.13-gke.1740000
cos-117-18613-534-110
cos-117-18613-534-110 release notes


1.33.12-gke.1165000
cos-121-18867-381-125
cos-121-18867-381-125 release notes


1.33.12-gke.1208000
cos-121-18867-381-125
cos-121-18867-381-125 release notes


1.34.8-gke.1284000
cos-125-19216-395-7
cos-125-19216-395-7 release notes


1.35.5-gke.1057002
cos-125-19216-395-7
cos-125-19216-395-7 release notes


1.35.5-gke.1163012
cos-125-19216-395-7
cos-125-19216-395-7 release notes


1.35.5-gke.1241004
cos-125-19216-395-7
cos-125-19216-395-7 release notes


1.35.5-gke.1324000
cos-125-19216-395-7
cos-125-19216-395-7 release notes


1.36.0-gke.3302001
cos-129-19506-120-64
cos-129-19506-120-64 release notes
```

説明：
このリリースに含まれる新しい GKE バージョンは、更新された Container-Optimized OS (COS) イメージを使用しています。これらのイメージは、前回の GKE リリース以降に公開されたすべての COS バージョンのセキュリティ修正を累積的に含んでいます。各 COS イメージで解決された特定の脆弱性については、それぞれのリリースノートを参照できます。

影響有無：
**影響あり（ポジティブ）。**
GKE のノードイメージが更新され、セキュリティ修正が含まれるため、Composer 環境の基盤となる GKE ノードのセキュリティが向上します。これは自動アップグレードによって適用されるため、ユーザー側の特別な対応は通常不要です。

対処方法：
特段の対処は不要です。GKE の自動アップグレードによって、セキュリティが強化された COS イメージが適用されます。

用語説明：
*   **Container-Optimized OS (COS)**: Google Cloud で Kubernetes コンテナを実行するために最適化された、セキュリティ強化済みのオペレーティングシステムです。

---

## Change (Stable channel)

原文:
```
 **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.34.7-gke.1499000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:

- 1.33.12-gke.1000000
- 1.34.8-gke.1000000
- 1.35.5-gke.1000004

- The following versions are no longer available in the Stable channel:

- 1.33.11-gke.1074000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.7-gke.1055000
- 1.35.3-gke.1389002 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.32 to 1.33.11-gke.1197000
- 1.33 to 1.34.7-gke.1499000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.33 to 1.33.11-gke.1197000
- 1.34 to 1.34.7-gke.1499000
- 1.35 to 1.35.3-gke.2190000
```

説明：
GKE の Stable チャネルにおいて、バージョン 1.34.7-gke.1499000 が新規クラスタ作成のデフォルトバージョンとなりました。
1.33.x から 1.35.x までの新しいバージョンが利用可能になっています。
また、1.33.11-gke.1074000 や 1.35.3-gke.1389002 など一部のバージョンが非推奨となり、90日以内に削除される予定です。
自動アップグレードのターゲットも更新
# Title: June 25, 2026 
Link: https://docs.cloud.google.com/release-notes#June_25_2026<br>
# BigQuery
## Change
原文: An updated version of the Simba ODBC driver for BigQuery is now available.
[Simba ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_odbc_driver)

説明:
Google Cloud BigQueryに接続するためのSimba ODBC (Open Database Connectivity) ドライバーの新しいバージョンがリリースされました。このドライバーは、BigQueryと他のアプリケーション（例えば、BIツールや分析アプリケーションなど）との間でデータ連携を行うために使用されます。

影響有無:
この変更は、**Simba ODBCドライバーを使用してBigQueryに接続しているシステムやアプリケーションに影響があります**。
BigQueryサービス本体の機能や料金体系、パフォーマンスに直接的な変更はありません。
*   **影響あり:** 現在、BigQuery用のSimba ODBCドライバーを明示的にインストールし、利用している場合。通常、新しいドライバーバージョンでは、バグ修正、パフォーマンス改善、新機能への対応、またはセキュリティパッチが含まれている可能性があります。
*   **影響なし:** Google Cloudコンソール、BigQuery API、gcloud CLI、またはBigQuery用JDBCドライバーなど、ODBCドライバー以外の方法でBigQueryを利用している場合。

対処方法:
1.  **利用状況の確認:** 貴社のシステムにおいてBigQuery用のSimba ODBCドライバーが利用されているかを確認してください。特に、サードパーティ製のBIツールやデータ統合ツールなどがBigQueryに接続する際に利用しているケースが多いです。
2.  **変更内容の把握:** 提供されたリンク（[Simba ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_odbc_driver)）を参照し、更新されたドライバーの具体的な変更点（新機能、修正されたバグ、パフォーマンス改善、セキュリティアップデートなど）を確認してください。通常、ドライバーのダウンロードページやリリースノートに詳細が記載されています。
3.  **互換性テスト:** ドライバーを更新する際は、本番環境への適用前に、開発/ステージング環境で新しいドライバーの互換性と動作を十分にテストしてください。特に、既存のクエリやレポートが正しく動作するかを確認することが重要です。
4.  **ドライバーの更新計画:** テスト結果に基づいて、必要であればドライバーの更新計画を立て、システム停止時間や影響を最小限に抑えながら適用してください。

用語説明:
*   **ODBC (Open Database Connectivity):** 異なるデータベースシステム間でアプリケーションが共通のインターフェースでデータにアクセスできるようにするための標準的なAPI (Application Programming Interface) です。これにより、アプリケーションは特定のデータベースに依存することなくデータにアクセスできます。
*   **Simba Technologies:** データベース接続ドライバーの開発に特化した企業で、BigQueryを含む様々なデータソース用のODBCやJDBC (Java Database Connectivity) ドライバーを提供しています。
*   **BigQuery:** Google Cloudが提供する、フルマネージドでペタバイト規模のデータを分析できるエンタープライズデータウェアハウスサービスです。SQLクエリを非常に高速に実行できます。