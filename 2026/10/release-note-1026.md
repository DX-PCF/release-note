
# Title: October 24, 2026 
Link: https://docs.cloud.google.com/release-notes#October_24_2026<br>
はい、承知いたしました。Google Cloudのインフラエンジニアとして、ご提示いただいたCloud Runのリリースノートについて、構築済みのサービスへの影響調査結果を報告します。

---

# Cloud Run
## Security

原文:
```
 The following runtime languages contain important security updates:

- Go 1.24 and later: `1.24.13`, `1.25.14`, `1.26.10`, `1.27.3`
- Node.js 22 and later: `22.23.4`, `24.22.1`, `26.12.1`
- Java 17 and later: `17.0.20_101`, `21.0.12_101.0.LTS`, `25.0.5_8.0.LTS`
- PHP 8.2 and later: `8.2.35`, `8.3.36`, `8.4.27`, `8.5.12`
- Python 3.10 and later: `3.10.22`, `3.11.17`, `3.12.15`, `3.13.15`, `3.14.6`
- Ruby 3.3 and later: `3.3.12`, `3.4.11`, `4.0.7`
- .NET 6 and later: `6.0.428`, `8.0.415`, `10.0.100`

[Go 1.24 and later](https://docs.cloud.google.com/run/docs/runtime-support#go)
[Node.js 22 and later](https://docs.cloud.google.com/run/docs/runtime-support#node.js)
[Java 17 and later](https://docs.cloud.google.com/run/docs/runtime-support#java)
[PHP 8.2 and later](https://docs.cloud.google.com/run/docs/runtime-support#php)
[Python 3.10 and later](https://docs.cloud.google.com/run/docs/runtime-support#python)
[Ruby 3.3 and later](https://docs.cloud.com/run/docs/runtime-support#ruby)
[.NET 6 and later](https://docs.cloud.google.com/run/docs/runtime-support#.net)
 The following stacks and their underlying operating system packages have also been updated:

- `google-22`, `google-22-full`
- `google-24`, `google-24-full`

 Take immediate protective action by rebuilding and redeploying your resources with updated dependencies.

 See Security bulletins for Google Cloud for more information.

[Security bulletins for Google Cloud](https://docs.cloud.google.com/support/bulletins)
```

説明：
Cloud Runでサポートされている主要なプログラミング言語（Go, Node.js, Java, PHP, Python, Ruby, .NET）の特定バージョン以降に対して、重要なセキュリティアップデートが提供されました。これにより、これらのランタイムに含まれる既知の脆弱性が修正されます。
また、Cloud Runのビルドパックで利用されるベースイメージ（`google-22`, `google-22-full`, `google-24`, `google-24-full`）およびその基盤となるOSパッケージも更新されました。
Google Cloudは、これらのセキュリティアップデートを適用するために、対象となるアプリケーションのリソースを最新の依存関係で再構築（ビルド）し、再デプロイすることを強く推奨しています。

影響有無：
**影響あり（セキュリティリスク低減のため推奨）**

現在稼働中のCloud Runサービス自体が直ちに停止したり、機能互換性の問題が発生することはありません。しかし、このアップデートはセキュリティ脆弱性の修正を目的としているため、**対応しない場合、サービスが既知のセキュリティリスクに晒される状態が継続します。** これは、当社のセキュリティ体制および潜在的なインシデントリスクに直接影響します。

対処方法：
サービスが利用しているランタイムに応じて、以下の対応を速やかに実施することを推奨します。

1.  **利用中のランタイムバージョンの確認:**
    *   現在Cloud Runサービスで使用しているアプリケーションの言語およびランタイムバージョンを確認します。Dockerfileでベースイメージを指定しているか、Google Cloud Buildpacksを使用しているかによって確認方法が異なります。
2.  **コンテナイメージの再構築:**
    *   **Dockerfileを使用している場合:**
        *   Dockerfileで指定しているベースイメージのタグを最新のパッチバージョンに更新します（例: `FROM python:3.11-slim-bookworm` を利用している場合、`docker pull python:3.11-slim-bookworm`で最新のパッチバージョンが取得されることを確認）。
        *   Dockerfile内で`apt-get update && apt-get upgrade`などのコマンドを実行している場合は、再度イメージをビルドすることで最新のOSパッケージが適用されます。
        *   アプリケーションの依存関係（例: `requirements.txt`や`package.json`など）が、リリースノートに記載されている推奨バージョンを満たすか、あるいはパッチバージョンが自動的に更新されるように調整します。
    *   **Google Cloud Buildpacksを使用している場合:**
        *   アプリケーションのソースコードに変更がなくても、`gcloud run deploy`コマンドを再実行するか、Cloud Buildトリガーを再実行することで、自動的に最新のビルドパックおよび基盤となるOSパッケージが適用されたコンテナイメージが再構築されます。
        *   この場合、明示的にランタイムバージョンを上げる必要は通常ありませんが、より新しいメジャーバージョンやマイナーバージョンへの移行を検討することも有効です。
