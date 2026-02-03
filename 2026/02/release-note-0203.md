
# Title: February 02, 2026 
Link: https://docs.cloud.google.com/release-notes#February_02_2026<br>
以下は、提供されたリリースノートに対する調査結果です。

---

# API Gateway
## Change
原文: Connect API Gateway to Apigee API hub instances that use VPC Service Controls. API Gateway can now be connected to Apigee API hub instances that use VPC Service Controls.
[connected to Apigee API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-connect)
[VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc)

説明：
API Gateway が、VPC Service Controls で保護された Apigee API hub インスタンスに接続できるようになりました。これにより、API Gateway を介して公開される API が、VPC Service Controls でセキュリティ境界が確立された Apigee API hub 内の API 資産と連携可能になります。

影響有無：
**影響はありません。**
この変更は、API Gateway の新たな接続オプション（機能追加）であり、既存の構成や利用方法に直接的な影響を与えるものではありません。現在 API Gateway または Apigee API hub を利用している環境において、既存の動作が変更されることはありません。
もし、将来的に API Gateway と Apigee API hub を VPC Service Controls のセキュリティ境界内で連携させる必要が生じた場合には、この新機能が利用できます。

対処方法：
現在のシステム構成で Apigee API hub と API Gateway の連携が必要なく、VPC Service Controls による境界保護が不要な場合は、**特に対応は不要**です。
もし、今後 VCP Service Controls で保護された環境下で API Gateway と Apigee API hub を連携させる要件が発生した場合は、本機能の利用を検討してください。詳細な設定方法については、提供されているリンク先のドキュメントを参照してください。

用語説明：
*   **API Gateway:** Google Cloud 上で API の作成、公開、保護、監視を行うためのフルマネージドサービスです。バックエンドのサービス（Cloud Functions, Cloud Run, Compute Engine, GKE など）へのアクセスを統一されたエンドポイントで提供し、API のトラフィック管理やセキュリティ強化に利用されます。
*   **Apigee API hub:** 組織内の API をカタログ化し、検索、共有、再利用を促進するためのハブです。API のライフサイクル管理を支援し、開発者が必要な API を簡単に見つけられるようにすることで、API の利用促進と統制を図ります。
*   **VPC Service Controls:** データ漏洩のリスクを軽減するために、Google Cloud サービスに対するセキュリティ境界（サービス境界）を定義する機能です。指定したサービス境界内からのアクセスのみを許可することで、機密データの不正な外部転送や、誤設定によるデータ公開を防ぎ、セキュリティを強化します。特に規制の厳しい業界や機密性の高い情報を扱う場合に利用されます。
# Title: January 30, 2026 
Link: https://docs.cloud.google.com/release-notes#January_30_2026<br>
# Cloud Storage
## Announcement
原文: `Object change notification is deprecated on January 30, 2026. To generate notifications for changes to objects, use Pub/Sub notifications for Cloud Storage instead.`

説明：
Google Cloud Storageにおけるオブジェクト変更通知のレガシーな機能が、2026年1月30日をもって非推奨となることが発表されました。この機能は、Cloud Storageバケット内のオブジェクト（ファイルなど）が作成、更新、削除されるといった変更があった際に、指定されたエンドポイントに通知を送信するものです。今後は、オブジェクトの変更通知を生成するためには、より堅牢でスケーラブルな「Pub/Sub notifications for Cloud Storage」を使用することが推奨されます。

影響有無：
**影響あり（条件付き）**
現在、既存のシステムでGoogle Cloud Storageの「Object change notification」機能を利用している場合、将来的にこの機能が利用できなくなるため、影響があります。2026年1月30日までに代替手段である「Pub/Sub notifications for Cloud Storage」への移行が必要となります。
この機能を利用していない場合は、直接的な影響はありません。ただし、今後Cloud Storageのオブジェクト変更通知機能を実装する際には、最初からPub/Subベースの通知を利用すべきです。

対処方法：
現在「Object change notification」を利用している場合は、以下の手順で「Pub/Sub notifications for Cloud Storage」への移行を計画・実行してください。
1.  **現状把握:** 既存のシステムがどのCloud Storageバケットに対して、どのような条件で「Object change notification」を設定しているかを確認します。
2.  **移行計画:** 新しい通知メカニズムである「Pub/Sub notifications for Cloud Storage」を用いたシステム設計を検討します。Pub/Subトピックの作成、通知設定の構成、そしてPub/Subメッセージを処理するためのアプリケーション（例: Cloud Functions, Cloud Run, Compute Engineなど）の開発または改修が含まれます。
3.  **移行作業:** 既存の通知設定を削除し、新しいPub/Subベースの通知設定を適用します。アプリケーション側も新しい通知形式に対応するように変更し、テストを行います。
4.  **期限:** 2026年1月30日までに移行を完了させる必要があります。

詳細な移行手順については、以下のGoogle Cloud公式ドキュメントを参照してください。
[Pub/Sub notifications for Cloud Storage への移行](https://docs.cloud.google.com/storage/docs/migrate-to-pub-sub-notifications)

用語説明：
*   **Object change notification:** Cloud Storageのバケット内のオブジェクト（ファイル）の変更（作成、更新、削除など）を検知し、HTTP POSTリクエストとして特定のURLに通知を送信する古い形式の機能です。
*   **Pub/Sub notifications for Cloud Storage:** Cloud Storageのオブジェクト変更イベントをGoogle Cloud Pub/Subというメッセージングサービスに発行する、推奨される新しい形式の通知機能です。Pub/Subを介することで、イベントドリブンなアーキテクチャの構築が容易になり、スケーラビリティと信頼性が向上します。
*   **Deprecated (非推奨):** 将来的に機能が利用できなくなり、サポートが終了する予定であることを意味します。現在利用中の場合は、代替機能への移行が強く推奨されます。
*   **Google Cloud Pub/Sub:** Google Cloudが提供するフルマネージドな非同期メッセージングサービスです。発行者-購読者モデルに基づき、スケーラブルで信頼性の高いメッセージングを実現します。アプリケーション間の連携やイベントドリブン処理に利用されます。