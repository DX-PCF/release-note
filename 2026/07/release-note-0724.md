
# Title: July 23, 2026 
Link: https://docs.cloud.google.com/release-notes#July_23_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、ご指定のフォーマットで影響調査の結果を回答します。

---

# BigQuery

## Change

原文:
An updated version of the Simba ODBC driver for BigQuery is now available.

[Simba ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_odbc_driver)

説明：
BigQueryに接続するためのSimba ODBC (Open Database Connectivity) ドライバーの新しいバージョンがリリースされました。このドライバーは、Tableau、Microsoft Excel、Power BIなどの様々なBIツールやアプリケーションからBigQueryデータに接続するために利用されます。新しいバージョンでは、通常、パフォーマンスの向上、バグ修正、新しい機能のサポートなどが含まれています。

影響有無：
**影響は限定的です。**
BigQueryサービス本体ではなく、BigQueryに外部から接続する際に使用するクライアントドライバーの更新に関するアナウンスです。現在、Simba ODBCドライバーを利用してBigQueryに接続しているシステムがある場合、新しいバージョンに更新することで、パフォーマンスの改善や既存のバグの解消が期待できます。既存の古いドライバーが直ちに動作しなくなるわけではありません。

対処方法：
**直ちに対応する必要はありませんが、更新を推奨します。**
1.  現在Simba ODBCドライバーを利用している場合、可能であればテスト環境にて新しいドライバーの動作検証を実施し、問題がなければ本番環境への適用を検討してください。
2.  既存のドライバーで特定の不具合が発生している場合や、より安定した接続、パフォーマンスの向上を求める場合は、更新を強く推奨します。
3.  新しいBIツールやアプリケーションをBigQueryに接続する際は、常に最新のドライバーを使用することが推奨されます。

用語説明：
*   **ODBC (Open Database Connectivity):** データベースに接続するための標準的なアプリケーションプログラミングインターフェース（API）です。異なるデータベースシステムに対して共通のインターフェースを提供し、アプリケーションが特定のデータベースに依存することなくデータにアクセスできるようにします。
*   **Simba ODBC driver for BigQuery:** Simba Technologies社が提供する、ODBC規格に準拠したBigQuery専用のドライバーソフトウェアです。このドライバーをPCやサーバーにインストールすることで、一般的なBIツールやカスタムアプリケーションがODBC経由でBigQueryのデータに接続し、クエリを実行できるようになります。
*   **BIツール (Business Intelligence Tool):** 企業が蓄積した膨大なデータを分析し、意思決定に役立つ情報（レポート、ダッシュボード、グラフなど）を可視化するためのソフトウェアやサービスのことです。例えば、Tableau、Microsoft Power BI、Lookerなどが該当します。
# Title: July 21, 2026 
Link: https://docs.cloud.google.com/release-notes#July_21_2026<br>
恐れ入りますが、提供された情報には具体的なリリースノートの内容が記載されていません。

`原文: release note.` の部分に、Cloud SDKに関する実際のリリースノートの本文（英語）を追記していただくことで、内容を分析し、ご指定の形式で影響調査の回答を作成することが可能です。

リリースノートの具体的な内容をご提供いただけますでしょうか。
# Title: July 20, 2026 
Link: https://docs.cloud.google.com/release-notes#July_20_2026<br>
## BigQuery
### Issue
原文: Lakehouse for Apache Iceberg: Data Products with special characters, such as "/" or "-", are not supported and will not be available in BigQuery even if shared from SAP BDC to BigQuery. If you share a Data Product with special characters, this could cause the stop a refresh and require re-enrollment. Known SAP systems producing these Data Products include SAP Business Warehouse (BW) sources and SAP SuccessFactors.
説明: Apache Iceberg用のBigQuery Lakehouse機能において、SAP BDC (Business Data Catalog) からBigQueryに共有されるデータプロダクト名に、スラッシュ("/")やハイフン("-")などの特殊文字が含まれている場合、BigQuery側でそのデータプロダクトが利用できないという問題があります。さらに、特殊文字を含むデータプロダクトを共有すると、データのリフレッシュが停止し、再登録が必要になる可能性があります。この問題を引き起こすデータプロダクトを生成するSAPシステムとして、SAP Business Warehouse (BW) やSAP SuccessFactorsが知られています。
影響有無: BigQueryのLakehouse for Apache Iceberg機能を利用し、SAP BDCからデータプロダクトを共有しており、そのデータプロダクト名に特殊文字（特に"/"や"-"）が含まれている場合、データが利用できない、またはリフレッシュが停止する影響があります。現在のシステムがこの条件に該当しない場合は、直接的な影響はありません。
対処方法:
1. 現在のデータ共有フローで、SAP BDCからBigQueryに共有されるデータプロダクト名に特殊文字が含まれていないか確認してください。
2. もし特殊文字が含まれている場合は、データプロダクト名を特殊文字を含まない形に変更できないか、SAP側の設定を見直してください。
3. 既にリフレッシュが停止しているなどの問題が発生している場合は、該当するデータプロダクトを再登録する必要がある可能性があります。

用語説明:
*   **Lakehouse for Apache Iceberg**: BigQueryがApache Icebergオープンテーブルフォーマットをサポートし、データレイクとデータウェアハウスの統合的な分析環境を提供する機能。データレイクの柔軟性とデータウェアハウスの構造化されたクエリ機能を組み合わせることを目指します。
*   **SAP BDC (Business Data Catalog)**: SAPシステムにおけるビジネスデータのメタデータ管理やデータソース連携のフレームワーク。Google Cloudとのデータ連携において、データ共有の起点となる可能性があります。
*   **Data Product**: 特定のビジネスニーズを満たすために準備された、キュレーション済みのデータセットやAPIなどのデータ資産。ここではSAPシステムからBigQueryへ共有されるデータの論理的な単位を指します。

