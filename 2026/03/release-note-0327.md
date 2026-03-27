
# Title: March 26, 2026 
Link: https://docs.cloud.google.com/release-notes#March_26_2026<br>
ご担当者様

Google Cloudのリリースノートに関するお問い合わせありがとうございます。
Apigee Xのリリースノートについて、製品への影響有無および対処方法を調査し、以下の通りご報告いたします。

---

# Apigee X

## Announcement

*   **原文**:
    On March 26th, 2026, we released an updated version of Apigee (1-17-0-apigee-6).
    > **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

*   **説明**:
    2026年3月26日に、Apigeeの新しいバージョン `1-17-0-apigee-6` がリリースされました。このリリースのロールアウトは本日開始され、全てのGoogle Cloudゾーンへの適用が完了するまでに4営業日以上かかる場合があります。ロールアウトが完了するまで、お客様のApigeeインスタンスでは新しい機能や修正が利用できない可能性があります。

*   **影響有無**:
    影響なし。Apigee XはGoogleによって管理されるフルマネージドサービスであるため、お客様側でのバージョンアップ作業は不要です。新しいバージョンはGoogleによって自動的に適用されます。ただし、ロールアウト期間中は、新機能や修正が一時的に利用できないゾーンが存在する可能性があります。

*   **対処方法**:
    お客様側での具体的な対処は不要です。ロールアウトの進行を待つことで、自動的に最新バージョンが適用されます。特定の機能や修正が必要な場合は、ロールアウトの完了状況を適宜ご確認ください。

*   **用語説明**:
    *   **ロールアウト (Rollout)**: ソフトウェアの新しいバージョンや機能が、システム全体またはユーザー全体に段階的に展開・適用されるプロセスのことです。Google Cloudのような大規模なシステムでは、一度に全てのユーザーやリージョンに適用するのではなく、影響を最小限に抑えながら段階的に導入されます。

## Security

