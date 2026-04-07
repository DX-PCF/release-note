
# Title: April 06, 2026 
Link: https://docs.cloud.google.com/release-notes#April_06_2026<br>
ご担当者様

リリースノートの調査結果をご報告いたします。
構築済みのサービス（Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)）への影響有無を中心に調査いたしました。

---

# Apigee X

## Fixed

原文:
Correction to April 2, 2026 release note: Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace
 For the deployment disruption announced on April 2, the announcement noted that deployment and management functionality using Google Cloud Deployment Manager would definitely be unavailable during the transition. This statement is incorrect. The functionality *might* be unavailable.
 See the Known issue for more information.
[Known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258)

説明：
2026年4月2日に発表されたApigee Drupal Portalのデプロイメントに関するリリースノートの訂正です。以前のアナウンスでは、Google Cloud Deployment Managerを使用したデプロイメントおよび管理機能が「確実に利用不可になる」とされていましたが、この記述が誤りであり、「利用不可になる可能性が**ある**」に修正されました。詳細については、関連する既知の問題（Known issue）のドキュメントを参照するよう促しています。

影響有無：
**影響なし**
現在運用中のGoogle Cloud Composer 2 (Airflow 2.7.3) 環境には直接的な影響はありません。本リリースノートは、API管理プラットフォームであるApigee Xの特定のコンポーネント（Apigee Drupal Portal）のデプロイメント方法に関するアナウンスの訂正であり、Composerとは直接関連しないためです。

対処方法：
現在運用中のComposer環境に対する特別な対処は不要です。
もし貴社環境でApigee X、特にApigee Drupal PortalをGoogle Cloud Deployment Manager経由でデプロイ・運用されている場合は、記載されているKnown issueのドキュメントを確認し、今後の計画への影響を評価することを推奨します。

用語説明：
*   **Apigee X**: Google Cloudが提供するエンタープライズ向けのAPI管理プラットフォームです。APIの設計、セキュリティ、分析、スケーリングなどをサポートします。
*   **Apigee Drupal Portal**: Apigee API Managementの一部として、APIコンシューマ（APIを利用する開発者など）向けにAPIドキュメント、APIキー管理、API使用状況の監視機能などを提供するための開発者ポータルを構築するためのコンポーネントです。Drupalはコンテンツ管理システム（CMS）の一種です。
*   **Google Cloud Deployment Manager**: Google CloudのリソースをInfrastructure as Code (IaC) の原則に基づいて定義、デプロイ、管理するためのサービスです。YAMLなどの構成ファイルを使用して、複数のGoogle Cloudリソースをまとめてプロビジョニングできます。
*   **Known issue (既知の問題)**: 製品やサービスにおいて、開発元が認識しているがまだ修正されていない問題や制限事項のことです。これらの問題は通常、ドキュメントで公開され、回避策や影響が説明されます。

---

# Cloud Logging

## Libraries

## Go

原文:
[v1.14.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.2...logging/v1.14.0)

説明：
Go言語用のCloud Loggingクライアントライブラリが、バージョンv1.13.2からv1.14.0にアップデートされました。提供されているリンクは、GitHub上で変更内容の差分（比較）を確認するためのものです。これは、Go言語でCloud Logging APIとやり取りするアプリケーションを開発する際に使用されるライブラリの更新です。

影響有無：
**影響なし**
現在運用中のGoogle Cloud Composer 2 (Airflow 2.7.3) 環境には直接的な影響はありません。ComposerおよびAirflowは主にPythonで動作しており、Go言語のクライアントライブラリのバージョンアップは、Composerの基盤やAirflow DAGの実行には直接関係しません。この変更は、Go言語で開発されたアプリケーションがCloud Loggingサービスと連携する場合に影響します。

対処方法：
現在運用中のComposer環境に対する特別な対処は不要です。
もし貴社でGo言語を使用してCloud Loggingと連携するカスタムアプリケーションを開発・運用されている場合は、このライブラリのアップデートを検討し、アプリケーションへの影響（新機能の利用、バグ修正など）を確認することを推奨します。

用語説明：
*   **Client Library (クライアントライブラリ)**: Google Cloudの各種サービスと連携するためのプログラミング言語ごとのソフトウェア開発キット（SDK）の一部です。開発者がAPIエンドポイントに直接HTTPリクエストを構築することなく、より簡単にサービスを利用できるようにするための関数やクラスが提供されます。
*   **Go (Golang)**: Googleによって開発されたオープンソースのプログラミング言語です。高いパフォーマンス、並行処理、シンプルさを特徴とし、クラウドネイティブアプリケーションやマイクロサービスの開発によく使用されます。

---
# Title: April 03, 2026 
Link: https://docs.cloud.google.com/release-notes#April_03_2026<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響調査結果を以下に報告いたします。

---

# Cloud Logging
## Announcement
原文: Cloud Logging adds support for the `ca` multi-region. For a complete list of supported regions, see Supported regions.
[Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions)

説明:
Cloud Logging が、新たに `ca` (カナダ) マルチリージョンのサポートを開始しました。これにより、ログデータをカナダ国内の複数の地理的リージョンに冗長的に保存する選択肢が追加されます。サポートされるすべてのリージョンの詳細なリストは、提供されたリンクから確認できます。

