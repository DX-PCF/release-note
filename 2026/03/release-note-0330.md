
# Title: March 27, 2026 
Link: https://docs.cloud.google.com/release-notes#March_27_2026<br>
Google Cloud リリースノートに関する調査結果をご報告いたします。

---

# Cloud Composer
## Announcement
原文: `Cloud Composer 2 environments can no longer be created in Melbourne (australia-southeast2). We're switching this region to supporting only Cloud Composer 3 environments. Existing Cloud Composer 2 environments in this region aren't affected by this change.`

説明:
Google Cloud Composer 2環境は、メルボルンリージョン (australia-southeast2) での新規作成ができなくなりました。今後は、このリージョンではCloud Composer 3環境のみがサポートされます。ただし、このリージョンに既に存在するCloud Composer 2環境は、この変更による影響を受けません。

影響有無:
**影響なし。**
当社のCloud Composer 2環境は現在、`australia-southeast2` リージョンにはデプロイされていません。また、この変更は既存のCloud Composer 2環境には影響せず、新規作成にのみ適用されるため、運用中のサービスへの影響はありません。

対処方法:
**特になし。**
将来的に `australia-southeast2` リージョンでCloud Composer環境を新規構築する必要が生じた場合は、Cloud Composer 3の使用を前提として計画してください。

用語説明:
*   **Cloud Composer**: Google Cloud 上で Apache Airflow を実行するためのマネージドサービスです。ワークフローのオーケストレーション、スケジューリング、監視を容易に行うことができます。
*   **Apache Airflow**: プログラムによるワークフローのオーサリング、スケジューリング、監視を行うためのオープンソースプラットフォームです。
*   **australia-southeast2**: Google Cloud のメルボルンリージョンを指すIDです。

---

# Compute Engine
## Security
原文: `A vulnerability (CVE-2026-23268) about CrackArmor was discovered and has been addressed. For more information, see the GCP-2026-015 security bulletin.`

説明:
CrackArmorに関する脆弱性 (CVE-2026-23268) が発見されましたが、Googleによって既にこの脆弱性への対処が完了しています。詳細については、[GCP-2026-015 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-015) を参照してください。

影響有無:
**影響なし。**
リリースノートには「has been addressed (対処済み)」と明記されており、[GCP-2026-015 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-015) にも「**No customer action is required.** Google has applied a fix to the underlying infrastructure that prevents this issue from affecting any existing or future Compute Engine instances.」と記載されています。これは、基盤となるインフラストラクチャレベルでGoogleによって修正が適用されており、既存または新規のCompute Engineインスタンスには影響がないことを意味します。

対処方法:
**特になし。**
Google Cloudの基盤インフラストラクチャにて既に修正が適用済みのため、お客様側での追加対応は不要です。

用語説明:
*   **Compute Engine**: Google Cloud 上で仮想マシン (VM) を実行できるサービスです。柔軟な仮想ハードウェア構成と多様なOSイメージをサポートします。
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているセキュリティ脆弱性に一意の識別子を割り当てる国際的な標準システムです。
*   **CrackArmor**: この文脈では具体的な技術的詳細は公開されていませんが、Google Cloudの内部的なセキュリティコンポーネントまたは脆弱性のある技術的課題を指していると考えられます。
*   **GCP Security Bulletin**: Google Cloud Platformにおけるセキュリティ脆弱性や、それに対するGoogleの対応、ユーザー側で必要となる措置に関する情報を提供する公式の速報です。
# Title: March 26, 2026 
Link: https://docs.cloud.google.com/release-notes#March_26_2026<br>
お客様がご利用中のサービス（Google Cloud Composer2, Compoer version 2.7.1, Airflow version 2.7.3）に照らし合わせ、提示されたApigee Xのリリースノートの影響を調査しました。

# Apigee X

## Announcement
原文: On March 26th, 2026, we released an updated version of Apigee (1-17-0-apigee-6).
> Note: Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: 2026年3月26日にApigeeの更新バージョン(1-17-0-apigee-6)がリリースされました。このリリースは現在Google Cloudの全ゾーンへのロールアウトが進行中であり、完了までには4営業日以上かかる場合があります。ロールアウトが完了するまで、お使いのApigeeインスタンスでは新機能や修正が利用できない可能性があります。
影響有無: **影響なし。** 本リリースはApigee Xに関するものであり、お客様がご利用中のGoogle Cloud Composer2には直接的な影響はありません。Apigee XはComposerとは独立したサービスです。
対処方法: 特になし。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **495897297, 495909767** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: - CVE-2026-33210- CVE-2026-25679- CVE-2026-27139- CVE-2026-27142- 2026-33186 |
This addresses the following vulnerabilities: - CVE-2026-33210- CVE-2026-25679- CVE-2026-27139- CVE-2026-27142- 2026-33186
- CVE-2026-33210- CVE-2026-25679- CVE-2026-27139- CVE-2026-27142- 2026-33186
[CVE-2026-33210](https://nvd.nist.gov/vuln/detail/CVE-2026-33210)
[CVE-2026-25679](https://nvd.nist.gov/vuln/detail/CVE-2026-25679)
[CVE-2026-27139](https://nvd.nist.gov/vuln/detail/CVE-2026-27139)
[CVE-2026-27142](https://nvd.nist.gov/vuln/detail/CVE-2026-27142)
[2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186)

説明: Apigeeインフラストラクチャにおける複数のセキュリティ脆弱性（CVE-2026-33210, CVE-2026-25679, CVE-2026-27139, CVE-2026-27142, CVE-2026-33186）が修正されました。
影響有無: **影響なし。** 本修正はApigee Xのインフラストラクチャに対するものであり、お客様がご利用中のGoogle Cloud Composer2には直接的な影響はありません。Apigee Xをご利用の場合でも、Google Cloudが管理するサービスであるため、インフラレベルのセキュリティパッチは自動的に適用されます。
対処方法: 特になし。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **N/A** | **Updates to infrastructure and libraries.** |

説明: Apigeeのインフラストラクチャおよびライブラリが更新されました。
影響有無: **影響なし。** 本更新はApigee Xに関するものであり、お客様がご利用中のGoogle Cloud Composer2には直接的な影響はありません。
対処方法: 特になし。

---

**用語説明:**
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームです。APIの設計、開発、セキュリティ、モニタリング、収益化などを一元的に行います。
*   **Google Cloud Composer**: Google Cloud上でApache Airflowをマネージドサービスとして提供するものです。ワークフローのオーケストレーションを可能にします。
*   **CVE (Common Vulnerabilities and Exposures)**: 既知のサイバーセキュリティの脆弱性とその公開情報に与えられる識別子です。セキュリティの脆弱性を識別し、公開するために使用されます。