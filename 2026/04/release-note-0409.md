
# Title: April 06, 2026 
Link: https://docs.cloud.google.com/release-notes#April_06_2026<br>
以下に、Google Cloudのリリースノートに基づいたサービスへの影響調査結果を簡潔にまとめました。

---

# Apigee X

## Change

原文: On April 6th, 2026, we released an updated version of Apigee. This change introduces the new `apigee.coreServiceAgent` IAM role for Apigee. **Effective immediately, use `apigee.coreServiceAgent` instead of the `apigee.serviceAgent` role.** For information on the new role, see [`apigee.coreServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent).

説明: Apigeeの更新版が2026年4月6日にリリースされ、新しいIAMロールである`apigee.coreServiceAgent`が導入されました。この変更により、既存の`apigee.serviceAgent`ロールの代わりに、`apigee.coreServiceAgent`ロールを即座に使用することが求められています。

影響有無: **あり。**
既存のApigee環境で`apigee.serviceAgent`ロールを使用している場合、新しいロールへの移行が必要です。特に、新規でApigeeインスタンスをプロビジョニングする際や、既存のサービスアカウントの権限設定を見直す際に影響します。既存の運用中の環境で権限の変更を伴わない限り、即座のサービス停止には繋がりませんが、今後の運用や新しい機能を利用する上でこのロールへの移行が必須となります。

対処方法:
1.  既存のApigee環境におけるIAMポリシーを確認し、`apigee.serviceAgent`ロールが付与されているサービスアカウントを特定します。
2.  Google CloudのIAMドキュメント（リンク先の`apigee.coreServiceAgent`を参照）を確認し、新しいロールの権限と移行手順を理解します。
3.  本番環境に適用する前に、テスト環境で`apigee.coreServiceAgent`ロールへの置き換えを慎重に実施し、Apigeeの機能が正常に動作することを確認します。
4.  新規にApigee環境を構築する場合は、最初から`apigee.coreServiceAgent`ロールを使用するように設定します。

用語説明:
*   **IAMロール (Identity and Access Management Role):** Google Cloudのリソースへのアクセス権限を定義する論理的なグループ。特定の操作（リソースの作成、読み取り、更新、削除など）を実行するために必要な権限の集合が含まれます。
*   **`apigee.serviceAgent` / `apigee.coreServiceAgent`:** ApigeeサービスがGoogle Cloud内の他のリソース（例: Cloud Storage, Cloud Pub/Subなど）にアクセスするために使用する特別なサービスアカウントに付与されるIAMロールです。Apigeeの内部的な運用に必要な権限をカプセル化しています。`apigee.coreServiceAgent`は、より新しい、または特定のコア機能に特化した権限セットを持つと推測されます。

## Fixed

原文: **Correction to April 2, 2026 release note: Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace** For the deployment disruption announced on April 2, the announcement noted that deployment and management functionality using Google Cloud Deployment Manager would definitely be unavailable during the transition. This statement is incorrect. The functionality *might* be unavailable. See the Known issue for more information. [`Known issue`](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258)

説明: 2026年4月2日のリリースノートで発表された、Google Cloud Marketplace経由でのApigee Drupal Portalのデプロイ中断に関する内容が訂正されました。以前はGoogle Cloud Deployment Managerを使用したデプロイおよび管理機能が移行期間中に「確実に」利用不可になるとされていましたが、この記述は誤りであり、「利用不可になる『可能性が』ある」に修正されました。詳細は既知の問題（Known issue）を参照するよう促されています。

影響有無: **限定的。**
これは過去の誤ったアナウンスの訂正であり、サービスの動作そのものが変更されたわけではありません。Apigee Drupal PortalをGoogle Cloud Marketplace経由でデプロイまたは管理しているユーザーが対象ですが、既知の問題として利用不可になる可能性が継続していることに変わりはありません。ただし、「確実に」から「可能性が」に訂正されたことで、影響の度合いに関する情報がより正確になりました。

対処方法:
1.  Apigee Drupal PortalをGoogle Cloud Marketplace経由でデプロイまたは管理している場合は、リンクされている「Known issue」ドキュメント（[https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258)）を確認し、最新の情報と推奨される対応策を把握してください。
2.  デプロイや管理作業を行う際は、引き続き機能が一時的に利用できない可能性を考慮し、時間的余裕を持って計画してください。
3.  必要に応じて、代替のデプロイ/管理手段やワークアラウンドを検討してください。

用語説明:
*   **Apigee Drupal Portal:** Apigee Edge (API管理プラットフォーム) で公開されているAPIを、開発者向けに一覧表示し、ドキュメントやテスト機能を提供するポータルサイトを構築するためのDrupalベースのソリューションです。
*   **Google Cloud Marketplace:** Google Cloud上で利用可能なサードパーティ製ソフトウェアやソリューションを検索、デプロイ、管理できるプラットフォームです。
*   **Google Cloud Deployment Manager:** Google Cloudリソースのデプロイを自動化し、Infrastructure as Codeを実現するためのサービスです。YAMLまたはPythonを使用してリソースの設定を定義し、デプロイ、更新、削除を行います。
*   **Known issue (既知の問題):** 製品やサービスにおいて、開発者によって認識されているが、まだ解決されていない問題やバグのこと。通常、その問題の再現手順、影響範囲、回避策などが公開されます。

---

# Cloud Logging

## Libraries

## Go

原文: [`v1.14.0`](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.2...logging/v1.14.0)

説明: Google Cloud LoggingのGo言語向けクライアントライブラリがバージョン1.14.0に更新されました。これは、主にライブラリ内部の改善、バグ修正、または新しいAPI機能への対応などが含まれるマイナーバージョンアップです。

影響有無: **間接的。**
Google Cloudのサービス自体への影響ではなく、Cloud LoggingのGoクライアントライブラリを使用しているアプリケーションに影響があります。通常、マイナーバージョンアップでは後方互換性が維持されますが、念のため変更内容を確認することが推奨されます。現在運用しているアプリケーションがこのライブラリに依存している場合、新しい機能を利用したい場合や、特定のバグ修正を取り込みたい場合にバージョンアップを検討する必要があります。

対処方法:
1.  自身のGoアプリケーションでCloud LoggingのGoクライアントライブラリを使用しているか確認します。
2.  リンク先のGitHubリポジトリ（`https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.2...logging/v1.14.0`）を参照し、v1.13.2からv1.14.0への具体的な変更点（コミット履歴、`CHANGELOG.md`など）を確認します。特に、後方非互換な変更や、重要なバグ修正が含まれていないか注意深く確認してください。
3.  もしアプリケーションでバージョンアップを検討する場合は、テスト環境でライブラリのバージョンを更新し、既存の機能が正常に動作するか、期待される改善が適用されているかなど、回帰テストと機能テストを実施してください。

用語説明:
*   **Go (Golang):** Googleが開発したオープンソースのプログラミング言語で、効率的なコンパイル、シンプルな構文、並行処理のサポートなどが特徴です。
*   **クライアントライブラリ (Client Library):** 特定のクラウドサービス（この場合はCloud Logging）のAPIをプログラミング言語（Go）から簡単に呼び出せるようにするための、事前に構築されたコードセットです。APIリクエストの構築、認証、レスポンスのパースなどを抽象化し、開発者がAPIを直接操作する手間を省きます。
*   **Semantic Versioning (セマンティックバージョニング):** ソフトウェアのバージョン番号付けの標準的な規則（例: MAJOR.MINOR.PATCH）。MAJORは後方非互換な変更、MINORは後方互換性のある機能追加、PATCHは後方互換性のあるバグ修正を示します。今回のv1.14.0はMINORバージョンアップに該当します。