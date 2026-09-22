
# Title: September 21, 2026 
Link: https://docs.cloud.google.com/release-notes#September_21_2026<br>
# Apigee X
## Announcement
原文: On September 21st, 2026, we began maintenance updates of Apigee instances configured for maintenance windows. If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-4**, your instance will be updated to **1-18-0-apigee-4** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will not be updated:
- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.

[Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues)
[Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)
For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.

[Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance)
[Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)

説明：
Google Cloudは、Apigee Xインスタンスのメンテナンスアップデートを開始したことを発表しました。このアップデートは、メンテナンスウィンドウを設定しているApigeeインスタンスが対象となります。現在のインスタンスバージョンが「1-18-0-apigee-4」未満の場合、設定されたメンテナンスウィンドウ期間中に自動的に「1-18-0-apigee-4」へアップグレードされます。アップグレードの正確な日程は、今後2営業日以内に通知され、通知後7日から21日以内に実施される予定です。

ただし、以下の2つの条件のいずれかに該当するインスタンスは、このアップデートの対象外となります。
1.  DNS設定に誤りがあるインスタンス（既知のIssue 445936920に記載）。
2.  廃止されたApigee Javaライブラリを使用しているインスタンス（2025年10月16日付のApigeeリリースノートに記載）。

影響有無：
**影響あり。**
Apigee Xを利用しており、メンテナンスウィンドウを設定しているインスタンス、かつ現在のバージョンが「1-18-0-apigee-4」未満である場合、自動的にバージョンアップが実施されます。これは、Apigeeプラットフォームの動作に影響を与える可能性があります。特に、DNS設定不備や廃止されたJavaライブラリを使用している場合はアップデートがスキップされるため、これらの問題を解決しない限り最新バージョンへ移行できません。意図しないバージョンのスキップは、将来的な機能利用やサポートに影響を与える可能性があります。

対処方法：
1.  **通知の確認**: まず、Google Cloudからの通知メールを確認し、Apigeeインスタンスの具体的なアップグレード予定日を把握してください。
2.  **現行バージョンの確認**: ご利用のApigeeインスタンスの現在のバージョンを確認し、「1-18-0-apigee-4」未満であるかを確認してください。
3.  **互換性テスト**: 可能であれば、アップグレード後のバージョン（「1-18-0-apigee-4」）で既存のAPIプロキシやポリシーが意図通りに動作するかを、テスト環境などで事前に確認することを推奨します。
4.  **例外条件の確認と対応**:
    *   インスタンスがDNS設定不備に該当しないか確認してください。もし該当する場合は、問題解決のため[Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues)を参照し、対応を検討してください。
    *   廃止されたApigee Javaライブラリを使用していないか確認してください。使用している場合は、[Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)を参照し、代替手段への移行を検討してください。これらの問題が解決されない限り、インスタンスは最新バージョンにアップデートされません。
5.  **メンテナンスウィンドウの考慮**: メンテナンスウィンドウ中にアップグレードが行われるため、この期間にサービスへの影響が発生しないか、または許容範囲内であるかを確認し、必要に応じて事業影響緩和策を講じてください。

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージド型のAPI管理プラットフォームです。APIの設計、デプロイ、セキュリティ、スケーリング、分析などを一元的に管理できます。
*   **Maintenance Windows (メンテナンスウィンドウ)**: クラウドサービスプロバイダーが、システムのアップデートや保守作業を行うために、ユーザーが事前に設定または合意する期間のことです。この期間中に一時的にサービスに影響が出る可能性があります。
*   **DNS misconfiguration (DNS設定不備)**: Domain Name System (DNS) の設定に誤りがある状態を指します。これにより、ドメイン名から正しいIPアドレスへの解決ができなくなり、サービスへのアクセスができなくなるなどの問題が発生します。
*   **Apigee Java Library**: Apigeeプラットフォーム上で、APIプロキシのカスタムロジックや高度な機能を実現するために、Javaコードを記述する際に使用される特定のライブラリ群です。