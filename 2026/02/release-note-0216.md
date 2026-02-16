
# Title: February 13, 2026 
Link: https://docs.cloud.google.com/release-notes#February_13_2026<br>
# Apigee X

## Announcement
原文: On February 13, 2026, we published a security bulletin for Apigee.
説明：2026年2月13日にApigeeに関するセキュリティ速報が公開された旨のアナウンスです。これは、後述のセキュリティ脆弱性に関する速報となります。
影響有無：このアナウンス自体は情報提供であり、直接的なシステムへの影響はありません。後述のセキュリティ脆弱性の内容を確認する必要があります。
対処方法：このアナウンス単体での対処は不要です。関連するセキュリティ脆弱性の内容に基づき対応を検討します。
用語説明：
*   **Security bulletin (セキュリティ速報)**: ソフトウェアやシステムにおけるセキュリティ上の脆弱性や脅威に関する情報、およびそれらに対処するためのパッチや回避策を提供する公式通知です。

## Security
原文: A vulnerability was identified in the Apigee platform (CVE-2025-13292) that could have allowed a malicious actor with administrative or developer-level permissions in their own Apigee environment to elevate privileges and access cross-tenant data.
[CVE-2025-13292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-13292)
**Security bulletin published: GCP-2026-010**
[GCP-2026-010](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-010)

説明：Apigeeプラットフォームにおいて、CVE-2025-13292として特定された脆弱性が発見されました。この脆弱性により、攻撃者が自身のApigee環境内で管理者または開発者レベルの権限を持っている場合、特権を昇格させ、他のテナントのデータにアクセスできる可能性がありました。関連するセキュリティ速報「GCP-2026-010」が公開されています。

影響有無：
*   **Apigee X を利用している場合**：影響がある可能性があります。この脆弱性はApigeeプラットフォーム自体に存在するため、お使いの環境が影響を受ける可能性があります。特権昇格やテナント間のデータアクセスが可能になることで、機密データの漏洩やシステム不正操作のリスクが考えられます。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) を利用している場合**：本リリースノートはApigee Xに関するものであり、Google Cloud Composerとは直接的な関連がないため、Composer環境への直接的な影響はありません。

対処方法：
Apigee XはGoogle Cloudのマネージドサービスであるため、通常、脆弱性に対するパッチ適用や基盤の修正はGoogle側で実施されます。お客様側で直接パッチを適用する作業は不要であると見込まれます。

しかしながら、以下の対応を推奨します。
1.  **セキュリティ速報の確認**: 公開されたセキュリティ速報「GCP-2026-010」の内容を詳細に確認してください。Googleがどのような対策を講じたのか、ユーザー側で確認・実施すべき設定変更、ログの監視、アクセス権限の見直しなど、具体的な推奨事項が記載されている可能性があります。
2.  **アクセス権限の見直し**: 脆弱性の前提として「自身のApigee環境内で管理者または開発者レベルの権限を持っている場合」とあるため、Apigee環境におけるIAMロールやポリシーが適切に設定されているか、最小権限の原則が守られているかを確認し、不要な権限が付与されていないか徹底してください。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: サイバーセキュリティの脆弱性に一意の識別子を割り当てるための国際的な標準規格です。この識別子を通じて、脆弱性に関する情報を共有しやすくなります。
*   **特権昇格 (Privilege Escalation)**: 攻撃者が、正規のユーザーアカウントやシステムが持つ権限よりも高いレベルの権限を獲得する行為です。これにより、通常では実行できない操作（例: システム設定の変更、データの削除・窃取）が可能になります。
*   **クロス・テナント (Cross-tenant)**: マルチテナント環境において、あるテナントのデータやリソースが、別のテナントから不正にアクセスされたり、影響を受けたりする状態を指します。クラウドサービスでは、複数の顧客（テナント）が同じ基盤を共有するため、このような問題は重大なセキュリティリスクとなります。