
# Title: October 26, 2026 
Link: https://docs.cloud.google.com/release-notes#October_26_2026<br>
Google Cloudのリリースノートに関する調査結果をご報告いたします。

---

# Apigee X
## Security
原文: On October 24, 2026, we published a security bulletin for Apigee.
Two vulnerabilities in PHP core (CVE-2026-109618 and CVE-2026-109619, "PHP2Shell") allow an unauthenticated attacker to execute code remotely on a server running a vulnerable PHP version. The impact is limited to Drupal-based Apigee developer portals, which customers deploy and operate. Apigee, Apigee Hybrid, and the Apigee integrated portal don't use PHP and aren't affected.

[CVE-2026-109618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109618)
[CVE-2026-109619](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109619)
**Security bulletin published: GCP-2026-072**

[GCP-2026-072](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-072)

説明：
2026年10月24日に、Apigeeに関するセキュリティ速報 (GCP-2026-072) が公開されました。これは、PHPコアに存在する2つの脆弱性 (CVE-2026-109618, CVE-2026-109619, 通称 "PHP2Shell") に関するものです。これらの脆弱性は、認証されていない攻撃者が脆弱なPHPバージョンが動作しているサーバー上でリモートコード実行 (RCE) を可能にするものです。
この脆弱性の影響は、お客様がデプロイおよび運用されているDrupalベースのApigeeデベロッパーポータルに限定されます。Apigee本体、Apigee Hybrid、およびApigee統合ポータルはPHPを使用していないため、この脆弱性の影響は受けません。

影響有無：
**影響の有無は、お客様のApigeeデベロッパーポータルの構成に依存します。**
*   **影響あり:** お客様が**DrupalをベースとしたApigeeデベロッパーポータルを構築・運用している場合**、PHPの脆弱性によりリモートコード実行のリスクが存在します。
*   **影響なし:** Apigee本体、Apigee Hybrid、Apigee統合ポータルをご利用の場合、またはDrupalベースではないカスタムデベロッパーポータルをご利用の場合、この脆弱性の直接的な影響は受けません。

対処方法：
お客様がDrupalベースのApigeeデベロッパーポータルを運用している場合は、以下の対応を推奨します。
1.  **セキュリティ速報の確認:** まず、[GCP-2026-072のセキュリティ速報](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-072)を参照し、詳細な情報と推奨される対策を確認してください。
2.  **PHPバージョンの確認とアップデート:** 運用中のDrupal環境で使用されているPHPのバージョンを確認し、速報で指定されている修正済みバージョン、または可能な限り最新の安定版バージョンへアップデートを検討してください。Drupalの公式ドキュメントやセキュリティ勧告も併せて参照し、適切な対応を実施してください。
3.  **システムへの影響評価:** アップデートを実施する前に、本番環境への影響を最小限に抑えるため、開発/ステージング環境での十分なテストを実施してください。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures):** 既知のサイバーセキュリティの脆弱性を識別するための国際的な識別子システムです。特定の脆弱性に関する情報共有を容易にします。
*   **Apigee Developer Portal:** APIを利用する開発者向けに、APIのドキュメント、登録、テスト、キー管理などの機能を提供するウェブポータルです。Apigeeユーザーはこれを通じてAPIを公開し、開発者に利用を促します。
*   **Drupal:** オープンソースのコンテンツ管理システム (CMS) です。Apigee Developer Portalは、Drupalを基盤として構築されることがあります。
*   **リモートコード実行 (RCE - Remote Code Execution):** 攻撃者が遠隔地から標的のコンピュータ上で任意のコードを実行できる脆弱性、またはその状態を指します。これにより、システムへの完全な制御を奪取される可能性があります。

---

# Compute Engine
## Security
原文: A vulnerability (CVE-2026-85299) about incorrect authorization in Compute Engine was discovered and has been addressed. For more information, see the GCP-2026-073 security bulletin.

[GCP-2026-073 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-073)

説明：
Compute Engineにおいて、不適切な承認に関する脆弱性 (CVE-2026-85299) が発見されましたが、この脆弱性はすでにGoogle Cloudによって対処済みであることがアナウンスされました。詳細については、セキュリティ速報GCP-2026-073を参照してください。

影響有無：
**影響なし。**
この脆弱性はGoogle Cloud側で既に「addressed (対処済み)」と報告されているため、お客様側での緊急の対応は不要です。これは、Google Cloudがサービス基盤の脆弱性を検出し、プロアクティブに修正を適用したことを意味します。

