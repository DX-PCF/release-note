
# Title: May 22, 2026 
Link: https://docs.cloud.google.com/release-notes#May_22_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、構築済みのサービスへの影響調査結果をご報告いたします。

現在利用中のサービスにおいて、Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) のバージョンを利用しているとご申告いただいておりますが、今回のリリースノートは Apigee X に関するものであり、Google Cloud Composer2 への直接的な影響はございません。

---

# Apigee X

## Announcement

### 原文: Apigee Emulator v2.0.0

On May 22, 2026, we released Apigee Emulator version 2.0.0.

Starting with this release, the Apigee Emulator is versioned and released independently from Apigee hybrid. This enables faster delivery of security patches and updates without waiting for hybrid release cycles. The emulator image continues to be available at [Google Artifact Registry](https://console.cloud.google.com/artifacts/docker/apigee-release/us/gcr.io/hybrid%2Fapigee-emulator).
To use the new version, update the emulator version in your VS Code Cloud Code settings to `2.0.0`. See [Manage the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#choose_the_emulator_version) for details.

### 説明：
Apigee Emulator のバージョン 2.0.0 がリリースされました。このバージョンから、Apigee Emulator は Apigee Hybrid とは独立してバージョン管理およびリリースされるようになります。これにより、Apigee Hybrid のリリースサイクルを待つことなく、セキュリティパッチやアップデートがより迅速に提供されるようになります。エミュレータのイメージは引き続き Google Artifact Registry で利用可能です。新しいバージョンを使用するには、VS Code Cloud Code の設定でエミュレータのバージョンを `2.0.0` に更新する必要があります。

### 影響有無：
**影響あり（ポジティブな影響、開発環境限定）**
*   **理由**: 本番環境の Apigee X サービス自体への直接的な影響はありません。Apigee Emulator は API 開発者がローカル環境で API プロキシの開発やテストを行う際に使用するツールであり、主に開発環境に影響します。独立したリリースサイクルにより、セキュリティアップデートの適用が早まるため、開発環境のセキュリティ体制が強化されます。

### 対処方法：
Apigee Emulator を開発環境で利用している場合、VS Code Cloud Code の設定を開き、エミュレータのバージョンを `2.0.0` に更新することを推奨します。

### 用語説明：
*   **Apigee X**: Google Cloud が提供する、API の設計、保護、デプロイ、監視、管理を行うためのAPI管理プラットフォームです。
*   **Apigee Emulator**: Apigee の API プロキシをローカル環境でシミュレートし、API 開発者が開発やテストを効率的に行えるようにするツールです。
*   **Apigee Hybrid**: Apigee のデプロイオプションの一つで、Google Cloud 上のコントロールプレーンと、オンプレミスまたは他のクラウド環境で実行されるランタイムを組み合わせたものです。
*   **VS Code Cloud Code**: Visual Studio Code の拡張機能で、Google Cloud 環境でのアプリケーション開発をサポートします。
*   **Google Artifact Registry**: Google Cloud が提供する、コンテナイメージやパッケージなどを一元的に保存・管理するためのサービスです。

---

## Security

### 原文: Apigee Emulator

This release addresses 78 security vulnerabilities across Cassandra base image, Go standard library, Java dependencies, and Python packages. Key fixes include:

| CVE | Component |
| --- | --- |
| CVE-2022-42003 | Jackson Databind |
| CVE-2022-42004 | Jackson Databind |
| CVE-2022-38749 | SnakeYAML |
| CVE-2022-38750 | SnakeYAML |
| CVE-2023-2976 | Google Guava |
| CVE-2020-8908 | Google Guava |
| CVE-2024-12798 | Logback |
| CVE-2025-22866 | Go stdlib |
| CVE-2025-22870 | Go stdlib |
| CVE-2022-40897 | Python setuptools |

And 68 additional CVEs fixed through updated upstream dependencies.

### 説明：
Apigee Emulator の今回のリリースでは、Cassandra ベースイメージ、Go 標準ライブラリ、Java 依存関係、Python パッケージなど、合計78件のセキュリティ脆弱性 (CVE) が修正されました。リストアップされている主要なものに加え、68件の追加の CVE も、更新されたアップストリーム依存関係を通じて修正されています。

### 影響有無：
**影響あり（ポジティブな影響、開発環境限定）**
*   **理由**: 本番環境の Apigee X サービス自体への直接的な影響はありません。Apigee Emulator を利用している開発環境において、これらの脆弱性が解消されるため、セキュリティ体制が大幅に向上します。開発者が安全な環境で作業するためには、迅速な適用が推奨されます。

### 対処方法：
Apigee Emulator を開発環境で利用している場合、セキュリティリスクを軽減するため、バージョン 2.0.0 への更新を**強く推奨**します。これにより、これらの脆弱性修正が適用されます。

### 用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 広く認識され、公開されている情報セキュリティの脆弱性や暴露に対する識別子を付与するシステムです。
*   **Cassandra**: 高い拡張性と可用性を持つオープンソースの分散型NoSQLデータベースです。
*   **Go standard library (Go stdlib)**: Go 言語に標準で含まれる、さまざまな機能を提供するライブラリ群です。
*   **Java dependencies**: Java アプリケーションが動作するために必要となる外部のライブラリやフレームワークのことです。
*   **Python packages**: Python プログラムで利用できる、特定の機能を提供するコードの集合体です。
*   **Jackson Databind, SnakeYAML, Google Guava, Logback, Python setuptools**: 今回のリリースノートで脆弱性が修正された、具体的なソフトウェアコンポーネントやライブラリの名前です。
# Title: May 21, 2026 
Link: https://docs.cloud.google.com/release-notes#May_21_2026<br>
Google Cloud リリースノートに関する影響調査結果を以下に報告いたします。

---

# AlloyDB for PostgreSQL
## Fixed
原文: `ChatGPT users are now able to list and use the AlloyDB toolset provided by the AlloyDB remote MCP server.`
説明：AlloyDBリモートMCPサーバーが提供するAlloyDBツールセットについて、ChatGPTユーザーがリスト表示および利用できるよう修正されました。
影響有無：現行のシステムにおいて、ChatGPTとAlloyDBのツールセット連携を積極的に利用していない場合、直接的な影響はありません。ChatGPTとの連携を検討している場合、この修正により機能が利用可能となり、ポジティブな影響があります。
対処方法：特に追加の対処は不要です。もしChatGPTとの連携を試みていたが問題があった場合は、この修正により解決されている可能性があるため、再確認を推奨します。
用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、PostgreSQLと完全に互換性のあるフルマネージドなエンタープライズグレードのデータベースサービスです。高性能、高可用性、スケーラビリティが特徴です。
*   **AlloyDB remote MCP server**: AlloyDBの特定の機能やツールセットを提供するバックエンドサービスを指すと考えられます。
*   **AlloyDB toolset**: AlloyDBの操作、管理、開発を支援する目的で提供されるツール群を指します。

---

# Apigee X
## Announcement
原文: `On May 21st, 2026, we released an updated version of Apigee (1-17-0-apigee-8). Note: Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.`
説明：Apigeeのバージョン1-17-0-apigee-8が2026年5月21日にリリースされました。このバージョンは順次Google Cloudの全ゾーンに展開されており、完了まで4営業日以上かかる場合があります。そのため、お客様のApigeeインスタンスに新機能や修正が反映されるまで時間を要する可能性があります。
影響有無：Apigee Xをご利用の場合、今回のバージョンアップは自動的に適用されるため影響があります。新機能の追加やバグ修正が含まれているため、システム全体の安定性向上や機能拡張といったポジティブな影響が期待されます。
対処方法：Apigee Xの管理者は、このリリースに含まれる機能変更や修正が既存のAPIプロキシ、統合、またはカスタムアプリケーションに潜在的な影響を与えないか、Apigeeの公式リリースノート全体を確認することを推奨します。自動アップグレードのため手動での操作は不要ですが、バージョンが適用された後にApigee環境の動作に異常がないか、監視を強化することが望ましいです。
用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームです。APIの設計、セキュリティ、デプロイ、監視、収益化といったライフサイクル全体を管理します。
*   **Rollout**: 新しいソフトウェアバージョンや機能が、システム全体に段階的に展開されていくプロセスです。ダウンタイムを最小限に抑えつつ、安定した展開を目的としています。

## Fixed
原文: `Bug ID 514973778: Fixed Model Armor response parsing to gracefully handle unknown fields, so future Model Armor field additions no longer cause policy failures.`
説明：バグID 514973778。Model Armor機能におけるレスポンスパース処理が修正され、未知のフィールドがレスポンスに含まれていても適切に処理されるようになりました。これにより、将来的にModel Armorに新しいフィールドが追加されても、ポリシーが失敗する原因となることがなくなります。
影響有無：Apigee XのModel Armor機能を利用している場合、この修正によりシステムの安定性が向上します。既存のポリシーが不明なフィールドによって予期せず失敗するリスクが軽減されるため、ポジティブな影響です。
対処方法：Model Armorを現在ご利用の場合、この修正により安定性が向上しているため、特に追加の対処は不要です。過去にModel Armor関連でポリシーの失敗が多発していた場合は、この修正によって解決されている可能性があるため、再評価を検討しても良いでしょう。
用語説明：
*   **Model Armor**: Apigee Xのセキュリティ機能の一つで、APIトラフィックをリアルタイムで分析し、悪意のあるペイロードや異常なリクエストパターンを検出し、ブロックする機能です。通常、機械学習モデルを活用して脅威を識別します。
*   **Response parsing**: APIからの応答データ（例: JSON、XML）をプログラムが解析し、構造化されたデータとして利用できるようにする処理です。
*   **Unknown fields**: データ構造の定義に含まれていない、またはプログラムが予期しないデータフィールドを指します。
*   **Policy failures**: Apigeeで設定されたAPIポリシー（例: セキュリティ、トラフィック管理、レート制限など）が、何らかの理由で正常に実行されなかった状態を指します。

---

# Google Kubernetes Engine (GKE)

## Change
原文: `GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.`
説明：GKEクラスターのバージョンが更新され、新しいバージョンが利用可能になりました。これらの新バージョンは、新規GKEクラスターの作成、および既存クラスターのコントロールプレーンとノードの手動アップグレードに利用できます。バージョン管理とアップグレードに関する詳細情報は、GKEのドキュメントを参照してください。
影響有無：
*   **GKEクラスター利用者**: 利用可能なGKEバージョンが増えることで、アップグレード計画の柔軟性が向上します。既存のクラスターが自動アップグレード設定を使用している場合、これらの新しいバージョンが順次適用される対象となります。
*   **Google Cloud Composer 2利用者 (Composer version 2.7.1, Airflow version 2.7.3)**: Composer 2はGKE Autopilotクラスターを基盤として利用しています。GKEの基盤バージョンはGoogleによって管理・アップグレードされるため、ユーザーによる直接のGKEアップグレード操作は不要です。しかし、基盤となるGKEのバージョン更新は、Composer環境の安定性、パフォーマンス、セキュリティに間接的に影響を与える可能性があります（通常は改善方向）。
対処方法：
*   **GKEクラスター管理者**: 現在のクラスターのアップグレードチャネルとバージョンを確認し、新しいバージョンへのアップグレード計画を検討してください。特に手動アップグレードの場合は、アップグレード前にテスト環境でワークロードの互換性を検証することを強く推奨します。
*   **Google Cloud Composer 2利用者**: Composer環境の健全性監視を継続してください。GKEの基盤アップグレードはGoogleによって管理されるため、特別な対処は不要ですが、ComposerのリリースノートやFAQで、基盤GKEのバージョンアップに関する追加アナウンスがないか確認することをお勧めします。
用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するフルマネージドなKubernetesサービスで、コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Control plane**: Kubernetesクラスターの管理層であり、APIサーバー、スケジューラー、コントローラーマネージャーなどのコンポーネントが含まれます。クラスターの状態を管理し、ワーカーノードに指示を出します。
*   **Node**: コンテナ化されたアプリケーション（Pod）が実際に実行される仮想マシンまたは物理マシンで、Kubernetesクラスターの計算リソースを提供します。

## Security
原文: `This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image: GKE version 1.36.0-gke.2253000 Container-Optimized OS version cos-beta-129-19506-120-52 Details cos-beta-129-19506-120-52 release notes`
説明：このGKEリリースには、更新されたContainer-Optimized OS（COS）イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたCOSイメージは、以前のGKEリリース以降にリリースされたすべてのCOSバージョンからのセキュリティ修正を累積的に含んでいます。各COSイメージで解決された特定の脆弱性については、個別のセキュリティリリースノートを参照してください。例えば、GKEバージョン1.36.0-gke.2253000は、cos-beta-129-19506-120-52のCOSイメージを使用しています。
影響有無：
*   **GKEクラスター利用者**: GKEクラスターの基盤となるノードイメージのセキュリティが向上します。これにより、クラスターの全体的なセキュリティ態勢が強化され、既知の脆弱性からの保護が強化されるため、ポジティブな影響です。
*   **Google Cloud Composer 2利用者**: Composer 2の基盤となるGKEノードはCOSを使用しているため、間接的にセキュリティ強化の恩恵を受けます。
対処方法：特に追加の対処は不要です。GKEのアップグレードチャネルを通じて、これらのセキュリティ修正が適用された新しいCOSイメージがクラスターノードに自動的に適用されます。もし自動アップグレードを無効にしている場合は、セキュリティ向上のためにも手動でのアップグレードを検討することを推奨します。
用語説明：
*   **Container-Optimized OS (COS)**: Google CloudがKubernetes Engine向けに提供する、コンテナの実行に最適化された最小限のオペレーティングシステムイメージです。セキュリティとパフォーマンスを重視して設計されています。
*   **Cumulative security fixes**: 以前のすべてのセキュリティ修正が含まれる、累積的なセキュリティパッチの適用を指します。これにより、最新のパッチを適用するだけで、過去のすべての脆弱性修正も網羅されます。

## Change
原文: `Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. The following versions are now available in the Stable channel: 1.33.11-gke.1013000, 1.34.6-gke.1307000, 1.35.3-gke.1389002`
説明：GKEのStableチャネルにおいて、バージョン1.33.11-gke.1013000、1.34.6-gke.1307000、および1.35.3-gke.1389002が利用可能になりました。これらのバージョンは現在ロールアウト中であり、全てのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：Stableチャネルを使用しているGKEクラスターは、これらの新しい安定版バージョンに自動または手動でアップグレードできるようになります。これにより、最新の安定した機能とバグ修正が利用可能となり、安定運用に寄与します。
対処方法：自動アップグレードを有効にしているクラスターでは特別な対処は不要ですが、アップグレードの進行状況を監視し、予期せぬ問題が発生しないか確認することが推奨されます。手動アップグレードを行う場合は、アップグレード計画に基づいて実施してください。

## Change
原文: `Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. Version 1.35.3-gke.1389002 is now available in the Regular channel.`
説明：GKEのRegularチャネルにおいて、バージョン1.35.3-gke.1389002が利用可能になりました。このバージョンは現在ロールアウト中であり、全てのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：Regularチャネルを使用しているGKEクラスターは、このバージョンに自動または手動でアップグレードできるようになります。これにより、より新しい機能とバグ修正が利用可能となります。
対処方法：Stableチャネルの場合と同様、自動アップグレードを有効にしている場合は特別な対処は不要ですが、アップグレードの進行状況を監視することが推奨されます。手動アップグレードを行う場合は、計画的に実施してください。

## Change
原文: `Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. The following versions are now available in the Rapid channel: 1.33.12-gke.1000000, 1.34.8-gke.1000000, 1.35.5-gke.1000000, 1.36.0-gke.2253000`
説明：GKEのRapidチャネルにおいて、バージョン1.33.12-gke.1000000、1.34.8-gke.1000000、1.35.5-gke.1000000、および1.36.0-gke.2253000が利用可能になりました。これらのバージョンは現在ロールアウト中であり、全てのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：Rapidチャネルを使用しているGKEクラスターは、これらのバージョンに自動または手動でアップグレードできるようになります。最も早く最新機能やバグ修正を利用できますが、他のチャネルと比較して安定性は低い可能性があります。
対処方法：他のチャネルの場合と同様、自動アップグレードを有効にしている場合は特別な対処は不要ですが、Rapidチャネルは新機能の早期適用を目的としているため、より入念なテストと監視が推奨されます。手動アップグレードを行う場合は、入念な検証計画に基づいて実施してください。

## Change
原文: `Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. The following versions are now available: 1.33.12-gke.1000000, 1.34.8-gke.1000000, 1.35.3-gke.1389002, 1.35.5-gke.1000000. The following node versions are now available: 1.30.14-gke.2530000, 1.31.14-gke.1942000, 1.32.13-gke.1551000, 1.33.12-gke.1000000, 1.34.8-gke.1000000, 1.35.3-gke.1389002, 1.35.5-gke.1000000.`
説明：いくつかの新しいGKEクラスターバージョンと対応するノードバージョンが利用可能になりました。これらのバージョンは現在ロールアウト中であり、全てのGoogle Cloudゾーンで利用可能になるまで数日かかる場合があります。
影響有無：
*   **GKEクラスター利用者**: 既存のGKEクラスターおよびノードのアップグレード、または新規クラスターの作成時に選択肢が増えます。これらのバージョンにはセキュリティ修正やバグ修正が含まれるため、クラスターの安定性とセキュリティ向上に寄与します。
*   **Google Cloud Composer 2利用者**: Composer 2はGKE Autopilotを利用しており、GKEノードのバージョン管理はGoogleに委ねられます。GKEのこれらのバージョンがComposer環境の基盤として採用される可能性があるため、間接的に影響します。
対処方法：GKEクラスターの運用方針（自動アップグレード vs 手動アップグレード、使用チャネル）に基づいて対応を決定してください。Composerユーザーの場合、Composerのアップデートは