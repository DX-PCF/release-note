
# Title: March 25, 2026 
Link: https://docs.cloud.google.com/release-notes#March_25_2026<br>
Google Cloudインフラエンジニアとして、リリースノートに基づく影響調査結果を報告します。

---

# AlloyDB for PostgreSQL
## Change
原文: When no major version is specified, AlloyDB for PostgreSQL now defaults to PostgreSQL major version 17 for new clusters.
[PostgreSQL major version 17](https://docs.cloud.google.com/alloydb/docs/db-version-policies#support-table)

説明：
AlloyDB for PostgreSQLにおいて、新規クラスタを作成する際にデータベースのメジャーバージョンを明示的に指定しない場合、デフォルトでPostgreSQL 17が選択されるように変更されました。

影響有無：
**影響なし（既存クラスタ）**
*   既に稼働しているAlloyDBクラスタのバージョンには影響しません。この変更は「新規クラスタ (new clusters)」の作成時のみに適用されます。

**影響あり（新規クラスタ作成時）**
*   今後AlloyDBクラスタを新規作成する際に、もし明示的にバージョンを指定しない場合、自動的にPostgreSQL 17でクラスタが作成されます。特定の旧バージョン（例: 14, 15, 16）での作成を意図している場合は、注意が必要です。

対処方法：
*   **既存クラスタ**: 不要です。
*   **新規クラスタ作成時**: もしPostgreSQL 17以外のバージョン（例: PostgreSQL 14, 15, 16）でクラスタを作成したい場合は、クラスタ作成時に `--database-version` オプションを使用して希望するメジャーバージョンを明示的に指定してください。
    *   例: `gcloud alloydb clusters create <CLUSTER_ID> --database-version=POSTGRES_14 --project=<PROJECT_ID> --region=<REGION>`

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、PostgreSQLと互換性のあるフルマネージドなエンタープライズグレードのリレーショナルデータベースサービスです。高いパフォーマンス、可用性、スケーラビリティが特徴です。
*   **PostgreSQL major version 17**: オープンソースのリレーショナルデータベースシステムであるPostgreSQLの主要なバージョンの一つです。メジャーバージョンアップでは、新機能の追加、パフォーマンス改善、セキュリティ強化などが行われますが、互換性に影響する変更が含まれる場合もあります。
*   **新規クラスタ (new clusters)**: まだ作成されていない、これから新たにプロビジョニングされるデータベースクラスタを指します。

---

# BigQuery
## Announcement
原文: The Gemini for Google Cloud API (cloudaicompanion.googleapis.com) is now enabled for existing BigQuery projects in the European jurisdiction.
[Gemini for Google Cloud API](https://docs.cloud.google.com/gemini/docs/overview)

説明：
Gemini for Google Cloud API (`cloudaicompanion.googleapis.com`) が、欧州管轄（European jurisdiction）に属する既存のBigQueryプロジェクトにおいて有効化されました。

影響有無：
**影響なし（欧州管轄外のプロジェクト）**
*   欧州管轄外のGoogle Cloudプロジェクトを使用している場合、この変更による直接的な影響はありません。

**影響あり（欧州管轄内のプロジェクト）**
*   欧州管轄に属する既存のBigQueryプロジェクトでは、Gemini for Google Cloud APIに関連する機能（例: Duet AI for Google Cloudが提供するSQL生成、コード補完などのAIアシスタント機能）が利用可能になります。これにより、データアナリストや開発者の生産性向上が期待されます。
*   APIが自動的に有効化されるため、特別な設定は不要です。しかし、組織のセキュリティポリシーやデータ利用ポリシーによっては、このAPIの利用を制限する必要があるか確認してください。

対処方法：
*   **欧州管轄外のプロジェクト**: 特段の対応は不要です。
*   **欧州管轄内のプロジェクト**:
    *   通常は特別な対処は不要であり、利便性の向上が期待されます。
    *   もし、Gemini for Google Cloud APIの利用を制限したい場合は、該当プロジェクトまたは組織レベルで `cloudaicompanion.googleapis.com` APIを無効化するか、APIを利用するためのIAM権限（例: `cloudaicompanion.apiUser` ロール）を適切に管理することを検討してください。

用語説明：
*   **Gemini for Google Cloud API**: Google Cloudの基盤となるAIモデルであるGeminiをGoogle Cloudサービス全体で活用するためのAPIです。Duet AI for Google CloudなどのAIアシスタント機能のバックエンドとして機能します。
*   **`cloudaicompanion.googleapis.com`**: Gemini for Google Cloud APIのサービス名（APIエンドポイント）です。Google CloudのAPI管理画面でこのサービスを有効/無効に設定できます。
*   **European jurisdiction**: 欧州連合（EU）のデータ保護規制（GDPRなど）が適用される地理的管轄区域を指します。Google Cloudは、顧客が欧州内でデータを保持できるよう、特定のリージョンや管轄区域を提供しています。
*   **BigQuery**: Google Cloudが提供する、ペタバイト規模のデータを分析できるフルマネージドなデータウェアハウスサービスです。
*   **Duet AI for Google Cloud**: Google Cloud全体で利用可能なAIアシスタント機能のブランド名です。コードの生成、デバッグ支援、SQLの作成補助など、多様な開発・運用タスクをAIが支援します。
# Title: March 24, 2026 
Link: https://docs.cloud.google.com/release-notes#March_24_2026<br>
Google Cloudのリリースノートに関する調査結果を報告します。

---

# Cloud Storage

## Announcement
原文: `Anywhere Cache has been renamed to Rapid Cache.`

説明：
Cloud Storageの機能である「Anywhere Cache」が「Rapid Cache」に名称変更されました。これは機能の提供内容や動作に変更はなく、単なる名称の変更となります。

影響有無：
**なし**

*   **機能的な影響**: 名称変更のみであり、Cloud Storageの既存の構成、API、機能、パフォーマンス、セキュリティ、料金体系、リージョン/ゾーンの可用性には直接的な影響はありません。現在利用されている「Anywhere Cache」機能の動作に変更はありません。
*   **構成的な影響**: お客様が現在お使いのCloud Storage FUSEの設定やコマンドラインインターフェースにおける指定方法に変更は生じません。
*   **Google Cloud Composer**: Cloud Storageの名称変更であり、Google Cloud Composer (Composer version 2.7.1, Airflow version 2.7.3)の動作や構成に直接的な影響はありません。

対処方法：
**不要**

*   技術的な対処は不要です。
*   今後、Google CloudのドキュメントやUI上では「Rapid Cache」という新しい名称が使用されるようになりますので、この変更を認識しておいてください。
*   社内ドキュメントやトレーニング資料などで「Anywhere Cache」という旧名称が使われている場合、情報の鮮度を保つために「Rapid Cache」へ更新を検討することは推奨されますが、必須ではありません。

用語説明：
*   **Anywhere Cache / Rapid Cache**: Google Cloud Storageをファイルシステムとしてマウントできるオープンソースアダプターである「Cloud Storage FUSE」において利用できるクライアントサイドキャッシュ機能です。この機能は、頻繁にアクセスされるファイルやディレクトリのメタデータ、および一部のオブジェクトデータをローカルディスクにキャッシュすることで、Cloud Storageへのアクセスレイテンシを削減し、特に多くの小さなファイルを扱うワークロードや、読み込み頻度の高いデータへのアクセスパフォーマンスを向上させます。元々「Anywhere Cache」という名称でしたが、より機能特性を反映した「Rapid Cache」に改名されました。
*   **Cloud Storage FUSE**: Google Cloud StorageバケットをLinuxまたはmacOSのファイルシステムとしてマウントし、アプリケーションが通常のファイル操作（読み書き、ディレクトリ参照など）を通じてCloud Storageのデータにアクセスできるようにするオープンソースソフトウェアです。これにより、オブジェクトストレージであるCloud Storageを、あたかもローカルファイルシステムのように扱えるようになります。
# Title: March 23, 2026 
Link: https://docs.cloud.google.com/release-notes#March_23_2026<br>
# Cloud Billing
## Change
原文: **Billing account permissions now streamline access to Google payments profiles and payments accounts**

We've launched a billing IAM permissions update that simplifies and streamlines Cloud Billing account access to the associated Google payments profiles and accounts, for users who have the `billing.accounts.updatePaymentInfo` permission on their Cloud Billing account.

[Google payments profiles and accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account)
**Prior to this update**: *While working in the Cloud Billing console*, to access and edit the associated Google payments profile and account information, all Cloud Billing account users **needed *two* sets of permissions**:

- Identity and Access Management (IAM) permissions on the Cloud Billing account to access and manage the billing account.
- Edit or Admin access permissions on the associated Google payments profile in order to add and edit payment methods, make a manual payment, and update payments profile info such as the business name, address, tax info, and payments account settings.

[permissions on the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
[access permissions on the associated Google payments profile](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions)
**After this permissions update**: Cloud Billing account users with the `billing.accounts.updatePaymentInfo` permission on the billing account can access and edit Google payments profile and account information directly from the Cloud Billing console, without needing additional permissions on the payments profile itself.
This includes users with the Billing Account Administrator role (`roles/billing.admin`) and those granted this permission via a custom role.

[Billing Account Administrator role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)
[custom role](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information)
Note that this permissions update applies only to Cloud Billing accounts associated with an Organization (or Business) Google payments profile type. You can verify your account type on the Payment settings page in the Cloud Billing console.

[Organization (or Business)](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types)
[Payment settings](https://console.cloud.google.com/billing/profile)
With the `billing.accounts.updatePaymentInfo` permission on the billing account, users can do the following:

- View payments history and documents related to the associated Google payments profile.
- Add and edit payment methods on a self-serve (online) billing account.
- Make a manual payment to a self-serve (online) billing account.
- Update payments profile info such as the business name, address, tax info, and payments account settings.

[View payments history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
[documents](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
[Add and edit payment methods](https://docs.cloud.google.com/billing/docs/how-to/payment-methods)
[Make a manual payment](https://docs.cloud.google.com/billing/docs/how-to/manual-payment)
[Update payments profile info](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account)
Billing account users with the `billing.accounts.updatePaymentInfo` permission won't have the *Manage users* or *Admin with all permissions* level of access on the Google payments profile. To *fully manage* a payments profile and gain *Manage users* and *Admin* permissions, billing account users still require additional *Google payments user permissions* granted on the associated payments profile.

[*Manage users* and *Admin* permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions)
[*Google payments user permissions*](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts)

説明：
この更新により、Cloud BillingのIAM権限を持つユーザーが、関連するGoogle Payments Profileにアクセスする際の権限管理が簡素化されます。

*   **変更前**: Cloud BillingコンソールからGoogle Payments Profileの情報（支払い方法、請求先情報など）を管理するには、Cloud Billingアカウントに対するIAM権限に加えて、Google Payments Profile自体に対する個別の編集または管理者権限が必要でした。
*   **変更後**: `billing.accounts.updatePaymentInfo`権限（`roles/billing.admin`ロールに含まれる、またはカスタムロールで付与）を持つCloud Billingアカウントユーザーは、Cloud Billingコンソールから直接Google Payments Profileの情報を閲覧・編集できるようになります。これにより、Google Payments Profile側で別途権限を付与する必要がなくなります。
*   対象となる操作: 支払い履歴の表示、関連ドキュメントの表示、支払い方法の追加・編集、手動支払い、ビジネス名・住所・税務情報などの支払いプロファイル情報の更新が含まれます。
*   注意点: この変更は、組織またはビジネスタイプのGoogle Payments Profileに紐付けられたCloud Billingアカウントにのみ適用されます。また、Google Payments Profileの「ユーザー管理」や「完全な管理者権限」を得るためには、引き続きGoogle Payments Profile側で個別の権限を付与する必要があります。

影響有無：
**影響なし（利便性向上）**。既存のサービスへの直接的な影響（稼働停止、機能不全など）はありません。
`billing.accounts.updatePaymentInfo`権限を持つユーザーが支払い情報を管理する際の操作性が向上し、権限付与が簡素化されるため、運用の利便性が向上します。既存の権限が剥奪されるわけではないため、既存の運用に悪影響はありません。

対処方法：
必須の対処はありません。
ただし、IAM権限管理のベストプラクティスとして、この変更を機に、`billing.accounts.updatePaymentInfo`権限を付与されているユーザーが、意図した範囲で支払い情報にアクセス・変更できるかを確認することを推奨します。これにより、最小権限の原則が適切に適用されているか再評価できます。

用語説明：
*   **Cloud Billing account**: Google Cloudで利用したリソースの料金を計算・請求するためのアカウントです。
*   **Google Payments Profile**: Googleサービス全般（Google Cloud、Google Play、Google Adsなど）で利用する支払い方法、請求先住所、税務情報などの支払いに関する詳細を管理するプロファイルです。
*   **IAM (Identity and Access Management)**: Google Cloudのリソースに対するアクセス権限を管理するためのフレームワークです。誰が（Who）どのリソースに（What）どのような操作を（Can do）できるかを定義します。
*   **`billing.accounts.updatePaymentInfo` permission**: Cloud Billingアカウントの支払い情報を更新するために必要なIAM権限です。この権限は、通常`roles/billing.admin`（Billing Account Administrator）ロールに含まれています。
*   **Organization (or Business) Google Payments Profile type**: 企業や組織がGoogleサービスを利用する際に選択する支払いプロファイルのタイプです。個人向けのプロファイルとは異なり、複数のユーザーがアクセスしたり、VAT IDなどのビジネス関連情報を登録したりできます。
*   **Self-serve (online) billing account**: ユーザー自身がオンラインポータルを通じて支払い方法の管理や請求書の確認などを行えるタイプの請求アカウントです。
*   **Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3)**: リリースノートの内容はCloud Billingに関するものであり、Cloud Composerのバージョンに特化した影響はありません。