
# Title: January 30, 2026 
Link: https://docs.cloud.google.com/release-notes#January_30_2026<br>
# Cloud Storage
## Announcement
原文: Object change notification is deprecated on January 30, 2026. To generate notifications for changes to objects, use Pub/Sub notifications for Cloud Storage instead.

[Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/migrate-to-pub-sub-notifications)

説明：
Cloud Storageの「Object change notification」（オブジェクト変更通知）機能が、2026年1月30日をもって非推奨（Deprecated）となります。今後、オブジェクトの変更通知を生成する場合は、「Pub/Sub notifications for Cloud Storage」を利用するように推奨されています。

影響有無：
**影響あり（ただし、即時ではない）**

現在、既存システムでCloud Storageの「Object change notification」機能を利用している場合、2026年1月30日の廃止日までに「Pub/Sub notifications for Cloud Storage」への移行作業が必要です。もしこの機能を使用していない場合は、直接的な影響はありません。

対処方法：
1.  **利用状況の確認:** まず、現在運用中のシステムでCloud Storageの「Object change notification」機能が使用されているかを確認してください。
2.  **移行計画の策定:** もし利用されている場合は、2026年1月30日までに「Pub/Sub notifications for Cloud Storage」への移行を計画・実施してください。移行に関する詳細は、提供されたリンクのドキュメントを参照してください。
    *   [Pub/Sub notifications for Cloud Storage への移行](https://docs.cloud.google.com/storage/docs/migrate-to-pub-sub-notifications)
3.  **非利用の場合:** 使用していない場合は、特に対処は不要です。しかし、将来的にオブジェクト変更通知が必要になった際には「Pub/Sub notifications for Cloud Storage」を利用することを前提として設計してください。

用語説明：
*   **Object change notification:** Cloud Storageにおけるオブジェクト（ファイル）の作成、更新、削除などの変更イベントを、指定されたHTTPエンドポイントにPOSTリクエストとして送信する、従来の通知機能です。主に外部サービスへのWebhook連携などに利用されていましたが、スケーラビリティや信頼性の面で課題がありました。
*   **Pub/Sub notifications for Cloud Storage:** Cloud Storageのオブジェクト変更イベントをGoogle Cloud Pub/Subサービスに発行する、現在の推奨される通知機能です。Pub/Subを介することで、Cloud Functions、Cloud Run、Dataflowなどの他のGoogle Cloudサービスと容易に連携でき、高い信頼性とスケーラビリティが提供されます。イベント駆動型アーキテクチャの構築に非常に有用です。
*   **Deprecated (非推奨化):** 特定の機能やプロダクトが、将来的にサポートされなくなる、あるいは廃止される予定であることをGoogle Cloudがアナウンスすることです。即座に使えなくなるわけではありませんが、新規利用は推奨されず、既存ユーザーには代替手段への移行が求められます。通常、一定の猶予期間が設けられます。