*   **原文**:
    | Bug ID | Description |
    | --- | --- |
    | **495897297, 495909767** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:  - CVE-2026-33210- CVE-2026-25679- CVE-2026-27139- CVE-2026-27142- 2026-33186 |
    [CVE-2026-33210](https://nvd.nist.gov/vuln/detail/CVE-2026-33210)
    [CVE-2026-25679](https://nvd.nist.gov/vuln/detail/CVE-2026-25679)
    [CVE-2026-27139](https://nvd.nist.gov/vuln/detail/CVE-2026-27139)
    [CVE-2026-27142](https://nvd.nist.gov/vuln/detail/CVE-2026-27142)
    [2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186)

*   **説明**:
    Apigeeの基盤インフラストラクチャに対するセキュリティ修正が実施されました。これにより、複数のCVE（共通脆弱性識別子）に関連する既知の脆弱性（CVE-2026-33210, CVE-2026-25679, CVE-2026-27139, CVE-2026-27142, 2026-33186）が解決されました。

*   **影響有無**:
    ポジティブな影響あり。Apigee XはGoogleが管理するフルマネージドサービスのため、基盤レベルのセキュリティ修正はお客様の操作なしに自動的に適用され、サービスのセキュリティ体制が向上します。お客様の既存のワークロードへの直接的な影響はありませんが、サービスがよりセキュアになります。

*   **対処方法**:
    お客様側での対処は不要です。Google Cloudによって自動的に修正が適用されます。

*   **用語説明**:
    *   **CVE (Common Vulnerabilities and Exposures)**: サイバーセキュリティの脆弱性を識別するための国際的な標準規格です。各脆弱性には一意のCVE識別番号が付与され、これによってセキュリティに関する情報共有や対応が効率化されます。
    *   **基盤インフラストラクチャ (Infrastructure)**: コンピューティング、ストレージ、ネットワークなどのITサービスを構成する物理的および仮想的なハードウェアとソフトウェアのことです。Apigee Xの場合、これをGoogle Cloudが管理しています。

## Fixed

*   **原文**:
    | Bug ID | Description |
    | --- | --- |
    | **N/A** | **Updates to infrastructure and libraries.** |

*   **説明**:
    Apigeeの基盤インフラストラクチャおよび使用されているライブラリの更新が実施されました。

*   **影響有無**:
    影響なし。Apigee XはGoogleが管理するフルマネージドサービスであり、これらの更新はサービスの安定性、パフォーマンス、またはメンテナンス性の向上を目的としてGoogle側で実施されます。お客様の既存の構成やAPI動作に直接的な影響を与える変更ではありません。

*   **対処方法**:
    お客様側での対処は不要です。

*   **用語説明**:
    *   **ライブラリ (Library)**: プログラムの構築に役立つ、再利用可能なコードの集合体です。共通の機能を提供し、開発者がゼロから全てを記述する必要がないようにします。セキュリティ修正やパフォーマンス改善のために定期的に更新されます。

---

ご不明な点がございましたら、お気軽にお問い合わせください。
# Title: March 25, 2026 
Link: https://docs.cloud.google.com/release-notes#March_25_2026<br>
ご担当者様

Google Cloudのリリースノートに基づく製品への影響調査の結果をご報告いたします。
構築済みのGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) の利用状況も踏まえて評価しました。

---

# AlloyDB for PostgreSQL
## Change
原文: When no major version is specified, AlloyDB for PostgreSQL now defaults to PostgreSQL major version 17 for new clusters.
説明: 新しいAlloyDB for PostgreSQLクラスタを作成する際に、メジャーバージョンを明示的に指定しなかった場合、デフォルトでPostgreSQLのメジャーバージョン17が選択されるようになりました。
影響有無: **一部影響あり**
*   **既存のAlloyDBクラスタ**: 影響はありません。既存クラスタのPostgreSQLバージョンが自動的に変更されることはありません。
*   **新規AlloyDBクラスタ**: 影響があります。今後クラスタを作成する際にバージョンを明示的に指定しない場合、意図せずPostgreSQL 17がデプロイされる可能性があります。もしPostgreSQL 16以前のバージョンを想定している場合は、明示的なバージョン指定が必要です。
対処方法:
*   新規にAlloyDB for PostgreSQLクラスタを作成する際に、意図するPostgreSQLメジャーバージョン（例: 16）を使用したい場合は、クラスタ作成時にそのバージョンを明示的に指定してください。
*   PostgreSQL 17へのアップグレードを検討している場合は、事前にアプリケーションやSQLクエリがPostgreSQL 17の新機能や変更点、非推奨となった機能に対応しているか、互換性テストを実施することを推奨します。
用語説明:
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、PostgreSQLと完全に互換性のあるエンタープライズグレードのマネージドデータベースサービスです。高いパフォーマンス、可用性、スケーラビリティを特徴とします。
*   **PostgreSQL major version 17**: PostgreSQLデータベースソフトウェアのメジャーバージョンの一つで、新しい機能、パフォーマンス改善、バグ修正などが含まれます。メジャーバージョンアップグレードは、非互換性のある変更を含む場合があるため、アプリケーションの互換性確認が重要となります。

---

# BigQuery
## Announcement
原文: The Gemini for Google Cloud API (cloudaicompanion.googleapis.com) is now enabled for existing BigQuery projects in the European jurisdiction.
説明: Gemini for Google Cloud API (`cloudaicompanion.googleapis.com`) が、欧州司法管轄区域に属する既存のBigQueryプロジェクトで利用可能になりました。
影響有無: **直接的な影響なし（機能拡張によるプラスの影響の可能性あり）**
*   **既存のBigQueryプロジェクト（欧州司法管轄区域外）**: 影響はありません。
*   **既存のBigQueryプロジェクト（欧州司法管轄区域内）**: 新たな機能（Gemini for Google Cloud API）が利用可能になったことを意味しますが、既存のワークロードが自動的に変更されたり、影響を受けたりすることはありません。必要に応じて、AI機能を活用したデータ分析やアプリケーション統合の可能性が広がります。
対処方法:
*   欧州司法管轄区域内に拠点を置くプロジェクトで、Google Cloudの生成AI機能（Gemini）の利用を検討している場合は、APIの有効化や利用方法について公式ドキュメントを参照し、ワークロードへの適用を検討してください。
*   データ所在地に関する企業ポリシー（データレジデンシー）が、Gemini APIの利用条件と合致しているか確認してください。
用語説明:
*   **Gemini for Google Cloud API**: Google Cloud上で利用可能な、Googleの高度な生成AIモデル「Gemini」にアクセスするためのAPIです。自然言語処理、画像生成、コード生成など、多岐にわたるAI機能をアプリケーションに統合できます。
*   **欧州司法管轄区域 (European jurisdiction)**: 欧州連合 (EU) および欧州経済領域 (EEA) のデータ保護規制（例: GDPR）が適用される地理的範囲を指します。この地域でのサービス提供やデータ処理には、厳格なデータプライバシーとセキュリティ要件が課せられます。

---

# Google Kubernetes Engine (GKE)
## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image: (table omitted for brevity)
説明: 今回のリリースには、Container-Optimized OS (COS) イメージを更新した新しいGKEバージョンが含まれています。これらのCOSイメージの更新には、前回のGKEリリース以降に公開されたすべてのCOSバージョンからのセキュリティ修正が累積的に適用されています。各COSイメージで解決された特定の脆弱性については、該当するCOSのセキュリティリリースノートを参照してください。
影響有無: **セキュリティ体制の向上（プラスの影響）**
*   **既存のGKEクラスタ**: GKEの自動アップグレードが有効な場合、クラスタのコントロールプレーンやノードがこれらの新しいGKEバージョンにアップグレードされることで、間接的にCOSイメージのセキュリティ修正が適用され、セキュリティ体制が向上します。手動で管理しているクラスタも、新しいGKEバージョンにアップグレードすることで同様に恩恵を受けます。
*   **新規GKEクラスタ**: 新しいGKEバージョンでクラスタを構築した場合、最初からセキュリティ修正が適用されたCOSイメージが使用されます。
*   **Google Cloud Composer2**: Composerは内部でGKEクラスタを使用しており、通常、Google Cloudが基盤となるGKEのセキュリティアップデートを管理します。ユーザーが直接操作することは少ないですが、基盤のセキュリティが向上することで、Composer環境全体のセキュリティも強化されると期待できます。
対処方法:
*   GKEクラスタの自動アップグレードを有効にすることを強く推奨します。これにより、セキュリティ修正が自動的に適用され、運用上の負担が軽減されます。
*   手動でGKEクラスタのバージョンを管理している場合は、計画的なアップグレードを実施し、新しいGKEバージョンに更新してください。アップグレード前に、リリースノートを確認し、既知の問題がないか確認することが重要です。
*   Google Cloud Composer2の利用者は、Composerのメンテナンスウィンドウやバージョンポリシーに従ってください。通常、基盤のGKEのアップグレードはGoogle Cloudによって管理されます。
用語説明:
*   **Container-Optimized OS (COS)**: Google Cloudが提供する、コンテナの実行に特化して最適化されたオペレーティングシステムです。セキュリティ、信頼性、管理性が重視されており、GKEノードのOSとして広く利用されています。
*   **累積的なセキュリティ修正 (Cumulative security fixes)**: 以前のすべてのセキュリティ修正が含まれていることを意味します。最新バージョンにアップグレードすることで、それまでのすべてのセキュリティパッチが適用されます。

## Change
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
説明: GKEクラスタのバージョンが更新され、新規クラスタの作成、既存クラスタのコントロールプレーンおよびノードの手動アップグレードで利用可能な新しいバージョンが提供されました。
影響有無: **直接的な影響なし（機能強化の機会）**
*   **既存のGKEクラスタ**: 自動アップグレードポリシーやメンテナンスウィンドウの設定に応じて、クラスタが新しいバージョンに自動的にアップグレードされる可能性があります。手動管理している場合は、アップグレードの選択肢が増えます。
*   **新規GKEクラスタ**: 最新の安定したバージョンでクラスタを構築できるようになります。
*   **Google Cloud Composer2**: Composerの基盤GKEクラスタはGoogle Cloudによって管理されるため、通常、ユーザーが直接GKEバージョンを選択・アップグレードすることはありません。Composer環境は、Google Cloudによって互換性が確認されたGKEバージョンに順次更新されていくと考えられます。
対処方法:
*   現在利用中のGKEバージョンとアップグレード先のバージョンについて、Kubernetesの変更ログやGKEのリリースノートを確認し、APIの非推奨化や互換性に影響する変更がないか事前に確認してください。
*   可能であれば、開発環境やステージング環境で事前にアップグレードをテストしてください。
*   自動アップグレードが有効な場合、メンテナンスウィンドウを設定し、意図しないタイミングでのアップグレードを防ぐようにしてください。
用語説明:
*   **GKE cluster versions**: Google Kubernetes Engineが提供するKubernetesのバージョンです。Kubernetes自体のバージョンと、Google Cloudが提供するGKE固有の機能や修正が含まれます。
*   **Control plane upgrade**: Kubernetesクラスタのコントロールプレーン（APIサーバー、スケジューラー、コントローラーマネージャーなど）のアップグレードです。
*   **Node upgrade**: クラスタのワーカーノード（コンテナが実行されるVMインスタンス）のアップグレードです。

## Change
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - Version 1.33.8-gke.1026000 is now the default version for cluster creation in the Stable channel. - The following versions are now available in the Stable channel: 1.32.12-gke.1076000, 1.33.8-
# Title: March 24, 2026 
Link: https://docs.cloud.google.com/release-notes#March_24_2026<br>
# Cloud Storage
## Announcement
原文: Anywhere Cache has been renamed to Rapid Cache.
説明：Cloud Storage の機能である「Anywhere Cache」が「Rapid Cache」に名称変更されました。これは機能そのものの変更ではなく、機能名の変更です。
影響有無：直接的な機能影響はありません。既存のCloud Storageの構成やアプリケーション動作に変更は不要です。管理コンソールやドキュメント上での名称表記が変更される可能性があります。
対処方法：既存のシステムやコードに変更の必要はありません。将来的にドキュメントやGoogle Cloud Console上での表記が新名称に変わることを認識しておいてください。
用語説明：
*   **Anywhere Cache / Rapid Cache**: Cloud Storage のパフォーマンス最適化機能の一つで、ユーザーの地理的な位置に近いエッジロケーションにデータをキャッシュすることで、アクセスレイテンシを大幅に削減します。特に、グローバル外部ロードバランサ (Global External Load Balancer) を介してコンテンツを配信する際に、オリジンとなるCloud Storageバケットへのアクセスを高速化するために利用されます。今回の変更は機能名の変更のみであり、その機能自体に変更はありません。
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
Cloud BillingアカウントのIAM権限に新しい更新が適用され、`billing.accounts.updatePaymentInfo` 権限を持つユーザーが、関連するGoogle支払いプロファイル（Google payments profile）および支払いアカウント（payments accounts）へのアクセスと編集が簡素化されました。

これまでは、Cloud Billingコンソールから支払いプロファイル情報を操作・編集するには、Cloud Billingアカウントに対するIAM権限と、Google支払いプロファイルに対する個別の編集または管理者権限という、2つの異なる権限セットが必要でした。今回の更新により、`billing.accounts.updatePaymentInfo` 権限（`roles/billing.admin` ロールに含まれるか、カスタムロールで付与されている場合）を持つユーザーは、Google支払いプロファイルに別途権限を付与することなく、Cloud Billingコンソールから直接支払いプロファイル情報にアクセスし、編集できるようになります。

この変更は、組織（Organization）またはビジネス（Business）タイプのGoogle支払いプロファイルに関連付けられたCloud Billingアカウントにのみ適用されます。この権限を持つユーザーは、支払い履歴の閲覧、支払い方法の追加・編集、手動支払い、ビジネス名・住所・税情報などの支払いプロファイル情報の更新が可能です。ただし、「ユーザーの管理」や「全ての権限を持つ管理者」といったGoogle支払いプロファイルに対する完全な管理権限は付与されず、それには引き続き支払いプロファイル自体に追加の権限が必要です。

影響有無：
**影響なし**

この変更は、Google Cloud Billingアカウントの支払いプロファイル情報へのアクセス管理を簡素化するものです。既存のシステムやアプリケーションの動作に直接的な影響はありません。むしろ、特定のIAM権限を持つユーザー（特に請求管理者）にとって、支払い情報の管理がより効率的になるポジティブな変更です。セキュリティモデルが緩和されるわけではなく、アクセス経路が統合され、管理者の利便性が向上します。

対処方法：
特別な対処は不要です。
ただし、請求管理者向けの運用手順書や、IAM権限管理に関する内部ドキュメントがある場合は、この変更を反映させることで、管理者の作業が効率化され、権限管理の複雑さが軽減される可能性があります。

用語説明：
*   **Cloud Billingアカウント**: Google Cloudのサービス利用料を請求・管理するためのアカウントです。組織やプロジェクトに関連付けられます。
*   **Google payments profile (支払いプロファイル)**: Googleの各種サービス（Google Cloud、Google Ads、Google Workspaceなど）全体で利用される、支払い情報（クレジットカード、銀行口座、住所、税情報など）を一元的に管理するためのプロファイルです。個人用、ビジネス用などのタイプがあります。
*   **IAM (Identity and Access Management)**: Google Cloudのリソース（プロジェクト、Cloud Billingアカウントなど）に対するアクセス権限を細かく制御するためのサービスです。誰が（Principal）、どのリソースに対して（Resource）、どのような操作を（Role）できるかを定義します。
*   **`billing.accounts.updatePaymentInfo`**: Cloud Billingアカウントの支払い情報（支払い方法、住所など）を更新するための権限です。この権限は、`roles/billing.admin` (Cloud Billingアカウント管理者) ロールにデフォルトで含まれています。
*   **`roles/billing.admin` (Cloud Billingアカウント管理者)**: Cloud Billingアカウントに対する広範な管理権限を持つIAMロールです。支払い方法の管理、予算の設定、請求レポートの閲覧などが可能です。
*   **カスタムロール**: Google CloudのIAMにおいて、プリセットされたロール（事前定義ロール）では満たせない特定の権限セットを、ユーザーが独自に作成・定義できるロールです。これにより、最小権限の原則に基づいたきめ細やかな権限管理が可能になります。