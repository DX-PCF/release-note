
# Title: July 21, 2026 
Link: https://docs.cloud.google.com/release-notes#July_21_2026<br>
Cloud SDKのリリースノート分析をご依頼いただきありがとうございます。

ご提供いただいた情報では、`Cloud SDK` の `Change` カテゴリに関するリリースノートの**原文（英文）が不足**しております。

リリースノートの原文が提供され次第、ご要望のフォーマットに沿って、構築済みサービスへの影響有無、対処方法、および用語説明を含めた詳細な調査と回答をいたします。

お手数ですが、Cloud SDKのリリースノートの原文をご提示いただけますでしょうか。
# Title: July 20, 2026 
Link: https://docs.cloud.google.com/release-notes#July_20_2026<br>
## BigQuery
### Issue
原文: `*Lakehouse for Apache Iceberg*: Data Products with special characters, such as "/" or "-", are not supported and will not be available in BigQuery even if shared from SAP BDC to BigQuery. If you share a Data Product with special characters, this could cause the stop a refresh and require re-enrollment. Known SAP systems producing these Data Products include SAP Business Warehouse (BW) sources and SAP SuccessFactors.`

説明:
SAP Data Bridge Connector (BDC) を介してSAPシステムからBigQueryへデータ連携を行う際に、Apache IcebergベースのLakehouse環境において、特殊文字（例: `/`や`-`）を含む「Data Product」はサポートされず、BigQuery側で利用できません。もし特殊文字を含むData Productが共有された場合、データのリフレッシュ処理が停止し、再登録が必要になる可能性があります。この問題が確認されているSAPシステムには、SAP Business Warehouse (BW) のデータソースやSAP SuccessFactorsが含まれます。

影響有無:
*   **影響なし**: 貴社の環境でBigQueryのLakehouse for Apache Iceberg機能を利用しておらず、特にSAPシステム（SAP BW、SAP SuccessFactorsなど）からBigQueryへのデータ連携をSAP BDC経由で行っていない場合。
*   **影響あり**: 貴社の環境でBigQueryのLakehouse for Apache Iceberg機能を利用しており、SAPシステムからSAP BDC経由でBigQueryへのデータ連携を行っている場合。特に、連携するData Product名に特殊文字が含まれている場合に影響を受けます。データリフレッシュの停止や、Data Productの再登録が必要になるリスクがあります。

対処方法:
*   **該当する場合**: SAPシステムからBigQueryに連携するData Productの命名規則を見直し、特殊文字（`/`、`-`など）の使用を避けるように変更してください。すでに特殊文字を含むData Productを連携している場合は、リフレッシュ状況を監視し、必要に応じてData Productの名称変更と再登録を検討してください。

用語説明:
*   **Lakehouse for Apache Iceberg**: データレイクとデータウェアハウスの利点を組み合わせたアーキテクチャで、オープンソースのテーブルフォーマットであるApache Icebergを利用して、データレイク上の構造化・非構造化データをBigQueryで効率的に扱えるようにする機能です。
*   **Data Product**: データメッシュアーキテクチャの概念で、特定のビジネス目的のために公開・共有される、独立した利用可能なデータの単位を指します。
*   **SAP BDC (SAP Data Bridge Connector)**: SAPの文脈で使用されることが想定されるデータ連携ツールまたはコンポーネントで、SAPシステムと外部システム間でのデータ転送を可能にします。
*   **SAP Business Warehouse (BW)**: SAPが提供する統合されたデータウェアハウスソリューションで、ビジネスインテリジェンスのためのデータ分析とレポート作成をサポートします。
*   **SAP SuccessFactors**: SAPが提供するクラウドベースの人事管理 (HR) ソリューションスイートです。

## Compute Engine
### Deprecated
原文: `Encrypting disks, snapshots, images, and machine images with customer-supplied encryption keys (CSEKs) is deprecated and will be disabled on July 20, 2027. For more information and alternatives to CSEKs for your Compute Engine resources, see Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine.`

説明:
Compute Engineのディスク、スナップショット、イメージ、およびマシンイメージに対するカスタマー指定の暗号鍵（CSEK: Customer-Supplied Encryption Keys）を使用した暗号化機能が非推奨となり、2027年7月20日には無効化される予定です。Compute EngineリソースにおけるCSEKの代替手段については、関連ドキュメントを参照してください。

