
# Title: December 03, 2025 
Link: https://docs.cloud.google.com/release-notes#December_03_2025<br>
Google Cloudのインフラエンジニアとして、ご提供いただいたリリースノートに基づき、製品ごとの影響分析と推奨される対応を以下の通りご説明いたします。

---

# Cloud Service Mesh

## Security
原文:
The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.6-asm.7 is rolling out to the rapid release channel.
- 1.20.8-asm.59 is rolling out to the regular release channel.
- 1.19.10-asm.54 is rolling out to the stable release channel.
These patch releases contain the fix for the managed Cloud Service Mesh security vulnerability listed in GCP-2025-073.
[GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073)

説明：
マネージドCloud Service Meshの各リリースチャネル（rapid、regular、stable）において、セキュリティ脆弱性「GCP-2025-073」の修正を含むパッチリリースが順次展開されています。これにより、各チャネルの対応バージョン（1.21.6-asm.7、1.20.8-asm.59、1.19.10-asm.54）が更新されます。

影響有無：
**影響あり (ポジティブな影響)**。
本リリースはセキュリティ脆弱性の修正であるため、利用中のマネージドCloud Service Mesh環境のセキュリティ態勢が自動的に強化されます。ユーザー側での直接的な操作は不要です。

対処方法：
マネージドサービスであるため、通常、ユーザーによる明示的な対処は不要です。Cloud Service Meshのリリースチャネルポリシーに従い、自動的にアップデートが適用されます。ただし、アップグレードによるサービスへの潜在的な影響を最小限に抑えるため、ご自身の環境が属するリリースチャネルのメンテナンスウィンドウと、アップデート適用後のシステムの健全性を監視することをお勧めします。

用語説明：
*   **Cloud Service Mesh**: Google Cloud上で動作するIstioベースのサービスメッシュソリューション。マネージドとin-clusterの2つのデプロイメントモデルがあります。
*   **リリースチャネル (rapid, regular, stable)**: Google Cloudのサービスやプロダクトの更新頻度と安定性を示す区分です。rapidは最新機能が早期に提供される傾向がありますが、stableは最も安定性が重視されます。
*   **GCP-2025-073**: 特定のセキュリティ脆弱性を識別するためのGoogle Cloud独自の脆弱性IDです。詳細情報は提供されたリンクで確認できます。

## Security
原文:
**1.27.4-asm.1 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the security vulnerabilities listed in GCP-2025-073. For details on upgrading Cloud Service Mesh, refer to Upgrade Cloud Service Mesh. Cloud Service Mesh v1.27.4-asm.1 uses Envoy v1.35.7.
[GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073)
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
In-cluster Cloud Service Mesh向けに、セキュリティ脆弱性「GCP-2025-073」の修正を含むバージョン1.27.4-asm.1が利用可能になりました。このバージョンでは、Envoyプロキシのバージョンは1.35.7が使用されています。

影響有無：
**影響あり (セキュリティ向上、ユーザーによる作業が必要)**。
in-cluster Cloud Service Meshをご利用の場合、このパッチリリースを適用することで、既知のセキュリティ脆弱性に対する保護が強化されます。ただし、マネージドサービスとは異なり、ユーザーが明示的にアップグレード作業を実行する必要があります。

対処方法：
利用中のin-cluster Cloud Service Mesh環境を、提供されたドキュメント「Upgrade Cloud Service Mesh」を参照し、バージョン1.27.4-asm.1へアップグレードすることを強く推奨します。アップグレード作業は、本番環境に適用する前に十分なテスト環境での検証を実施してください。

用語説明：
*   **In-cluster Cloud Service Mesh**: GKEクラスタ内にIstioコントロールプレーンを自身でデプロイ・管理するデプロイメントモデルです。マネージドとは異なり、コントロールプレーンのアップグレードやパッチ適用はユーザーの責任で行われます。
*   **Envoy**: Istioにおいてデータプレーンのプロキシとして機能する高性能なオープンソースのエッジプロキシおよびサービスプロキシです。

## Security
原文:
**1.25.6-asm.1 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the security vulnerabilities listed in GCP-2025-073. For details on upgrading Cloud Service Mesh, refer to Upgrade Cloud Service Mesh. Cloud Service Mesh v1.25.6-asm.1 uses Envoy v1.33.13.
[GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073)
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade)