3.  **Cloud Runサービスの再デプロイ:**
    *   再構築した最新のコンテナイメージを使用して、Cloud Runサービスを再デプロイします。これにより、稼働中のサービスがセキュリティパッチが適用された新しいイメージに切り替わります。
    *   `gcloud run deploy SERVICE_NAME --image gcr.io/PROJECT_ID/IMAGE_NAME --region REGION --allow-unauthenticated` (または認証が必要なオプション) を実行します。
4.  **CI/CDパイプラインの更新:**
    *   CI/CDパイプラインを導入している場合、定期的にコンテナイメージを再ビルド・再デプロイするジョブが含まれているか確認し、含まれていない場合は追加を検討します。これにより、今後も自動的にセキュリティアップデートが適用されるようになります。

用語説明：
*   **ランタイム (Runtime)**: アプリケーションのコードを実行するためのソフトウェア環境です。特定のプログラミング言語（例: Python, Node.js）の実行エンジン、標準ライブラリ、およびその他の必要なコンポーネントを含みます。
*   **依存関係 (Dependencies)**: アプリケーションが正しく動作するために必要とする外部のライブラリ、モジュール、フレームワークなどのコンポーネントです。これらは通常、パッケージマネージャー（例: pip for Python, npm for Node.js）を介して管理されます。
*   **再構築 (Rebuilding)**: コンテナイメージを最初から作り直すプロセスです。これにより、最新のベースイメージや依存関係がコンテナに取り込まれます。
*   **再デプロイ (Redeploying)**: 新しく構築されたコンテナイメージをCloud Runサービスに適用し、既存の稼働中のインスタンスを置き換えるプロセスです。
*   **スタック (Stack) / ベースイメージ (Base Image)**: コンテナイメージの土台となる部分で、オペレーティングシステム（OS）と、特定のアプリケーションやランタイムを動作させるために必要な基本的なソフトウェアがプリインストールされています。`google-22`や`google-24`は、Google Cloudが提供するCloud Buildpacksで使用されるベースイメージのバージョンです。
*   **セキュリティ脆弱性 (Security Vulnerability)**: ソフトウェアやシステムの設計上または実装上の欠陥で、悪用されると情報漏洩、データの改ざん、サービス停止などのセキュリティインシデントにつながる可能性のあるものです。
# Title: October 23, 2026 
Link: https://docs.cloud.google.com/release-notes#October_23_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、構築済みのサービスへの影響について調査結果をご報告いたします。

---