影響有無:
*   **影響なし**: 現在、Compute Engineのディスク、スナップショット、カスタムイメージ、またはマシンイメージの暗号化にCSEKを使用していない場合。
*   **影響あり**: 現在、Compute Engineリソースの暗号化にCSEKを使用している場合。2027年7月20日以降はCSEKが利用できなくなるため、この期日までに代替の暗号化方法へ移行する必要があります。

対処方法:
*   **該当する場合**: CSEKを利用しているCompute Engineリソースを特定し、Cloud Key Management Service (Cloud KMS) を使用したカスタマー管理の暗号鍵（CMEK: Customer-Managed Encryption Keys）や、Google管理の暗号化など、他の暗号化オプションへの移行を計画・実行してください。移行計画は、2027年7月20日の無効化期日を考慮して、余裕を持って実施することが推奨されます。詳細はリンクされたドキュメントを参照してください。

用語説明:
*   **CSEK (Customer-Supplied Encryption Keys)**: Google Cloudにおいて、ユーザー自身が生成・管理し、APIリクエスト時に提供することでデータを暗号化・復号する鍵です。鍵マテリアルはGoogleのインフラストラクチャには永続的に保存されず、使用時のみ提供されます。
*   **CMEK (Customer-Managed Encryption Keys)**: Google Cloud KMSを通じてユーザーが暗号鍵を管理し、それをGoogle Cloudの様々なサービスのリソースの暗号化に使用する機能です。鍵の生成、管理、アクセス制御をユーザーが行いますが、鍵マテリアル自体はGoogle Cloud KMS内で安全に管理されます。
*   **Google管理の暗号化**: ユーザーが特別な設定を行わなくても、Google Cloudがデフォルトでデータに適用する暗号化です。鍵の管理はGoogleによって行われます。

## Google Kubernetes Engine
### Deprecated
原文: `To improve security, Ubuntu node images in GKE version 1.37 and later don't pre-install the vulkan-tools package. If you run Vulkan diagnostic tools (such as vulkaninfo) directly on GKE Ubuntu hosts, then you must manually install the vulkan-tools package. This change doesn't affect containerized GPU/Vulkan workloads.`

説明:
セキュリティを向上させるため、GKEバージョン1.37以降のUbuntuノードイメージでは、`vulkan-tools`パッケージがデフォルトでプリインストールされなくなります。もしGKEのUbuntuホスト上でVulkan診断ツール（例: `vulkaninfo`）を直接実行する必要がある場合は、手動で`vulkan-tools`パッケージをインストールする必要があります。この変更は、コンテナ化されたGPU/Vulkanワークロードには影響しません。

影響有無:
*   **影響なし**: GKEを利用しているが、GKEのUbuntuノードイメージのバージョン1.37以降を使用する予定がなく、かつノードのホストOS上で直接Vulkan診断ツールを実行していない場合。また、コンテナ内でGPU/Vulkanワークロードを実行している場合は影響を受けません。
*   **影響あり**: GKEのUbuntuノードイメージのバージョン1.37以降にアップグレードする予定があり、かつノードのホストOS上で直接`vulkan-tools`パッケージに含まれる診断ツール（例: `vulkaninfo`）を実行する運用を行っている場合。

対処方法:
*   **該当する場合**: GKEのUbuntuノードのホストOS上でVulkan診断ツールを継続して使用する必要がある場合は、ノードの起動スクリプトやプロビジョニングプロセスに`vulkan-tools`パッケージの手動インストールコマンド（例: `sudo apt-get update && sudo apt-get install -y vulkan-tools`）を追加することを検討してください。ほとんどのGPU/Vulkanワークロードはコンテナ内で実行されるため、直接的な影響を受けるケースは限られます。

用語説明:
*   **Vulkan**: Khronos Groupによって開発された、低オーバーヘッドかつクロスプラットフォームな3DグラフィックスおよびコンピューティングAPIです。GPUへのより直接的なアクセスを提供し、高性能なアプリケーション開発を可能にします。
*   **`vulkan-tools`パッケージ**: Vulkan APIを利用するアプリケーションの開発やデバッグ、診断に役立つツール群を含むパッケージです。`vulkaninfo`コマンドは、システムのVulkan対応状況やGPUの情報を表示するために使用されます。
*   **GKE Ubuntuノードイメージ**: Google Kubernetes Engineクラスタのワーカーノードとして使用される、Ubuntu Linuxベースの仮想マシンイメージです。GKEによって管理され、Kubernetesのコンポーネントや必要なドライバ、ツールが組み込まれています。