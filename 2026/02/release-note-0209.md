
# Title: February 06, 2026 
Link: https://docs.cloud.google.com/release-notes#February_06_2026<br>
Google Cloud のインフラエンジニアとして、お問い合わせいただいたリリースノートについて、構築済みサービスへの影響を調査し、以下の通りご報告いたします。

---

# Apigee X

## Announcement
原文: On February 6th, 2026, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
Apigeeの新しいバージョンがリリースされました。このリリースは、本日からGoogle Cloudの全てのゾーンへの展開が開始され、完了までに4営業日以上かかる可能性があります。展開が完了するまでは、新しい機能や修正がお客様のApigeeインスタンスで利用できない場合があります。

影響有無：
影響なし（ただし、情報把握は必要）。これは新バージョンのリリースに関するアナウンスであり、既存の構成に直接的な非互換性や即時のアクションを必要とするものではありません。ただし、後述のセキュリティ修正を含むため、システムが更新されることでセキュリティ体制が向上します。ロールアウト期間中は、新機能や修正が適用されていない可能性がある点に留意が必要です。

対処方法：
特段の対処は不要です。Google Cloud側で自動的にロールアウトが進行します。セキュリティ修正が適用されるのを待つことになります。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **477294854, 477297075, 477297324, 470988850, 471662549** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:- CVE-2025-58187- CVE-2025-61723- CVE-2025-61725- CVE-2025-61729- CVE-2025-61727 |
This addresses the following vulnerabilities:- CVE-2025-58187- CVE-2025-61723- CVE-2025-61725- CVE-2025-61729- CVE-2025-61727
[CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187)
[CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723)
[CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725)
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)
[CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)

説明：
Apigeeの基盤インフラストラクチャに対するセキュリティ修正が適用されました。この修正は、特定された複数のCVE（共通脆弱性識別子）に対応し、セキュリティ脆弱性を解消します。

影響有無：
影響あり（ポジティブ）。既存のApigeeインスタンスのセキュリティが向上します。ユーザー側での直接的な操作は不要ですが、基盤レベルでの脆弱性が修正されるため、より安全な環境でAPI管理サービスを運用できるようになります。

対処方法：
特段の対処は不要です。Google Cloud側で自動的に修正が適用されます。これにより、お客様のApigeeインスタンスのセキュリティが自動的に強化されます。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures):** ソフトウェアの脆弱性を識別し、公開するための国際的な標準識別子です。これにより、ITシステムにおけるセキュリティ脆弱性を共通の認識で管理・追跡できます。

---

# Compute Engine

## Change
原文: Expanded coverage for compute flexible committed use discounts (CUDs) is available to all Cloud Billing accounts. All Cloud Billing accounts have been automatically migrated to the new spend-based CUD model and you no longer need to opt in to benefit from the expanded coverage. For the full list of eligible SKUs across Compute Engine, GKE, and Cloud Run, see SKU Groups - Compute Flexible CUD Eligible SKUs.
[new spend-based CUD model](https://docs.cloud.google.com/docs/cuds-multiprice)
[SKU Groups - Compute Flexible CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/compute-flexible-cud-eligible-skus)
To learn more about compute flexible CUDs and how they apply to your usage, see the compute flexible CUDs documentation.
[compute flexible CUDs documentation](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based)

説明：
Compute Engine のフレキシブル コミットメント利用割引（CUDs）の適用範囲が全てのCloud Billingアカウントに拡大されました。既存の全てのCloud Billingアカウントは、新しい「支出ベースのCUDモデル」へ自動的に移行されたため、ユーザーは追加の操作なしに、この拡張された割引の恩恵を受けられます。Compute Engine、GKE、Cloud Runをまたがる対象SKUのリストは、関連ドキュメントで確認できます。

影響有無：
影響あり（ポジティブ）。Compute Engine、GKE、Cloud Runを利用している場合、既存の課金アカウントが自動的に新しい支出ベースのCUDモデルに移行され、より広範なSKUに対して割引が適用される可能性が高まります。これにより、追加の費用なしでクラウド費用の最適化が進む可能性があります。パフォーマンスや機能動作への影響はありません。

対処方法：
特段の対処は不要です。お客様のCloud Billingアカウントは自動的に移行されます。
推奨されるアクションとしては、Google Cloudの課金レポート（Billing Reports）を確認し、Compute Flexible CUDsがどのように適用され、全体的な費用にどのような影響を与えているか（コスト削減効果）を定期的にモニタリングすることをお勧めします。

用語説明：
*   **CUDs (Committed Use Discounts):** コミットメント利用割引。特定のGoogle Cloudリソースを一定期間（例：1年または3年）利用することをコミット（確約）することで、オンデマンド料金よりも大幅な割引を受けられる料金体系です。
*   **Compute Flexible CUDs:** Compute Engine、GKE、Cloud RunのCompute関連の費用に対して適用されるCUDの一種です。インスタンスタイプやリージョンに縛られず、利用したComputeの支出全体に対して割引が適用される柔軟なモデルです。
*   **Spend-based CUD model:** 支出ベースのCUDモデル。従来のCUDが特定のリソース（例：特定のvCPU数やメモリ量）をコミットする形式であったのに対し、支出ベースのCUDは、対象となるサービスでの「支出額」をコミットする形式であり、より柔軟な割引適用が可能です。