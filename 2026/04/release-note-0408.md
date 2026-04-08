
# Title: April 06, 2026 
Link: https://docs.cloud.google.com/release-notes#April_06_2026<br>
Google Cloudのリリースノートに関する調査依頼、承知いたしました。
Google Cloudのインフラエンジニアとして、各リリースノートの内容を解析し、お客様の構築済みサービスへの影響を評価します。

---

# Apigee X

## Change
原文: On April 6th, 2026, we released an updated version of Apigee. This change introduces the new `apigee.coreServiceAgent` IAM role for Apigee. **Effective immediately, use `apigee.coreServiceAgent` instead of the `apigee.serviceAgent` role.** For information on the new role, see `apigee.coreServiceAgent`.
[`apigee.coreServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent)

説明: Apigeeの更新版がリリースされ、新しいIAMロール `apigee.coreServiceAgent` が導入されました。この変更により、既存の `apigee.serviceAgent` ロールの代わりに、この新しい `apigee.coreServiceAgent` ロールを直ちに使用するよう指示されています。新しいロールに関する詳細は、提供されたドキュメントリンクを参照してください。

影響有無: **影響あり**
Apigeeを使用している既存のプロジェクトにおいて、`apigee.serviceAgent` IAMロールが割り当てられているサービスアカウントが存在する場合、このロールを `apigee.coreServiceAgent` に変更または追加する必要があります。この変更は「Effective immediately（直ちに有効）」とされており、対応が必要です。この変更はApigeeのコアサービスに関する権限に影響するため、適切なIAM設定が行われていない場合、Apigeeの機能が正常に動作しなくなる可能性があります。

対処方法:
1.  **IAMポリシーの確認**: お使いのGoogle Cloudプロジェクトで、Apigeeに関連するサービスアカウントに `apigee.serviceAgent` ロールが付与されているかを確認してください。
2.  **ロールの更新**: `apigee.serviceAgent` ロールが付与されている場合、そのサービスアカウントに対して `apigee.coreServiceAgent` ロールを付与してください。
3.  **既存ロールの削除 (推奨)**: `apigee.coreServiceAgent` ロールへの移行が完了し、問題がないことを確認した後、セキュリティベストプラクティスとして、不要になった `apigee.serviceAgent` ロールは削除することを検討してください。
4.  **ドキュメント参照**: 公式ドキュメント [`apigee.coreServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) を参照し、新しいロールの権限内容と設定方法の詳細を確認してください。

用語説明:
*   **IAMロール (Identity and Access Management Role)**: Google Cloudリソースに対するアクセス権限の集合を定義するものです。特定のサービスアカウントやユーザーに付与することで、その主体がどのような操作を行えるかを制御します。
*   **サービスアカウント (Service Account)**: Google Cloudの仮想的なIDであり、アプリケーションやワークロードがGoogle Cloud APIを呼び出す際に使用します。
*   **Apigee**: APIの設計、デプロイ、セキュリティ保護、監視、分析を行うためのAPI管理プラットフォームです。

## Fixed
原文: **Correction to April 2, 2026 release note: Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace** For the deployment disruption announced on April 2, the announcement noted that deployment and management functionality using Google Cloud Deployment Manager would definitely be unavailable during the transition. This statement is incorrect. The functionality *might* be unavailable. See the Known issue for more information.
[`Known issue`](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258)

説明: 2026年4月2日に発表された、Google Cloud Marketplace経由でのApigee Drupal Portalのデプロイ中断に関するリリースノートの訂正です。以前のアナウンスでは、Google Cloud Deployment Managerを使用したデプロイおよび管理機能が移行期間中に「確実に利用不可になる」とされていましたが、この記述は「利用不可になる *可能性* がある」に修正されました。詳細については、既知の問題（Known issue）のリンクを参照してください。

影響有無: **影響軽微**
これは以前のアナウンスの「修正」であり、機能の追加や変更ではありません。Apigee Drupal PortalをGoogle Cloud Marketplace経由でデプロイまたは管理しているユーザーは、以前の「確実な停止」という認識から、「停止する *可能性* がある」という認識に改めることで、運用計画におけるリスク評価が緩和されます。ただし、停止の可能性は依然として存在するため、注意は必要です。

対処方法:
1.  **状況認識の更新**: Apigee Drupal PortalをGoogle Cloud Marketplace経由で運用している場合、デプロイや管理機能が一時的に利用不可になる可能性があることを認識し、それに応じた運用計画（例えば、メンテナンスウィンドウの調整や代替手段の検討）を立ててください。
2.  **Known issueの確認**: 提供されている [`Known issue`](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258) のリンクを参照し、具体的な影響範囲や期間、回避策などの詳細情報を確認してください。

用語説明:
*   **Apigee Drupal Portal**: Apigeeを介してAPIを利用する開発者向けのポータルサイトを構築するためのDrupalベースのソリューションです。
*   **Google Cloud Marketplace**: Google Cloud上で利用可能なソフトウェアソリューションやサービスを見つけてデプロイできるプラットフォームです。
*   **Google Cloud Deployment Manager**: Google Cloudリソースの作成と管理を、テンプレートとして定義して自動化できるサービスです。

---

# Cloud Logging

## Libraries

## Go
原文: [v1.14.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.2...logging/v1.14.0)

説明: Google Cloud LoggingのGo言語クライアントライブラリがバージョン `v1.14.0` に更新されました。このリリースは、以前のバージョン `v1.13.2` からの変更を含んでいます。変更点の詳細は、提供されているGitHubの比較リンクで確認できます。

影響有無: **影響なし** (通常の場合)
このリリースノートは、Cloud LoggingのGo言語クライアントライブラリのバージョンアップに関するものです。お客様の環境で提供されている情報によると、「Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)」をご利用とのことですが、Composerは主にPythonベースのAirflowを使用しており、直接的にGo言語のライブラリに依存している可能性は低いと考えられます。
もし、お客様が独自にGo言語でCloud Logging APIを利用するアプリケーションを開発・運用されている場合、そのアプリケーションがこのライブラリに依存している場合にのみ影響が発生します。通常、マイナーバージョンアップでは後方互換性が保たれる傾向にありますが、機能追加やバグ修正が含まれるため、アップグレードを検討する際は変更ログの確認とテストが推奨されます。

対処方法:
*   **Go言語アプリケーションを使用していない場合**: 特段の対応は不要です。
*   **Go言語でCloud Loggingクライアントライブラリを使用している場合**:
    1.  アプリケーションの `go.mod` ファイルなどでGoクライアントライブラリの依存関係を確認してください。
    2.  `v1.14.0` へのアップグレードを検討する場合、提供されているGitHubの比較リンク ([`v1.13.2...v1.14.0`](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.2...logging/v1.14.0)) を参照し、具体的な変更点（新機能、バグ修正、潜在的な破壊的変更）を確認してください。
    3.  本番環境への適用前に、開発環境やテスト環境で十分な動作確認とテストを実施してください。

用語説明:
*   **クライアントライブラリ (Client Library)**: 特定のプログラミング言語（この場合はGo）でGoogle CloudのAPIを簡単に利用できるようにするためのコードセットです。APIの直接的なHTTPリクエストを抽象化し、開発者が使いやすい関数やオブジェクトとして提供します。
*   **Go (Golang)**: Googleが開発したオープンソースのプログラミング言語で、シンプルさ、効率性、堅牢性に重点を置いています。
*   **GitHub**: ソフトウェア開発プロジェクトのバージョン管理システムとしてGitを使用するWebサービスです。コードのホスティングや共同開発に広く利用されます。