# Cloud Monitoring
## Fixed
**原文**: Ops Agent version 2.73.0 includes patches for a Go vulnerability involving system root certificates, CVE-2026-111943. For more information, see Ops Agent 2.73.0 notes.
[CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943)
[Ops Agent 2.73.0 notes](https://github.com/GoogleCloudPlatform/ops-agent/releases/tag/2.73.0)

**説明**:
Cloud Monitoringで利用されるOps Agentのバージョン2.73.0において、Go言語のシステムルート証明書に関連する脆弱性 (CVE-2026-111943) が修正されました。このバージョンにはその脆弱性に対するパッチが含まれています。

**影響有無**:
影響あり（推奨対応）。
Ops AgentをGoogle CloudのCompute Engine VMインスタンスやオンプレミスサーバーなどにデプロイして、モニタリングやロギングデータを収集している場合に影響します。この修正はセキュリティ脆弱性への対応であるため、該当バージョンのOps Agentを利用している場合はアップグレードが強く推奨されます。
Google Cloud Composer 2.7.1環境の内部でOps Agentが直接利用されているかは、ユーザーが管理する範囲ではないため通常はGoogleによる管理に委ねられます。しかし、お客様が独自にComposer環境のVMにOps Agentをデプロイしている場合や、Composer以外のVMにOps Agentをデプロイしている場合は影響があります。

**対処方法**:
現在Ops Agentをご利用の場合、バージョン2.73.0以降へのアップグレードを検討してください。Ops Agentの自動更新設定が有効になっている場合は、特別な操作は不要で自動的に最新バージョンに更新されます。手動でインストールまたは管理している場合は、公式ドキュメントを参照し、エージェントを更新してください。

**用語説明**:
*   **Ops Agent**: Google Cloud MonitoringおよびCloud Loggingのために、VMインスタンスからシステム、アプリケーションのテレメトリーデータ（ログ、メトリクス）を収集するエージェントです。以前のMonitoring AgentおよびLogging Agentの後継として開発されました。
*   **Go vulnerability**: プログラミング言語Goで記述されたソフトウェアにおける脆弱性。本件ではシステムルート証明書（TLS/SSL通信の信頼性を確立するために使用される証明書）の処理に関する問題が修正されました。
*   **CVE-2026-111943**: 共通脆弱性識別子（Common Vulnerabilities and Exposures）の一つで、特定の情報セキュリティ脆弱性を一意に識別するためのIDです。

---

# Cloud SQL for PostgreSQL
## Security
**原文**: In response to GCP-2026-071, Google is updating Cloud SQL's managed components. No manual updates to the certificate store are required for Cloud SQL-managed instances. The fix is shipping in a new maintenance version that will be applied during scheduled maintenance. You can also apply the fix by performing self-service maintenance. An announcement will be published when the self-service maintenance fix is available.

**What should I do?**
*   If you use the Cloud SQL Auth Proxy, then upgrade the Cloud SQL Auth Proxy to 2.26.3 or later and the Cloud SQL Proxy Operator to 1.8.4 or later. If you run the standalone proxy binary, then also update the host's certificate authority (CA) certificates.
*   If you use a Cloud SQL Language Connector, then update the language runtime and operating system CA certificates used with the Cloud SQL Language Connector (for example, Go 1.26.10 or 1.27.3 or later, certifi 2026.10.19 or later).
*   If you're using the gcloud CLI to install the Cloud SQL Auth Proxy, then update the gcloud CLI to 590.0.1.

[GCP-2026-071](https://docs.cloud.google.com/support/bulletins#gcp-2026-071)
[scheduled maintenance](https://docs.cloud.google.com/sql/docs/postgres/maintenance)
[performing self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance)
[2.26.3 or later](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#install)
[1.8.4 or later](https://docs.cloud.com/sql/docs/postgres/connect-proxy-operator)
[Cloud SQL Language Connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors)
[590.0.1](https://docs.cloud.google.com/sdk/gcloud#download_and_install_the)

**説明**:
GCP-2026-071というセキュリティ問題に対応するため、Cloud SQLのマネージドコンポーネントが更新されます。Cloud SQLインスタンス自体については、ユーザー側での証明書ストアの手動更新は不要であり、Googleが提供するスケジュールメンテナンス中に自動的に修正が適用されます。より早く修正を適用したい場合は、自己サービスメンテナンスを実行することも可能です。

しかし、Cloud SQLに接続するためのクライアント側ツールを利用している場合は、ユーザー側での対応が必要です。具体的には以下のツールのアップデートが求められます。
1.  **Cloud SQL Auth Proxy**: 2.26.3以降のバージョンへのアップグレード。スタンドアロンバイナリを使用している場合は、ホストのCA証明書も更新。
2.  **Cloud SQL Proxy Operator**: 1.8.4以降のバージョンへのアップグレード（Kubernetes環境などで利用している場合）。
3.  **Cloud SQL Language Connector**: 使用している言語ランタイムとOSのCA証明書を更新（例: Go, certifi）。
4.  **gcloud CLI**: Cloud SQL Auth Proxyのインストールにgcloud CLIを使用している場合、gcloud CLIを590.0.1以降に更新。

**影響有無**:
影響あり（要確認および対応）。
Cloud SQL for PostgreSQLインスタンス自体はGoogleが管理するため、データベースへの直接的な影響は少ないですが、お客様のCloud SQLへの接続方法によって対処が必要になります。

特に、Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) の環境からCloud SQLに接続している場合、通常はCloud SQL Auth Proxyを介した接続が行われます。Composer環境内部でAuth ProxyのバージョンがGoogleによって管理されている場合はユーザー側の直接的な操作は不要ですが、もしComposerのDAGsからAuth Proxyを直接利用するようなカスタム実装を行っている場合、またはComposer以外のアプリケーション（例: Compute Engine VM上のアプリケーション、GKE Podなど）がCloud SQL Auth ProxyやLanguage Connectorを利用してCloud SQLに接続している場合は、それぞれのツールのバージョンを確認し、必要に応じてアップデートが必要です。

これは重要なセキュリティ修正であるため、関連するツールを利用している場合は、速やかに対応を進めることを強く推奨します。

**対処方法**:
以下のステップで対応してください。
1.  現在Cloud SQLへの接続に利用しているツール（Cloud SQL Auth Proxy, Cloud SQL Proxy Operator, Cloud SQL Language Connector, gcloud CLI）を特定します。
2.  それぞれのツールのバージョンが、リリースノートに記載されている推奨バージョン（Auth Proxy 2.26.3以上、Proxy Operator 1.8.4以上、gcloud CLI 590.0.1以上）を満たしているか確認します。
3.  バージョンが古い場合は、指定されたバージョン以降にアップグレードしてください。
4.  スタンドアロンのAuth ProxyバイナリやLanguage Connectorを使用している場合は、それらが稼働するホストのCA証明書も最新の状態に保つようにしてください。
5.  Cloud SQLインスタンス自体については、今後のGoogleによるスケジュールメンテナンスで自動的に修正が適用されます。緊急性に応じて、自己サービスメンテナンスの利用も検討できますが、これには事前にアナウンスされる情報をご確認ください。

**用語説明**:
*   **GCP-2026-071**: Google Cloud Platformにおける特定のセキュリティ脆弱性を識別するためのIDです。詳細については、提供されたリンクのセキュリティ速報（Support Bulletins）で確認できます。
*   **Cloud SQL Auth Proxy**: Cloud SQLインスタンスへの接続を安全に行うためのオープンソースコネクタです。TLS/SSL暗号化とIAM認証を組み合わせて、安全な接続チャネルを提供します。特にGoogle Cloud外の環境からCloud SQLに接続する際に推奨されます。
*   **Cloud SQL Proxy Operator**: Kubernetes環境でCloud SQL Auth Proxyをデプロイおよび管理するためのKubernetesオペレーターです。
*   **Cloud SQL Language Connector**: 各プログラミング言語の標準ライブラリ（Go, Python, Javaなど）を使用してCloud SQLに接続するためのヘルパーライブラリです。Auth Proxyと同様に安全な接続を提供します。
*   **gcloud CLI**: Google Cloudを管理するためのコマンドラインインターフェースツールです。Cloud SQL Auth Proxyのダウンロードやセットアップにも利用されることがあります。
*   **CA証明書 (Certificate Authority certificates)**: 信頼された第三者機関（認証局）によって発行されるデジタル証明書で、通信相手の身元を検証したり、暗号化通信を確立したりするために使用されます。

---
# Title: October 22, 2026 
Link: https://docs.cloud.google.com/release-notes#October_22_2026<br>
Google Cloudインフラエンジニアとして、ご提示いただいたリリースノートに基づき、既存サービスへの影響調査結果を報告いたします。

---

# Apigee X

## Announcement

原文: On October 22, 2026, we released an updated version of Apigee (1-18-0-apigee-7).
> **Note:** Rollouts of this release began today and can take four or more business
days to complete across all Google Cloud zones. Your instances might not have
the features and fixes available until the rollout is complete.

説明: Apigeeの新しいバージョン (1-18-0-apigee-7) がリリースされました。このリリースは本日（リリースノートが公開された日）からロールアウトが開始され、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる場合があります。ロールアウトが完了するまで、インスタンスで新機能や修正が利用できない可能性があります。
(※原文の日付が2026年となっていますが、これは誤植の可能性が高く、リリースノートの公開時期から2024年のものと推察されます。)

影響有無: 影響なし（自動適用）
Apigee X はGoogle Cloudが管理するマネージドサービスであるため、バージョンアップはGoogle側で自動的に実施されます。ユーザー側で特別な操作は不要です。ただし、ロールアウト期間中は、一部のインスタンスで新機能や修正がすぐに反映されない可能性があります。

対処方法: 特になし。ロールアウトの完了を待ってください。

用語説明:
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームの最新バージョン。APIの設計、セキュリティ、デプロイ、監視、分析などを一元的に行える。
*   **Rollout**: ソフトウェアやサービスの新しいバージョンを段階的に導入していくプロセス。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **573663408** | **Security fix for Apigee.** Upgraded the ingress gateway to patch security vulnerabilities. |
| **N/A** | **Security fix for Apigee infrastructure.** |

説明:
*   Bug ID 573663408: ApigeeのIngress Gatewayのセキュリティ脆弱性を修正するため、Gatewayがアップグレードされました。
*   N/A: Apigeeの基盤インフラストラクチャにおけるセキュリティ修正が適用されました。

影響有無: 影響なし（セキュリティ向上）
これらの修正は、Apigeeサービスのセキュリティを強化するためのものであり、既存のワークロードに直接的な影響を与えることなく、プラットフォーム全体のセキュリティ体制が向上します。Apigeeはマネージドサービスのため、これらのパッチはGoogleによって自動的に適用されます。

対処方法: 特になし。

用語説明:
*   **Ingress Gateway**: 外部からのトラフィックをサービス内部にルーティングするための入口となるゲートウェイ。Apigee Xでは、APIトラフィックを受け付けるエッジコンポーネント。
*   **Security Vulnerabilities**: セキュリティ上の欠陥や弱点。悪用されると、システムへの不正アクセス、データ漏洩、サービス妨害などにつながる可能性がある。

## Fixed

### Bug ID 568535165

原文: Skip main_task_wait_time and nio_task_wait_time metrics for the first 12 Prometheus scrapes during Message Processor startup warmup.

説明: Message Processorの起動ウォームアップ期間中、最初の12回のPrometheusスクレイピングにおいて、`main_task_wait_time`および`nio_task_wait_time`のメトリクスがスキップされるようになりました。

影響有無: 影響なし
メトリクス収集の最適化であり、通常運用への直接的な影響はありません。ウォームアップ期間中の不要なメトリクス収集が抑制され、より正確な運用メトリクスが得られる可能性があります。

対処方法: 特になし。

用語説明:
*   **Message Processor**: Apigeeのランタイムコンポーネントの一部で、APIプロキシへのリクエスト処理、ポリシーの実行、バックエンドへのルーティングなどを担当する。
*   **Prometheus**: オープンソースの監視およびアラートツールキット。
*   **Scrape**: Prometheusが監視対象からメトリクスを定期的に収集する行為。

### Bug ID 573602919

原文: Fix generated OpenAPI specs' servers[] to carry the Apigee envgroup hostname instead of the backend target host.

説明: 生成されるOpenAPI仕様の`servers[]`フィールドに、バックエンドターゲットホストではなく、Apigeeの環境グループホスト名が正しく設定されるようになりました。

影響有無: 影響なし（OpenAPI定義の正確性向上）
OpenAPI定義を利用している場合、生成される仕様がより正確になります。既存のOpenAPI定義に直接的な変更を強制するものではありませんが、再生成する際に正しいホスト名が含まれるようになります。

対処方法: 特になし。新しいOpenAPI定義を生成する際に、この修正が反映されます。

用語説明:
*   **OpenAPI Specification (OAS)**: RESTful APIを記述するための標準的な言語に依存しないインターフェース定義形式。以前はSwagger Specificationとして知られていた。
*   **`servers[]`**: OpenAPI Specificationにおいて、APIが利用可能なサーバーのURLを記述するフィールド。
*   **EnvGroup (環境グループ)**: Apigee XにおけるAPIデプロイの論理的なグループ。これにより、複数の環境をまとめた単一のホスト名でAPIを公開できる。

### Bug ID 562964081 (1回目)

原文: The sgpUserIntentMatchingMode verdict-log field is now always present, including on dry-run policy records, and shows the mode used for the evaluation, including when sgpUserIntentMatching isn't set (CONSTRAINTS_AND_INTENT, or INTENT_ONLY when no policies match the tool call).

説明: `sgpUserIntentMatchingMode`のverdict-logフィールドが、ドライランポリシーのログ記録を含むすべての場合に常に存在し、評価に使用されたモードを表示するようになりました。これは、`sgpUserIntentMatching`が設定されていない場合（`CONSTRAINTS_AND_INTENT`、またはツール呼び出しにポリシーがマッチしない場合は`INTENT_ONLY`）でも同様です。

影響有無: 影響なし（ログ詳細化）
Semantic Governance Policy (SGP) の評価に関するログの詳細度が向上します。既存のログ解析ツールやクエリに大きな影響はありませんが、より詳細な情報に基づいてポリシーの挙動を理解できるようになります。

対処方法: 特になし。

用語説明:
*   **Semantic Governance Policy (SGP)**: API呼び出しにおける意味的なチェックやガバナンスルールを適用するためのポリシー。特に大規模言語モデル（LLM）関連のAPI利用でセキュリティとコンプライアンスを強化するために使用される。
*   **Verdict-log**: ポリシー評価の結果が記録されるログエントリ。
*   **Dry-run policy**: 実際にポリシーを適用せずに、その評価結果をテストするために使用されるポリシー。

### Bug ID 524115876

原文: Fix an intermittent HTTP 400 error in the OASValidation policy's strict parameter validation that rejected valid requests.

説明: `OASValidation`ポリシーの厳格なパラメータ検証において、有効なリクエストが断続的にHTTP 400エラーで拒否される問題が修正されました。

影響有無: 影響なし（サービス信頼性向上）
誤って拒否されていた有効なリクエストが正しく処理されるようになります。これにより、APIの信頼性と可用性が向上します。

対処方法: 特になし。

用語説明:
*   **OASValidation policy**: OpenAPI Specificationに基づいてAPIリクエストの検証を行うApigeeポリシー。リクエストパス、ヘッダー、クエリパラメータ、ボディなどの形式をチェックする。

### Bug ID 572025634

原文: Responses with a compressed text/event-stream body to a proxy with an EventFlow now skip EventFlow processing and pass through intact instead of returning a corrupted body.

説明: 圧縮された`text/event-stream`ボディを持つレスポンスがEventFlowを使用するプロキシに送信された場合、EventFlow処理をスキップし、破損したボディが返されることなくそのまま通過するようになりました。

影響有無: 影響なし（データ整合性向上）
`text/event-stream`（Server-Sent Eventsなど）を利用し、かつ圧縮されたレスポンスを扱っている場合に、データの破損が解消され、正常に処理されるようになります。

対処方法: 特になし。

用語説明:
*   **EventFlow**: Apigeeの機能の一つで、APIプロキシを通過するイベントデータを監視・処理するためのもの。
*   **text/event-stream**: Server-Sent Events (SSE) で使用されるMIMEタイプ。サーバーからクライアントへ一方的にイベントを送信する際に使われる。

### Bug ID 549078690

原文: If no SGP policy is attributed for a denial, a customer sees the generic fallback message. This fix short-circuits to show the rationale instead when no matched policy has a configured denial message.

説明: SGPポリシーが拒否に帰属しない場合、以前は一般的なフォールバックメッセージが表示されていましたが、この修正により、一致するポリシーに拒否メッセージが設定されていない場合でも、拒否の根拠が短絡的に表示されるようになりました。

影響有無: 影響なし（エラーメッセージの改善）
SGPポリシーによって拒否された際のエラーメッセージがより分かりやすくなります。運用上の影響はありません。

対処方法: 特になし。

### Bug ID 492041991

原文: VerifyAPIKey and VerifyAccessToken now set the apiproduct.operation.llmTokenQuota.* flow variables only from the LLM operation(s) that matched the request; they are no longer set from unmatched LLM operations or for requests that match no LLM operation.

説明: `VerifyAPIKey`および`VerifyAccessToken`ポリシーが、`apiproduct.operation.llmTokenQuota.*`フロー変数を、リクエストにマッチしたLLM操作からのみ設定するようになりました。マッチしないLLM操作や、LLM操作に全くマッチしないリクエストからは設定されなくなります。

影響有無: 影響なし（フロー変数の正確性向上）
`apiproduct.operation.llmTokenQuota.*`変数を利用している場合に、より正確な値が設定されるようになります。既存の挙動でこれらの変数を誤って利用していなければ影響はありません。

対処方法: 特になし。

用語説明:
*   **LLM Operation**: 大規模言語モデル（LLM）に関連するAPI操作。

### Bug ID 567244615 (1回目)

原文: Semantic Governance now evaluates LLM requests it previously skipped, such as OpenAI requests whose message content is an array of parts, which can produce new denials and judge-model usage. It considers every system message rather than only the last, and a non-streaming OpenAI or an Ollama tool call whose arguments are not valid JSON is now an evaluation error.

説明: Semantic Governanceが、以前はスキップされていたLLMリクエスト（例: メッセージコンテンツがパートの配列であるOpenAIリクエストなど）を評価するようになりました。これにより、新たな拒否や判断モデルの使用量が発生する可能性があります。また、最後のシステムメッセージだけでなくすべてのシステムメッセージを考慮するようになり、引数が有効なJSONでない非ストリーミングのOpenAIまたはOllamaのツール呼び出しは評価エラーとなります。

影響有無: **影響あり（ポリシー適用範囲の拡大、新たな拒否発生の可能性、課金対象となるモデル使用量の増加の可能性）**
Semantic Governanceの評価対象が拡大されたため、これまで通過していたリクエストがポリシーに違反していると見なされ、新たに拒否される可能性があります。また、これにより関連する判断モデルの使用量が増加し、課金に影響する可能性があります。

対処方法:
1.  **影響分析**: 現在利用しているLLM関連APIのトラフィックに対し、この変更が新たな拒否を引き起こす可能性がないか、SGPポリシーの設定と合わせて評価してください。特に、OpenAIリクエストのメッセージコンテンツ形式や、Ollamaなどのツール呼び出しの引数形式を確認してください。
2.  **ポリシーの見直し**: 必要に応じて、SGPポリシーを調整し、誤った拒否が発生しないように設定を見直してください。ドライランモードでテストを実施し、本番環境への影響を事前に確認することを推奨します。
3.  **コスト監視**: LLM関連の判断モデル使用量が増加する可能性があるため、Apigeeのコスト監視を強化してください。

### Bug ID 567244615 (2回目)

原文: Semantic Governance no longer evaluates a request or response with a field it cannot read when a tool call is involved. It records verdict ERROR naming the field, with status MODEL_ERROR. The inline SemanticGovernance policy instead raises GovernedLLMResponseParseError or GovernedLLMProviderDetectionFailed (HTTP 500), in DRY_RUN too unless continueOnError is true. It also reads every text part of a Gemini system instruction and Gemini tool parameters given as parametersJsonSchema, and no longer loses the rest of a Claude or Gemini request when one field has an unexpected shape.

説明: Semantic Governanceは、ツール呼び出しが関連する場合に、読み取ることができないフィールドを持つリクエストやレスポンスを評価しなくなりました。代わりに、フィールド名を指定した`ERROR`の裁定を`MODEL_ERROR`ステータスで記録します。インラインのSemanticGovernanceポリシーは、`continueOnError`が`true`でない限り、ドライランモードでも`GovernedLLMResponseParseError`または`GovernedLLMProviderDetectionFailed`（HTTP 500）を発生させます。また、Geminiのシステム指示のすべてのテキスト部分と、`parametersJsonSchema`として与えられたGeminiツールパラメータを読み取るようになり、一つのフィールドの形状が予期しない場合にClaudeやGeminiリクエストの残りの部分が失われることがなくなりました。

影響有無: **影響あり（ポリシー評価挙動の変更、エラー応答の変化）**
ガバナンスチェックが失敗した場合の挙動が変更されました。特に、以前は通過していた可能性のある不正な形式のフィールドを持つリクエスト/レスポンスが、明確なエラーとして処理され、インラインポリシーの場合はHTTP 500を返す可能性があります（`continueOnError`が`false`の場合）。これにより、APIクライアントの挙動に影響が出る可能性があります。

対処方法:
1.  **エラー処理の見直し**: SGPポリシーで`continueOnError`を`false`に設定している場合、この変更によりHTTP 500エラーが返される可能性があるので、APIクライアント側でのエラー処理を適切に行っているか確認してください。
2.  **LLMプロバイダとの連携確認**: GeminiやClaudeのリクエスト/レスポンス形式が、この変更によって適切に解析されるようになることを確認してください。

### Bug ID 560272924

原文: Added continuous-scan bidirectional gRPC streaming support for the SanitizeModelResponse policy over Server-Sent Events (SSE) streams, preserving native LLM provider SSE JSON envelopes and event framing.

説明: `SanitizeModelResponse`ポリシーに対して、Server-Sent Events (SSE) ストリームを介した継続的なスキャンを行うための双方向gRPCストリーミングサポートが追加されました。これにより、ネイティブなLLMプロバイダのSSE JSONエンベロープとイベントフレーミングが維持されます。

影響有無: 影響なし（新機能追加）
これは新しい機能の追加であり、既存の利用には直接的な影響はありません。LLMプロバイダとの連携においてSSEストリームを使用している場合に、より高度なレスポンスのサニタイズが可能になります。

対処方法: 特になし。必要に応じてこの新機能の利用を検討してください。

用語説明:
*   **gRPC**: Googleが開発した高性能、オープンソースのRPC（Remote Procedure Call）フレームワーク。
*   **Server-Sent Events (SSE)**: HTTP接続を介してサーバーからクライアントへ一方的にイベントをプッシュするための技術。
*   **SanitizeModelResponse policy**: 大規模言語モデル（LLM）からの応答をサニタイズ（クリーンアップ、不要な情報の削除、フォーマット調整など）するためのApigeeポリシー。

### Bug ID 555332621

原文: Model Armor policies now honor HTTPClient.managementplane.skip.proxy: with it set, Model Armor callouts bypass the forward proxy like other googleapis traffic. Streaming (ContinuousScan) Model Armor traffic uses the forward proxy.

説明: Model Armorポリシーが`HTTPClient.managementplane.skip.proxy`設定を尊重するようになりました。この設定が有効な場合、Model Armorのコールアウトは、他のgoogleapisトラフィックと同様にフォワードプロキシをバイパスします。ただし、ストリーミング（継続スキャン）のModel Armorトラフィックはフォワードプロキシを使用します。

影響有無: **影響あり（ネットワークルーティングの変更の可能性）**
`HTTPClient.managementplane.skip.proxy`設定をApigee環境で利用しており、Model Armorポリシーを使用している場合に、そのコールアウトのネットワークルーティング挙動が変わる可能性があります。既存のネットワークセキュリティポリシーやファイアウォール設定に影響がないか確認が必要です。

対処方法:
1.  **ネットワーク構成の確認**: Apigeeインスタンスが利用しているネットワーク構成において、`HTTPClient.managementplane.skip.proxy`設定の有無と、その影響範囲を確認してください。
2.  **ファイアウォールルールの確認**: Model Armorからのアウトバウンドトラフィックが正しくルーティングされ、必要な外部エンドポイントに到達できるか、関連するファイアウォールルールを確認してください。

用語説明:
*   **Model Armor**: LLMとのインタラクションを保護するためのセキュリティ機能。
*   **Callout**: Apigeeポリシーから外部サービスを呼び出す機能。
*   **Forward Proxy**: クライアントからのリクエストを代理してウェブサーバーに送信するプロキシサーバー。

### Bug ID 158204922 (1回目)

原文: VerifyJWT now rejects a JWT whose header contains "b64":false, with fault steps.jwt.InvalidToken, as RFC 7797 section 7 requires. Previously, such a token could be accepted if KnownHeaders listed b64, IgnoreCriticalHeaders was true, or the header had no crit.

説明: `VerifyJWT`ポリシーが、RFC 7797のセクション7の要求に従い、ヘッダーに`"b64":false`を含むJWTを`steps.jwt.InvalidToken`エラーで拒否するようになりました。以前は、`KnownHeaders`に`b64`がリストされていたり、`IgnoreCriticalHeaders`が`true`であったり、ヘッダーに`crit`がなかったりした場合、そのようなトークンも受け入れられる可能性がありました。

影響有無: **影響あり（後方互換性のない変更 - Breaking Change）**
RFC 7797に準拠していない`"b64":false`を含むJWTを生成・利用している場合、この変更により`VerifyJWT`ポリシーによってそれらのJWTが拒否されるようになります。これは既存のクライアントやシステムに影響を与える可能性があります。

対処方法:
1.  **JWT生成元の確認**: `b64`ヘッダーを使用しているJWTの生成元を確認し、それがRFC 7797に準拠しているか検証してください。
2.  **JWTの更新**: 必要に応じて、`"b64":false`を使用するJWTの生成プロセスを修正し、RFC 7797に準拠した形式にする必要があります。

用語説明:
*   **JWT (JSON Web Token)**: クレーム（情報）を安全に表現するためのコンパクトなURLセーフな手段。通常、API認証や情報交換に使用される。
*   **`b64` header**: JWTの`JWS Protected Header`の一部で、ペイロードがBase64エンコードされているかを示する（`false`はエンコードされていないことを意味する）。RFC 7797で定義されている。
*   **RFC 7797**: JSON Web Signature (JWS) の非エンコードペイロード（Unencoded Payload）に関する仕様を定義するRFC。
*   **`crit` header**: JWSでクリティカルなヘッダーを示し、受信者が理解できない場合は拒否すべきヘッダーをリストする。
*   **`VerifyJWT` policy**: JWTの有効性を検証するためのApigeeポリシー。

### Bug ID 158204922 (2回目)

原文: GenerateJWS supports RFC 7797 unencoded payloads. GenerateJWS now raises MissingPayload, InvalidPayload or FailedToResolveVariable for payload errors, where it previously raised GenerationFailed. KnownHeaders and CriticalHeaders in the JWS and JWT policies accept names separated by whitespace, such as one per line. A b64 header supplied through AdditionalHeaders is now rejected, with steps.jws.InvalidNameForAdditionalHeader for GenerateJWS and steps.jwt.InvalidNameForAdditionalHeader for GenerateJWT. A proxy that set b64 through an AdditionalHeaders variable produced an RFC 7797 JWS before this change, and must move to UnencodedPayload, with DetachContent for the detached form.

説明: `GenerateJWS`ポリシーがRFC 7797の非エンコードペイロードをサポートするようになりました。ペイロードエラーの場合、以前は`GenerationFailed`を発生させていましたが、現在は`MissingPayload`、`InvalidPayload`、または`FailedToResolveVariable`を発生させます。JWSおよびJWTポリシーの`KnownHeaders`と`CriticalHeaders`は、空白で区切られた名前（例: 1行に1つ）を受け入れるようになりました。`AdditionalHeaders`を介して提供された`b64`ヘッダーは、`GenerateJWS`の場合は`steps.jws.InvalidNameForAdditionalHeader`、`GenerateJWT`の場合は`steps.jwt.InvalidNameForAdditionalHeader`で拒否されるようになりました。この変更以前に`AdditionalHeaders`変数を通じて`b64`を設定していたプロキシは、非エンコードペイロードのために`UnencodedPayload`（デタッチ形式の場合は`DetachContent`とともに）に移行する必要があります。

影響有無: **影響あり（後方互換性のない変更 - Breaking Change、機能拡張）**
*   **機能拡張**: RFC 7797非エンコードペイロードJWSの生成が可能になります。
*   **エラー処理の変更**: ペイロードエラー時のFault Name