影響有無:
影響なし。
これは新しいマルチリージョンの追加であり、既存のCloud Loggingの構成に自動的に変更が適用されることはありません。現在 `ca` マルチリージョンを使用している、またはログバケットを `ca` マルチリージョンに配置する予定がない限り、直接的な影響はありません。将来的にカナダにログデータを保持する必要がある場合、利用可能な選択肢が増えたことになります。

対処方法:
特になし。
ただし、ログデータの物理的な配置要件やコンプライアンス要件がある場合は、`ca` マルチリージョンが新たな選択肢として利用可能になったことを認識し、必要に応じてログバケットのストレージロケーション構成を検討することができます。

用語説明:
*   **Cloud Logging**: Google Cloud 環境から生成されるあらゆる種類のログデータ（アプリケーションログ、システムログ、監査ログなど）を一元的に収集、保存、分析、モニタリングするためのフルマネージドサービスです。
*   **マルチリージョン (Multi-region)**: Google Cloud のストレージロケーションの種類の一つで、データが地理的に複数のリージョンに冗長的に保存される構成を指します。これにより、単一リージョン障害からの保護や、地理的に分散したユーザーからのアクセスレイテンシの低減が図られます。Cloud Loggingのログバケットの場合、指定されたマルチリージョン内の複数のリージョンにログが自動的に複製され、高い可用性と耐久性が提供されます。
*   **ログバケット (Log bucket)**: Cloud Loggingにおいて、ログデータが最終的に保存される論理的なコンテナです。ログエントリは、ルーティングルール（シンク）に従って特定のログバケットに格納され、そこで設定された保持期間やストレージロケーション（リージョンまたはマルチリージョン）が適用されます。

---

# Identity and Access Management
## Deprecated
原文: Extended attributes for Workforce Identity Federation are deprecated. For group mapping, we recommend using SCIM instead of extended attributes. For more information, see IAM deprecations.
[SCIM](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim)
[IAM deprecations](https://docs.cloud.google.com/iam/docs/deprecations)

説明:
Identity and Access Management (IAM) の Workforce Identity Federation において使用されてきた「拡張属性 (Extended attributes)」が非推奨となりました。グループマッピング機能については、今後は拡張属性ではなく SCIM (System for Cross-domain Identity Management) を使用することが強く推奨されています。詳細な非推奨化情報については、提供されたIAM非推奨化に関するドキュメントを参照してください。

影響有無:
影響あり、または影響なし。
*   **影響なしの場合**: 現在、Workforce Identity Federation を利用していない、あるいは利用していてもグループマッピングのために「拡張属性」を明示的に使用していない場合は、直接的な影響はありません。
*   **影響ありの場合**: 現在、Workforce Identity Federation を利用しており、特に外部IDプロバイダーのグループ情報をGoogle Cloudにマッピングするために「拡張属性」を積極的に使用している場合は影響があります。非推奨化は将来的な機能の削除やサポート終了につながるため、既存の構成のレビューと代替手段への移行計画が必要です。

対処方法:
*   Workforce Identity Federation を利用していない場合は、特に対処は不要です。
*   Workforce Identity Federation を利用しており、かつグループマッピングに「拡張属性」を使用している場合は、速やかに SCIM を利用したグループマッピングへの移行を検討し、計画を策定してください。提供されている SCIM のドキュメント（[SCIM](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim)）とIAM非推奨化に関するドキュメント（[IAM deprecations](https://docs.cloud.google.com/iam/docs/deprecations)）を参照し、移行パスと期限を確認することが重要です。移行作業には、IdP側のSCIM設定変更やGoogle Cloud側のWorkforce Identityプールの設定更新が含まれる可能性があります。

用語説明:
*   **Identity and Access Management (IAM)**: Google Cloud のリソースに対するアクセス権限をきめ細かく管理するためのフレームワークとサービスです。誰が（プリンシパル）、どのリソースに対して、どのような操作（ロール）を許可されるかを定義します。
*   **Workforce Identity Federation**: 企業や組織が、既存のオンプレミスまたは他のクラウドプロバイダーのアイデンティティシステム（例: Okta、Azure AD、Active Directory Federation Services (AD FS) など）のユーザーやグループをGoogle Cloud に直接連携させ、Google Cloud リソースへのアクセスを許可するための機能です。これにより、Google Workspace アカウントを別途作成することなく、外部ユーザーがGoogle Cloud環境にアクセスできるようになります。
*   **拡張属性 (Extended attributes)**: Workforce Identity Federationにおいて、外部アイデンティティプロバイダーから受け取ったユーザーの追加属性情報（例: 部署、役職、カスタム属性など）をGoogle Cloud側で利用可能にするための設定です。これまで、これらの属性を用いてユーザーを特定のGoogle Cloudグループにマッピングするなどの用途で利用されていました。
*   **SCIM (System for Cross-domain Identity Management)**: ドメイン間でユーザーやグループのアイデンティティ情報を自動的にプロビジョニングおよびデプロビジョニングするための標準ベースのプロトコルです。Workforce Identity Federation におけるSCIMサポートは、外部IDプロバイダーのグループ情報をGoogle CloudのWorkforce Identityプールに同期し、IAMポリシーでそのグループを利用できるようにするために推奨される代替手段です。これにより、グループメンバーシップの管理が効率化されます。