説明：
In-cluster Cloud Service Mesh向けに、セキュリティ脆弱性「GCP-2025-073」の修正を含むバージョン1.25.6-asm.1が利用可能になりました。このバージョンでは、Envoyプロキシのバージョンは1.33.13が使用されています。

影響有無：
**影響あり (セキュリティ向上、ユーザーによる作業が必要)**。
in-cluster Cloud Service Meshをご利用の場合、このパッチリリースを適用することで、既知のセキュリティ脆弱性に対する保護が強化されます。ただし、マネージドサービスとは異なり、ユーザーが明示的にアップグレード作業を実行する必要があります。

対処方法：
利用中のin-cluster Cloud Service Mesh環境を、提供されたドキュメント「Upgrade Cloud Service Mesh」を参照し、バージョン1.25.6-asm.1へアップグレードすることを強く推奨します。アップグレード作業は、本番環境に適用する前に十分なテスト環境での検証を実施してください。

## Security
原文:
**1.26.7-asm.1 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the security vulnerabilities listed in GCP-2025-073. For details on upgrading Cloud Service Mesh, refer to Upgrade Cloud Service Mesh. Cloud Service Mesh v1.26.7-asm.1 uses Envoy v1.34.11.
[GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073)
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade)

説明：
In-cluster Cloud Service Mesh向けに、セキュリティ脆弱性「GCP-2025-073」の修正を含むバージョン1.26.7-asm.1が利用可能になりました。このバージョンでは、Envoyプロキシのバージョンは1.34.11が使用されています。

影響有無：
**影響あり (セキュリティ向上、ユーザーによる作業が必要)**。
in-cluster Cloud Service Meshをご利用の場合、このパッチリリースを適用することで、既知のセキュリティ脆弱性に対する保護が強化されます。ただし、マネージドサービスとは異なり、ユーザーが明示的にアップグレード作業を実行する必要があります。

対処方法：
利用中のin-cluster Cloud Service Mesh環境を、提供されたドキュメント「Upgrade Cloud Service Mesh」を参照し、バージョン1.26.7-asm.1へアップグレードすることを強く推奨します。アップグレード作業は、本番環境に適用する前に十分なテスト環境での検証を実施してください。

---

# Google Cloud Armor

