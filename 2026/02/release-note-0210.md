
# Title: February 06, 2026 
Link: https://docs.cloud.google.com/release-notes#February_06_2026<br>
ご担当者様

Google Cloudのリリースノートに関する調査結果をご報告いたします。
以下の内容をご確認ください。

---

# Apigee X

## Announcement

原文: On February 6th, 2026, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：2026年2月6日、Apigeeの新しいバージョンがリリースされました。このリリースは本日よりGoogle Cloudの全ゾーンへのロールアウトが開始されており、完了までに4営業日以上かかる可能性があります。ロールアウトが完了するまで、お客様のApigeeインスタンスでは新機能や修正が利用できない場合があります。

影響有無：
*   **影響あり（ポジティブ）**：ApigeeサービスはGoogleが管理するマネージドサービスであるため、自動的に最新バージョンにアップデートされます。これにより、サービスが最新の状態に保たれ、新しい機能や改善が享受できます。
*   **影響あり（一時的）**：ロールアウト期間中は、インスタンスが最新の機能や修正を即座に利用できない可能性があります。

対処方法：
*   お客様側での特別な対処は不要です。Google Cloudによる自動アップデートが適用されます。
*   新しい機能の利用を計画している場合は、全ゾーンへのロールアウト完了まで時間を要する可能性があることを考慮してください。

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームの最新バージョンで、APIの設計、セキュアな公開、運用、分析を包括的に行うことができます。
*   **ロールアウト (Rollout)**: 新しいソフトウェアバージョンや機能が段階的に展開・適用されるプロセスを指します。全ユーザーや全リージョンに一度に適用するのではなく、安定性を確保しながら徐々に適用範囲を広げます。

## Security

原文: | Bug ID | Description |
|---|---|
| **477294854, 477297075, 477297324, 470988850, 471662549** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:- CVE-2025-58187- CVE-2025-61723- CVE-2025-61725- CVE-2025-61729- CVE-2025-61727 |
This addresses the following vulnerabilities:- CVE-2025-58187- CVE-2025-61723- CVE-2025-61725- CVE-2025-61729- CVE-2025-61727

[CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187)
[CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723)
[CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725)
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)
[CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)

説明：Apigeeインフラストラクチャに対するセキュリティ修正が適用されました。この修正により、以下の複数のCVE（共通脆弱性識別子）に関連する脆弱性に対処されています。提供されているリンクから各CVEの詳細情報を確認できます。

影響有無：
*   **影響あり（ポジティブ）**：基盤となるApigeeインフラストラクチャのセキュリティが強化され、既知の脆弱性が修正されるため、サービス全体のセキュリティ態勢が向上します。お客様のAPIゲートウェイの安全性が高まります。

対処方法：
*   Apigeeはマネージドサービスであるため、これらのセキュリティ修正はお客様の操作なしにGoogle Cloud側で自動的に適用されます。
*   お客様側での特別な対処は不要です。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: サイバーセキュリティの脆弱性や情報セキュリティの公開された脆弱性を識別するために使用される国際的な標準識別子です。
*   **脆弱性 (Vulnerability)**: ソフトウェアやシステムの設計上の欠陥、または設定ミスなどに起因するセキュリティ上の弱点であり、悪用されると情報漏洩や不正アクセスなどの被害につながる可能性があります。

---

# Compute Engine

## Change

原文: Expanded coverage for compute flexible committed use discounts (CUDs) is available to all Cloud Billing accounts. All Cloud Billing accounts have been automatically migrated to the new spend-based CUD model and you no longer need to opt in to benefit from the expanded coverage. For the full list of eligible SKUs across Compute Engine, GKE, and Cloud Run, see SKU Groups - Compute Flexible CUD Eligible SKUs.
[new spend-based CUD model](https://docs.cloud.google.com/docs/cuds-multiprice)
[SKU Groups - Compute Flexible CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/compute-flexible-cud-eligible-skus)
To learn more about compute flexible CUDs and how they apply to your usage, see the compute flexible CUDs documentation.
[compute flexible CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based)

説明：Compute Engineの柔軟なコミットメント利用割引（CUD）の適用範囲が、すべてのCloud Billingアカウントに拡大されました。これにより、既存のすべてのCloud Billingアカウントは、新しい利用額ベースのCUDモデルに自動的に移行され、拡大された割引の恩恵を受けるためのオプトインが不要になりました。対象となるSKU（製品サービス単位）は、Compute Engine、Google Kubernetes Engine（GKE）、Cloud Runにまたがります。詳細な対象SKUリストは提供されているリンクから確認できます。

影響有無：
*   **影響あり（ポジティブ）**：すべてのCloud Billingアカウントで、自動的にコミットメント割引の適用範囲が拡大されます。これにより、Compute Engine、GKE、Cloud Runといった多様なサービスにおける利用コストの削減機会が増加します。以前は手動でのオプトインが必要でしたが、その手間が不要になりました。
*   **影響なし（設定変更不要）**：既存のコミットメントは自動的に新しいモデルに移行されるため、お客様側での設定変更や移行作業は不要です。

対処方法：
*   お客様側で特別な対処は不要ですが、コスト最適化の観点から以下の対応を推奨します。
    *   **SKUグループの確認**: 提供されている「SKU Groups - Compute Flexible CUD Eligible SKUs」のリンクを確認し、現在利用しているサービスが新たに割引対象になっているか、または割引率が変更されたかどうかを把握してください。
    *   **コスト分析**: Cloud Billingレポートを活用し、新しいCUDモデルがどの程度のコスト削減に貢献しているか、または今後コミットメントを追加することで更なる削減が可能かを定期的に評価してください。
    *   **コミットメント戦略の見直し**: 既存のワークロードと将来の計画に基づいて、Compute Flexible CUDの最適なコミットメント戦略を再検討してください。

用語説明：
*   **CUD (Committed Use Discounts)**: Google Cloudのサービス利用に対して一定期間（通常1年または3年）のコミットメントを行うことで、オンデマンド料金よりも大幅な割引が適用される料金体系です。
*   **SKU (Stock Keeping Unit)**: 製品やサービスの料金を計算するための最小単位です。Google Cloudでは、例えば特定のVMタイプ、ストレージの種類、データ転送量などが個別のSKUとして定義されています。
*   **Spend-based CUD model (利用額ベースのCUDモデル)**: 従来の特定リソース（例: 特定のvCPU数やメモリ量）にコミットするモデルとは異なり、対象となるサービス群（例: Compute Engine、GKE、Cloud Run）の総利用額に対して割引が適用されるCUDモデルです。これにより、リソースの利用状況に柔軟に対応しながら割引を受けやすくなります。
*   **Cloud Billing account**: Google Cloudプロジェクトの利用料金を管理するためのアカウントです。これに紐づくすべてのプロジェクトの利用料金が一元的に課金されます。

---

ご不明な点がございましたら、お気軽にお問い合わせください。