対処方法：
お客様側での緊急の対処は不要ですが、セキュリティプラクティスとして、以下の対応を推奨します。
1.  **セキュリティ速報の確認:** [GCP-2026-073のセキュリティ速報](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-073)を参照し、この脆弱性がお客様のCompute Engineの利用方法に対して間接的な影響がないか、または今後のセキュリティ運用において留意すべき点がないかを確認することをお勧めします。通常、"addressed"とある場合は、追加の顧客アクションは不要です。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures):** 既知のサイバーセキュリティの脆弱性を識別するための国際的な識別子システムです。特定の脆弱性に関する情報共有を容易にします。
*   **Incorrect Authorization (不適切な承認):** システムが、正当な権限を持たないユーザーやプロセスに対して、本来アクセスが許可されるべきではないリソースや機能へのアクセスを誤って許可してしまう脆弱性を指します。これにより、機密情報への不正アクセスや、不正な操作が可能になるリスクがあります。
# Title: October 24, 2026 
Link: https://docs.cloud.google.com/release-notes#October_24_2026<br>
# Cloud Run
## Security
原文: The following runtime languages contain important security updates:

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
[Ruby 3.3 and later](https://docs.cloud.google.com/run/docs/runtime-support#ruby)
[.NET 6 and later](https://docs.cloud.google.com/run/docs/runtime-support#.net)
The following stacks and their underlying operating system packages have also been updated:

- `google-22`, `google-22-full`
- `google-24`, `google-24-full`

Take immediate protective action by rebuilding and redeploying your resources with updated dependencies.

See Security bulletins for Google Cloud for more information.

[Security bulletins for Google Cloud](https://docs.cloud.google.com/support/bulletins)

説明:
Cloud Runで提供されているマネージドランタイムおよび基盤となるオペレーティングシステムパッケージに対して、重要なセキュリティアップデートが適用されました。
このアップデートは、以下のランタイム言語の特定のバージョン以降、および`google-22`、`google-22-full`、`google-24`、`google-24-full`スタックに影響します。これらのアップデートには、潜在的なセキュリティ脆弱性に対する修正が含まれています。Google Cloudは、影響を受けるリソースについて、速やかに依存関係を更新して再構築し、再デプロイすることで、保護措置を講じることを推奨しています。

影響有無:
**影響あり**:
貴社のCloud Runサービスが、上記のリリースノートに記載されているGo、Node.js、Java、PHP、Python、Ruby、.NETのいずれかのランタイム言語の指定バージョン以降を使用している場合、または`google-22`、`google-22-full`、`google-24`、`google-24-full`スタックをベースイメージとして利用している場合に影響があります。
**理由**:
これらのアップデートは「重要なセキュリティアップデート」であり、脆弱性の修正が含まれています。既存のサービスがこれらの更新を適用していない場合、セキュリティ上のリスクにさらされる可能性があります。

対処方法:
1.  **利用状況の確認**: 現在Cloud Runでデプロイしているサービスが、対象のランタイム言語のバージョンまたはスタック（`google-22`, `google-22-full`, `google-24`, `google-24-full`）を使用しているかを確認してください。特に、公式のランタイムを使用している場合や、これらのスタックをベースとしたカスタムイメージを使用している場合は、対応が必要です。
2.  **アプリケーションイメージの再構築**: 該当するCloud Runサービスについて、最新の依存関係を取り込んだ上でアプリケーションイメージを再構築してください。通常、Dockerイメージを再ビルドすることで最新のパッチが適用されます。
3.  **Cloud Runサービスへの再デプロイ**: 再構築した新しいアプリケーションイメージをCloud Runサービスにデプロイしてください。これにより、最新のセキュリティパッチが適用されたランタイムおよびOS環境でサービスが実行されるようになります。
4.  **CI/CDパイプラインのレビュー**: CI/CD（継続的インテグレーション/継続的デリバリー）パイプラインを使用している場合は、ビルドプロセスが常に最新のベースイメージや依存関係を取得・使用するように設定されていることを確認してください。

用語説明:
*   **ランタイム (Runtime)**: プログラムを実行するために必要な実行環境やライブラリ群の総称です。Cloud Runでは、特定のプログラミング言語（例: Go、Node.js、Pythonなど）に対応したマネージドな実行環境を提供しています。
*   **スタック (Stack)**: Cloud Runにおいて、アプリケーションの実行基盤となるOSや共通ライブラリ、ランタイムなどがプリインストールされたベースイメージを指します。`google-22`や`google-24`は、それぞれDebian 11 (Bullseye) や Debian 12 (Bookworm) をベースとしたGoogle提供のビルド済み環境です。
*   **再構築 (Rebuild)**: アプリケーションのソースコードと依存関係を用いて、Dockerイメージなどのデプロイ可能な成果物を再度作成するプロセスです。これにより、最新のパッチやライブラリが組み込まれます。
*   **再デプロイ (Redeploy)**: 既存のCloud Runサービスに対して、新しく構築されたアプリケーションイメージを適用し、再度展開することです。これにより、サービスの稼働中のインスタンスが新しいイメージに切り替わります。
*   **依存関係 (Dependencies)**: アプリケーションが正しく動作するために必要とする、外部のライブラリ、フレームワーク、モジュール、ソフトウェアパッケージなどのことです。
*   **セキュリティ脆弱性 (Security Vulnerability)**: ソフトウェアやシステムの設計、実装、設定に存在する欠陥で、悪意のある攻撃者によって悪用され、システムへの不正アクセス、情報漏洩、サービス妨害などのセキュリティ上の問題を引き起こす可能性があるものです。
*   **Google Cloud Composer 2**: Apache AirflowをGoogle Cloud上でマネージドサービスとして提供するものです。今回のリリースノートはCloud Runに関するものであり、Composerのランタイムやその環境には直接的な影響はありません。しかし、ComposerからCloud Runサービスを呼び出しているようなワークフローがある場合、呼び出されるCloud Runサービス側での対応が必要です。
# Title: October 23, 2026 
Link: https://docs.cloud.google.com/release-notes#October_23_2026<br>
Google Cloudのリリースノートに基づき、構築済みのサービスへの影響調査結果を以下の通り報告いたします。

---

# Cloud Monitoring
## Fixed
原文: Ops Agent version 2.73.0 includes patches for a Go vulnerability involving system root certificates, CVE-2026-111943. For more information, see Ops Agent 2.73.0 notes.
[CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943)
[Ops Agent 2.73.0 notes](https://github.com/GoogleCloudPlatform/ops-agent/releases/tag/2.73.0)

説明：
Ops Agent のバージョン 2.73.0 に、Go 言語におけるシステムルート証明書に関する脆弱性 (CVE-2026-111943) の修正パッチが含まれました。この修正により、Ops Agent を利用するシステムのセキュリティが強化されます。

影響有無：
影響: なし（直接的な影響はなし、セキュリティ向上による間接的なプラスの影響）
理由: Google Cloud Composerはマネージドサービスであり、その基盤となるVMやコンポーネントでOps Agentが使用されている場合でも、それらの管理とアップデートはGoogle Cloud側で行われるため、お客様側で直接 Ops Agent のバージョンを管理・更新する必要はありません。もしComposer環境内のVMに対してお客様が独自にOps Agentをインストールし管理している場合は、そのOps Agentが更新対象となります。

対処方法：
特別な対処は不要です。Google Cloud マネージドサービスの一部として Ops Agent が利用されている場合は、Google Cloud 側で計画的にアップデートが適用されます。お客様がVMに独自にOps Agentをデプロイしている場合は、バージョン 2.73.0 以降への更新を検討してください。

用語説明：
*   **Ops Agent**: Google Cloud の VM インスタンスやオンプレミスサーバーから、ログ（Cloud Logging）とメトリック（Cloud Monitoring）を収集するための統合エージェントです。以前の Monitoring Agent と Logging Agent の機能を統合しています。
*   **Go vulnerability**: Go言語で記述されたソフトウェアにおける脆弱性を指します。本件では、システムがルート証明書を扱う方法に関連するセキュリティ上の問題が修正されました。
*   **CVE-2026-111943**: 共通脆弱性識別子（Common Vulnerabilities and Exposures）は、公開されている情報セキュリティ脆弱性に一意の識別番号を付与するシステムです。この番号は、特定の Go 言語の脆弱性を示しています。

---

# Cloud SQL for PostgreSQL
## Security
原文: In response to GCP-2026-071, Google is updating Cloud SQL's managed components. No manual updates to the certificate store are required for Cloud SQL-managed instances. The fix is shipping in a new maintenance version that will be applied during scheduled maintenance. You can also apply the fix by performing self-service maintenance. An announcement will be published when the self-service maintenance fix is available.

**What should I do?**
- If you use the Cloud SQL Auth Proxy, then upgrade the Cloud SQL Auth Proxy to 2.26.3 or later and the Cloud SQL Proxy Operator to 1.8.4 or later. If you run the standalone proxy binary, then also update the host's certificate authority (CA) certificates.
- If you use a Cloud SQL Language Connector, then update the language runtime and operating system CA certificates used with the Cloud SQL Language Connector (for example, Go 1.26.10 or 1.27.3 or later, certifi 2026.10.19 or later).
- If you're using the gcloud CLI to install the Cloud SQL Auth Proxy, then update the gcloud CLI to 590.0.1.

[GCP-2026-071](https://docs.cloud.google.com/support/bulletins#gcp-2026-071)
[scheduled maintenance](https://docs.cloud.google.com/sql/docs/postgres/maintenance)
[performing self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance)
[2.26.3 or later](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#install)
[1.8.4 or later](https://docs.cloud.google.com/sql/docs/postgres/connect-proxy-operator)
[Cloud SQL Language Connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors)
[590.0.1](https://docs.cloud.google.com/sdk/gcloud#download_and_install_the)

説明：
GCP-2026-071 で識別されたセキュリティ脆弱性に対応するため、Cloud SQL の管理コンポーネントが更新されます。Cloud SQL が管理するインスタンス（Cloud Composer のメタデータデータベースなど）の場合、証明書ストアの手動更新は不要で、定期メンテナンスまたはセルフサービスメンテナンスによって自動的に修正が適用されます。
しかし、Cloud SQL への接続に使用しているクライアント側コンポーネントには、お客様によるアップデートが必要となる場合があります。具体的には、Cloud SQL Auth Proxy、Cloud SQL Proxy Operator、Cloud SQL Language Connector、または gcloud CLI を使用している場合に影響があります。

影響有無：
影響: あり（潜在的なセキュリティリスクとその回避のためのクライアント側コンポーネントのアップデートが必要）
理由: Google Cloud ComposerのメタデータデータベースはCloud SQL for PostgreSQLでホストされており、そのインスタンスはGoogle Cloudによって管理されているため、インスタンス自体の修正は自動的に行われます。
しかし、DAGのデプロイやAirflowのCLI操作など、Composer環境外からCloud SQL Auth Proxyやgcloud CLIを使用してCloud SQLに接続している場合、セキュリティ強化のためにこれらのクライアント側コンポーネントのバージョンアップが必要です。既存のクライアント環境を更新しない場合、将来的に接続問題が発生したり、セキュリティリスクにさらされる可能性があります。

対処方法：
1.  **Cloud SQL インスタンス本体**:
    Cloud Composerのメタデータデータベースとして利用されているCloud SQLインスタンスは、Google Cloudの定期メンテナンス中に自動的に修正が適用されます。緊急で適用を希望する場合は、セルフサービスメンテナンスの提供が開始され次第、利用を検討してください。

2.  **お客様側のクライアントツール**:
    Cloud Composer (Composer version 2.7.1, Airflow version 2.7.3) の利用環境において、以下のいずれかの方法でCloud SQLに接続している場合は、それぞれ対応が必要です。
    *   **Cloud SQL Auth Proxy を利用している場合**:
        *   Cloud SQL Auth Proxy をバージョン 2.26.3 以降にアップグレードしてください。
        *   Kubernetes 環境で Cloud SQL Proxy Operator を利用している場合は、Operator をバージョン 1.8.4 以降にアップグレードしてください。
        *   スタンドアロンの Cloud SQL Auth Proxy バイナリを使用している場合は、その実行環境（ホストOS）の Certificate Authority (CA) 証明書も併せて更新してください。
    *   **Cloud SQL Language Connector を利用している場合**:
        *   Cloud Composerの環境では直接利用されることは稀ですが、もし利用している場合は、使用している言語ランタイム（例: Go 1.26.10 または 1.27.3 以降）およびオペレーティングシステムの CA 証明書を最新のものに更新してください。
    *   **gcloud CLI を使用して Cloud SQL Auth Proxy をインストールしている場合**:
        *   gcloud CLI をバージョン 590.0.1 以降にアップデートしてください。

これらの更新は、計画的なメンテナンス期間中に実施し、更新後の接続確認を十分に行ってください。

用語説明：
*   **GCP-2026-071**: Google Cloud Platformにおける特定のセキュリティ脆弱性に対応するための内部識別子です。詳細情報は、関連するGoogle Cloudサポート速報で公開されます。
*   **Cloud SQL Auth Proxy**: Cloud SQL インスタンスに安全に接続するためのプロキシアプリケーションです。データベースクライアントと Cloud SQL インスタンス間の接続を暗号化し、Google Cloud IAM ベースの認証を可能にします。
*   **Cloud SQL Proxy Operator**: Kubernetes 環境において、Cloud SQL Auth Proxy のデプロイとライフサイクルを管理するための Kubernetes Operator です。
*   **Certificate Authority (CA) 証明書**: 公開鍵インフラストラクチャ（PKI）において、デジタル証明書を発行し、その信頼性を保証する第三者機関（認証局）によって発行される証明書です。セキュアな通信において、通信相手の身元を検証するために使用されます。
*   **Cloud SQL Language Connector**: Cloud SQL と連携するために、特定のプログラミング言語（Go、Pythonなど）から利用されるライブラリやツールキットの総称です。
*   **gcloud CLI**: Google Cloud をコマンドラインから操作するための統合ツールキットです。リソースの管理、デプロイ、監視など、幅広いタスクに使用されます。