## Compute Engine
### Deprecated
原文: Encrypting disks, snapshots, images, and machine images with customer-supplied encryption keys (CSEKs) is deprecated and will be disabled on July 20, 2027. For more information and alternatives to CSEKs for your Compute Engine resources, see Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine.
説明: Compute Engineにおいて、ユーザー提供の暗号化キー（CSEK: Customer-Supplied Encryption Keys）を使用してディスク、スナップショット、イメージ、マシンイメージを暗号化する機能が非推奨となりました。この機能は2027年7月20日に完全に無効化されます。CSEKの代替手段や詳細については、提供されているドキュメントを参照するよう案内されています。
影響有無: 現在のCompute Engine環境でCSEKを使用してディスク、スナップショット、イメージ、またはマシンイメージを暗号化している場合、直接的な影響があります。2027年7月20日までに代替の暗号化方法へ移行する必要があります。CSEKを使用していない場合は影響ありません。
対処方法:
1.  現在のCompute Engineリソース（永続ディスク、スナップショット、カスタムイメージ、マシンイメージ）がCSEKで暗号化されているかどうかを確認してください。
2.  CSEKを使用しているリソースがある場合、2027年7月20日までに以下のいずれかの代替手段への移行を計画し、実行してください。
    *   **Customer-Managed Encryption Keys (CMEK)**: Cloud Key Management Service (Cloud KMS) で管理されるキーを使用する方法。推奨される代替策であり、より容易なキー管理が可能です。
    *   **Google-managed encryption keys**: Googleがデフォルトで管理するキーを使用する方法。
3.  移行には、既存リソースの再暗号化や、新しいキーで暗号化されたリソースの作成と置き換えが含まれる可能性があります。十分なテストと計画を実施してください。

用語説明:
*   **CSEK (Customer-Supplied Encryption Keys)**: ユーザーが独自の暗号化キーを生成し、Google Cloudに提供してCompute Engineのリソース（ディスクなど）を暗号化する機能。キーはGoogleによって保存されず、使用時にユーザーから提供される必要があります。
*   **CMEK (Customer-Managed Encryption Keys)**: Google Cloud Key Management Service (Cloud KMS) を利用して、ユーザーが暗号化キーを生成・管理し、Google Cloudリソースの暗号化に使用する機能。CSEKと比較して、キー管理がGoogle Cloud上で完結し、より使いやすいです。
*   **ディスク、スナップショット、イメージ、マシンイメージ**: Compute Engineにおける主要なストレージおよびVMデプロイ関連リソース。ディスクはVMにアタッチされる永続ストレージ、スナップショットはディスクのポイントインタイムコピー、イメージはVMを起動するためのテンプレート、マシンイメージはVMインスタンス全体の状態（ディスク、メタデータなど）をキャプチャしたものです。

## Google Kubernetes Engine
### Deprecated
原文: To improve security, Ubuntu node images in GKE version 1.37 and later don't pre-install the `vulkan-tools` package. If you run Vulkan diagnostic tools (such as `vulkaninfo`) directly on GKE Ubuntu hosts, then you must manually install the `vulkan-tools` package. This change doesn't affect containerized GPU/Vulkan workloads.
説明: セキュリティを向上させるため、GKEのUbuntuノードイメージにおいて、バージョン1.37以降では`vulkan-tools`パッケージがデフォルトでプリインストールされなくなります。もしGKEのUbuntuホスト上で直接Vulkan診断ツール（例: `vulkaninfo`コマンド）を実行する必要がある場合は、手動で`vulkan-tools`パッケージをインストールする必要があります。この変更は、コンテナ内で実行されるGPU/Vulkanワークロードには影響しません。
影響有無: GKEクラスタのノードイメージとしてUbuntuを使用しており、かつGKEのバージョンが1.37以降にアップグレードされる、または既に1.37以降である場合、影響があります。特に、GKEノードのOSレベルで直接`vulkan-tools`（例: `vulkaninfo`）を使用している診断や運用ワークフローがある場合に影響が出ます。コンテナ内でVulkanを利用する通常のGPUワークロードには影響ありません。
対処方法:
1.  GKEクラスタがバージョン1.37以降のUbuntuノードイメージを使用する予定があるか、または既にそうなっているか確認してください。
2.  GKEノードのOS環境で直接`vulkan-tools`パッケージ（例: `vulkaninfo`コマンド）に依存する作業やスクリプトがないか確認してください。
3.  もし必要な場合は、ノードの起動スクリプトやカスタムノードイメージの作成プロセスにおいて、`vulkan-tools`パッケージ（例: `sudo apt-get update && sudo apt-get install -y vulkan-tools`）を手動でインストールするステップを追加してください。
4.  コンテナ化されたGPU/Vulkanワークロードに関しては、特別な対処は不要です。

用語説明:
*   **Vulkan**: クロスプラットフォームで低オーバーヘッドな高性能グラフィックスおよびコンピュートAPI。主に3DグラフィックスやGPGPU (General-purpose computing on Graphics Processing Units) アプリケーションに使用されます。
*   **`vulkan-tools`パッケージ**: Vulkan APIの開発、デバッグ、診断に役立つユーティリティツール群を含むソフトウェアパッケージ。例えば、`vulkaninfo`コマンドはシステムにインストールされているVulkanの機能やドライバ情報を表示します。
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを自動化します。
*   **Ubuntu node images**: GKEクラスタのワーカーノードとして使用される、Canonical社のUbuntu Linuxをベースとした仮想マシンイメージ。