## Security
原文:
The Cloud Armor `cve-canary` rules include the `google-mrs-v202512-id000001-rce` signature to help detect and mitigate CVE-2025-55182.
For more information, see Cloud Armor preconfigured WAF rules overview.
[`google-mrs-v202512-id000001-rce` signature](https://docs.cloud.google.com/armor/docs/waf-rules#cves_and_other_vulnerabilities)
[CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182)
[Cloud Armor preconfigured WAF rules overview](https://docs.cloud.google.com/armor/docs/waf-rules)

説明：
Google Cloud Armorの`cve-canary`ルールセットに、新しいシグネチャ「`google-mrs-v202512-id000001-rce`」が追加されました。このシグネチャは、特定の脆弱性であるCVE-2025-55182を検出および緩和するために役立ちます。

影響有無：
**影響あり (ポジティブな影響)**。
Google Cloud Armorをご利用の場合、WAFルールが自動的に更新され、新しいシグネチャが適用されることで、CVE-2025-55182に関連するリモートコード実行（RCE）攻撃からの保護が強化されます。ユーザーによる追加の設定や作業は不要です。

対処方法：
特になし。Cloud ArmorのマネージドWAFルールは自動的に更新が適用されます。現在`cve-canary`ルールが有効になっていることを確認するだけで十分です。

用語説明：
*   **Google Cloud Armor**: Google Cloud上で提供されるDDoS攻撃防御およびWeb Application Firewall (WAF) サービスです。
*   **`cve-canary` rules**: Cloud Armorが提供するWAFルールのカテゴリの一つで、新しく発見された脆弱性や攻撃手法に迅速に対応するために設計されています。
*   **WAF (Web Application Firewall)**: Webアプリケーションに対する攻撃（SQLインジェクション、クロスサイトスクリプティングなど）を検知し、防御する役割を担うファイアウォールです。
*   **CVE-2025-55182**: 国際的に付与された特定のセキュリティ脆弱性の識別子です。
*   **RCE (Remote Code Execution)**: 遠隔から悪意のあるコードを実行できるセキュリティ脆弱性のカテゴリです。

---

# Google Kubernetes Engine

## Issue
原文:
Starting with version 1.33.2-gke.4655000, the GCSFuse CSI Driver automatically applies performance-tuning defaults for Cloud Storage FUSE volumes used on nodes with high-performance machine types.
However, in GKE versions 1.34.1-gke.1431000 to 1.34.1-gke.3403001, these defaults are not being applied. This is due to an issue where GCSFuse fails to recognize the machine type from the configuration file provided by the GCSFuse CSI Driver.
[high-performance machine types](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations)
To apply the performance defaults, explicitly set the machine-type as a gcsfuse mount option. Use the command-line flag format, with the key and value separated by an equals sign (`=`).
For example: `machine-type=n2-standard-4`
Ensure the Pod using the GCSFuse volume is scheduled on a node that matches the specified machine type. These settings are optimized for high-performance machine types and might not be suitable for other node types. For more information on scheduling, see the Kubernetes documentation on assigning Pods to Nodes.
[assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

説明：
GKEバージョン1.33.2-gke.4655000以降では、高性能マシンタイプを使用するノード上のCloud Storage FUSEボリュームに対して、GCSFuse CSI Driverが自動的にパフォーマンスチューニングのデフォルト設定を適用するようになりました。しかし、GKEバージョン1.34.1-gke.1431000から1.34.1-gke.3403001の範囲では、GCSFuseがCSI Driverが提供する設定ファイルからマシンタイプを認識できない問題により、これらのデフォルト設定が適用されないという問題が発生しています。この問題の回避策として、`gcsfuse`マウントオプションとして`machine-type`を明示的に設定することが推奨されています。

影響有無：
**影響あり (パフォーマンスの潜在的低下)**。
もし、現在ご利用のGKEクラスターバージョンが1.34.1-gke.1431000から1.34.1-gke.3403001の範囲であり、かつ高性能マシンタイプのノードでGCSFuse CSI Driverを介してCloud Storage FUSEボリュームを使用している場合、期待されるパフォーマンスチューニングが自動的に適用されず、I/O性能が低下する可能性があります。Google Cloud Composer 2.7.1はGKE上で動作するため、Composer環境でGCSFuse CSI Driverを利用している場合は注意が必要です。

対処方法：
上記の影響を受けるGKEバージョンを使用している場合、GCSFuse CSI Driverを利用してCloud Storage FUSEボリュームをマウントするPodの定義に、以下の`gcsfuse`マウントオプションを明示的に追加してください。
例: `machine-type=n2-standard-4`
また、Podが指定した`machine-type`に合致する高性能マシンタイプのノードにスケジュールされるよう、Podの`nodeSelector`や`affinity`設定を用いてノードへの割り当てを適切に構成することも重要です。
将来的に問題が修正されたGKEバージョンへのアップグレードを検討してください。

用語説明：
*   **GCSFuse CSI Driver**: Google Kubernetes Engine (GKE) において、Google Cloud Storage (GCS) バケットをKubernetesのPersistentVolume (PV) として動的にプロビジョニングし、PodからファイルシステムとしてアクセスできるようにするためのContainer Storage Interface (CSI) ドライバーです。
*   **Cloud Storage FUSE**: Google Cloud Storageのバケットをファイルシステムとしてマウントすることを可能にするオープンソースアダプターであるGCSFuseを利用した機能です。これにより、アプリケーションはGCSを通常のファイルシステムのように扱えます。
*   **高性能マシンタイプ**: GCE (Google Compute Engine) のVMインスタンスタイプのうち、特定のワークロード（高I/O、計算集約型など）向けに最適化された高性能なインスタンス群を指します。
*   **Podのスケジュール**: Kubernetesにおいて、Podがどのノード上で実行されるかを決定するプロセスです。`nodeSelector`や`affinity`などの設定により、特定のノードにPodを配置する制約を設けることができます。

---

# Spanner

## Changed
原文:
String values in Spanner Studio query results are now enclosed in double quotes, providing a clear visual cue to differentiate string values from other data types. This enhancement is for display purposes only and does not affect how data is exported or accessed.
[Spanner Studio query results](https://docs.cloud.google.com/spanner/docs/manage-data-using-console#create-modify-query-data)

説明：
Spanner Studioのクエリ結果表示において、文字列型の値が二重引用符で囲まれるようになりました。この変更は、文字列値を他のデータ型（例: 数値）と視覚的に区別しやすくするためのものです。この強化は表示のみに影響し、データの出力形式やプログラムからのデータアクセス方法には影響しません。

影響有無：
**影響なし (ポジティブなUX改善)**。
本変更はSpanner Studioのユーザーインターフェース（UI）における表示方法の改善であり、Spannerの実際のデータ、既存のSQLクエリ、API、データのエクスポート/インポート機能など、あらゆるプログラム的な動作やワークロードには影響を与えません。

対処方法：
特になし。ユーザー側での対応は不要です。

用語説明：
*   **Spanner Studio**: Google Cloudコンソール内でGoogle Cloud Spannerのインスタンスに対してSQLクエリを実行したり、スキーマを参照・管理したりするためのグラフィカルユーザーインターフェース（GUI）ツールです。
*   **二重引用符**: プログラミング言語やデータベースのSQLなどで、文字列リテラルを定義する際に使用される区切り記号です。
# Title: December 02, 2025 
Link: https://docs.cloud.google.com/release-notes#December_02_2025<br>
はい、承知いたしました。Google Cloud のインフラエンジニアとして、提供されたリリースノートに対する影響調査と回答を行います。

---

# BigQuery

## Changed

原文:
An updated version of the ODBC driver for BigQuery is now available.
[ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_odbc_driver)

説明：
BigQuery に接続するための ODBC (Open Database Connectivity) ドライバの新しいバージョンがリリースされ、利用可能になりました。ODBC ドライバは、Tableau や Power BI といったBIツール、あるいはカスタムアプリケーションなどから BigQuery のデータにアクセスするために使用されます。ドライバの更新には通常、パフォーマンスの改善、バグ修正、セキュリティの強化、新機能への対応などが含まれます。

影響有無：
**影響の可能性あり**

*   **影響ありと判断されるケース**: BigQuery ODBCドライバを使用して、BIツール（例: Tableau Desktop, Power BI Desktop, Qlik Senseなど）やカスタムアプリケーションからBigQueryに接続し、データ分析やレポート作成を行っている場合。
    *   既存のドライバを使い続けている限り、直ちにサービスが停止するなどの直接的な影響はありません。
    *   しかし、新しいドライババージョンに含まれるパフォーマンス改善、バグ修正、セキュリティパッチの恩恵を受けられません。また、将来的に古いドライバでは利用できない新しいBigQuery機能が出た場合、接続がサポートされなくなる可能性があります。
    *   稀に、ドライバのメジャーアップデートで非互換性のある変更（Breaking Change）が含まれることがありますが、リリースノートからはその具体的な情報はありません。通常は互換性が維持されますが、念のため詳細な変更ログを確認することが推奨されます。

*   **影響なしと判断されるケース**: BigQueryを、ODBCドライバ経由で利用していない場合（例: BigQuery コンソール、bq コマンドラインツール、Google Cloud クライアントライブラリ、dbt-bigquery、Apache Spark など、ドライバを直接利用しない接続方法を使用している場合）。

対処方法：
BigQuery ODBCドライバを利用しているかどうかに応じて、以下の対応を推奨します。

1.  **BigQuery ODBCドライバを利用している場合**:
    *   現在利用中のODBCドライバのバージョンと、今回の更新されたドライバのバージョンにおける変更点（リリースノートやドライバの公式ドキュメントにある変更ログ）を確認してください。
    *   可能であれば、開発環境やテスト環境で最新版のODBCドライバを導入し、既存の接続やクエリが正常に動作するか、パフォーマンスに変化がないかなどの互換性テストおよび機能テストを十分に行うことを強く推奨します。
    *   テスト結果に基づき、本番環境へのアップグレード計画を策定し、適用を検討してください。最新版へのアップグレードは、パフォーマンス向上、セキュリティ強化、バグ修正の恩恵を受けるために推奨されます。
2.  **BigQuery ODBCドライバを利用していない場合**:
    *   特に対処は不要です。

用語説明：
*   **ODBC (Open Database Connectivity)**: さまざまなデータベース管理システム（DBMS）へのアクセスを可能にするための標準的なアプリケーションプログラミングインターフェース（API）です。アプリケーションが特定のデータベースの種類に依存することなく、SQLクエリを通じてデータにアクセスできるようになります。
*   **BigQuery ODBC Driver**: Google BigQueryデータウェアハウスへのODBC接続を可能にするソフトウェアコンポーネントです。これにより、Microsoft Excel, Tableau, Power BI, Qlik Senseなどの一般的なBIツールや、ODBCをサポートするカスタムアプリケーションからBigQueryのデータにアクセスし、クエリを実行できます。