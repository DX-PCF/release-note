
# Title: May 22, 2026 
Link: https://docs.cloud.google.com/release-notes#May_22_2026<br>
# Apigee X

## Announcement: Apigee Emulator v2.0.0

原文:
On May 22, 2026, we released Apigee Emulator version 2.0.0.
Starting with this release, the Apigee Emulator is versioned and released independently from Apigee hybrid. This enables faster delivery of security patches and updates without waiting for hybrid release cycles. The emulator image continues to be available at Google Artifact Registry.
To use the new version, update the emulator version in your VS Code Cloud Code settings to `2.0.0`. See Manage the Apigee Emulator for details.

説明：
Apigee Emulator のバージョン 2.0.0 がリリースされました。このバージョンから Apigee Emulator は Apigee Hybrid とは独立してバージョン管理・リリースされるようになり、Apigee Hybrid のリリースサイクルに依存せずにセキュリティパッチやアップデートが迅速に提供されるようになります。エミュレータイメージは引き続き Google Artifact Registry で入手可能です。新しいバージョンを使用するには、VS Code Cloud Code の設定でエミュレータのバージョンを `2.0.0` に更新する必要があります。

影響有無：
**影響あり。**
Apigee Emulator を使用して Apigee の開発を行っている場合、特に VS Code Cloud Code を利用している開発者は、エミュレータのバージョンを手動で `2.0.0` に更新する必要があります。更新しない場合でも既存の環境は動作しますが、最新の機能やセキュリティ修正の恩恵を受けられません。

対処方法：
Apigee Emulator を利用している開発者は、VS Code Cloud Code の設定を開き、Apigee Emulator のバージョンを `2.0.0` に更新してください。詳細な手順は、公式ドキュメント「[Manage the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#choose_the_emulator_version)」を参照してください。

用語説明：
*   **Apigee Emulator**: Apigee API プロキシをローカル環境で開発・テストするためのツール。Apigee Hybrid 環境のAPIランタイムをシミュレートします。
*   **Apigee Hybrid**: Apigee のデプロイメントモデルの一つで、API ランタイムを顧客のデータセンターや Google Cloud の Compute Engine、Google Kubernetes Engine (GKE) などにデプロイし、管理プレーンは Google Cloud でホストされる形式です。
*   **Google Artifact Registry**: Google Cloud が提供する、コンテナイメージ、Maven パッケージ、npm パッケージなどのアーティファクトを一元的に保存、管理、共有するためのサービスです。
*   **VS Code Cloud Code**: Visual Studio Code (VS Code) の拡張機能で、Google Cloud のアプリケーション開発を支援するツール群です。Kubernetes や Cloud Run などの開発・デプロイを容易にします。

## Security: Apigee Emulator

原文:
This release addresses 78 security vulnerabilities across Cassandra base image, Go standard library, Java dependencies, and Python packages. Key fixes include: (表にCVE番号とコンポーネントが記載) And 68 additional CVEs fixed through updated upstream dependencies.

説明：
Apigee Emulator のこのリリースでは、Cassandra のベースイメージ、Go の標準ライブラリ、Java の依存関係、および Python パッケージにおける合計78のセキュリティ脆弱性に対処されました。これには、Jackson Databind、SnakeYAML、Google Guava、Logback、Go stdlib、Python setuptools の特定の CVE などが含まれます。また、アップストリームの依存関係の更新を通じて68の追加の CVE も修正されています。

影響有無：
**影響あり（ポジティブな影響）。**
Apigee Emulator を使用している場合、これらのセキュリティ修正により、エミュレータのセキュリティ体制が大幅に強化されます。既存のワークロードへの直接的な負の影響はありません。

対処方法：
このセキュリティ修正の恩恵を受けるには、Apigee Emulator を前述の v2.0.0 に更新してください。開発環境のセキュリティを向上させるために、速やかに更新することを強く推奨します。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 一般的な脆弱性と露出の識別子。公開されている情報セキュリティの脆弱性に関するデータベースで、各脆弱性に一意のIDが付与されます。
*   **Jackson Databind**: Java の JSON プロセッシングライブラリの一つです。
*   **SnakeYAML**: YAML 1.1 の Java パーサーおよびエミッターライブラリです。
*   **Google Guava**: Google が提供する Java のコアライブラリ集です。
*   **Logback**: Java アプリケーション向けのロギングフレームワークです。
*   **Go stdlib**: Go 言語の標準ライブラリです。
*   **Python setuptools**: Python プロジェクトのパッケージングを容易にするライブラリです。
*   **アップストリームの依存関係 (Upstream Dependencies)**: あるソフトウェアが利用している、より基盤となるライブラリやコンポーネントのことです。これらの依存関係にセキュリティ問題があった場合、その依存関係を更新することで自身のソフトウェアの脆弱性が解消されます。